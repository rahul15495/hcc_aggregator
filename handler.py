from pyDatalog import pyDatalog
from model_crosswalk import select_model
import traceback
import pandas as pd
import importlib

raf_type_lookup = {'CFA': ('valid_community_aged_variables', 'community_full_benefit_dual_aged'),
                        'CFD': ('valid_community_disabled_variables', 'community_full_benefit_dual_disabled'),
                        'CNA': ('valid_community_aged_variables', 'community_nondual_aged'),
                        'CND': ('valid_community_disabled_variables', 'community_nondual_disabled'),
                        'CPA': ('valid_community_aged_variables', 'community_partial_benefit_dual_aged'),
                        'CPD': ('valid_community_disabled_variables', 'community_partial_benefit_dual_disabled'),
                        'NE': ('valid_new_enrollee_variables', 'new_enrollee'),
                        'SNPE': ('valid_new_enrollee_variables', 'snp_new_enrollee'),
                        'INS': ('valid_institutional_variables', 'institutional'),
                        'DI':  ('valid_dialysis_variables', 'dialysis'),
                        'DNE': ('valid_dialysis_new_enrollee_variables', 'dialysis_new_enrollee'),
                        'GC':  ('valid_functioning_graft_community_variables', 'functioning_graft_community'),
                        'GI':  ('valid_functioning_graft_institutional_variables', 'functioning_graft_institutional'),
                        'GNE': ('valid_functioning_graft_new_enrolle_regression_variables', 'functioning_graft_new_enrolle'),
                        'CE': ('valid_community_variables','community')
                        }

sex_lookup = {'f': 'female', 'm': 'male'}




def format_date(date): return ''.join(date.split('-'))



def get_scores(hicno, sex, dob, year_of_eligibility,month_of_eligibility='02', RAF_type=None, lob=None, orec=0, medicaid=True, codes=[]):
    try:

        global model

        RAF_type = RAF_type.upper()

        combined_df= []

        combined_score =0

        for params in select_model(year_of_eligibility, RAF_type,lob):
            print(params)

            try:
                _, weight, model_name , coefficients_file_path, _payment_year= params

                model= importlib.import_module("models.{}.hcc".format(model_name))


            except:
                print("invalid RAF_type: {}".format(RAF_type))
                print(traceback.format_exc())
                return
            
            try:
                coefficients_df = pd.read_csv(
                    coefficients_file_path, names=['raf_type', 'coeff', 'contribution_category'], float_precision='high')

                coefficients_df['raf_type']= coefficients_df['raf_type'].str.upper()

                # print(coefficients_df.head())

            except:

                print('coefficients file not found : {}'.format(coefficients_file_path))

            def get_coeff(x):
                # print(x)
                temp =coefficients_df[coefficients_df['raf_type'] == x].values[0]

                return temp[2], temp[1]

            formatted_dob = format_date(dob)

            age_upto = "-".join([year_of_eligibility, month_of_eligibility, '01'])

            # print(age_upto)

            formatted_age_upto = format_date(age_upto)

            formatted_sex = sex_lookup[sex.lower()]

            if orec not in [0, 1, 2, 3]:
                print("invaild original_reason_entitlement : {}".format(orec))
                return

            else:
                temp_orec = orec

                person = model.Beneficiary(hicno=hicno, sex=formatted_sex, dob=formatted_dob,
                                    age_upto=formatted_age_upto, original_reason_entitlement=temp_orec, medicaid=medicaid, )

            for code in codes:

                add_diagnosis_code(person, code)

            pyDatalog.create_terms("Vars, ScoreVar")

            temp_raf_type = raf_type_lookup[RAF_type][0]

            hcc_reg_variables_list = model.regvars(person, temp_raf_type, model.Vars)


            t = raf_type_lookup[RAF_type][1]


            out_df = {}

            out_df['RAF_TYPE'] = RAF_type
            out_df['raf_contribution']= {
                'Demographic': [],
                'Clinical': [],
                'Entitlement Class': []
            }

            score= 0
            if len(hcc_reg_variables_list) > 0:

                condition_categories = hcc_reg_variables_list[
                    0][0].split(',')



                for temp_category in condition_categories:

                    formatted_category = "{}_{}".format(
                        RAF_type, temp_category.upper())

                    category,temp_coeff = get_coeff(formatted_category)

                    out_df['raf_contribution'][category].append({temp_category: temp_coeff})

                    score+= temp_coeff

                score= float(format(score, '0.3f'))
                
                combined_score += score*weight

                combined_score= float(format(combined_score, '0.3f'))


            combined_df.append({'Model':model_name.split('_')[0] ,
                            'Payment_Year': _payment_year,
                            'RAF_TYPE': out_df['RAF_TYPE'],
                            'Raf_Contribution': out_df['raf_contribution'],
                            'Score': score})

            pyDatalog.clear()

        final_df = {'models': combined_df, 'final_score': combined_score}


        return final_df
    
    except :
        print(traceback.format_exc())
        return None


def add_diagnosis_code(Beneficiary, code):
    Beneficiary.add_diagnosis(model.Diagnosis(Beneficiary, code, model.ICDType.TEN))
