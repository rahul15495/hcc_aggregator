from pyDatalog import pyDatalog
import pandas as pd

raf_type_lookup_v22 = {'CFA': 'valid_community_aged_variables', 'CFD': 'valid_community_disabled_variables',
                       'CNA': 'valid_community_aged_variables', 'CND': 'valid_community_disabled_variables',
                       'CPA': 'valid_community_aged_variables', 'CPD': 'valid_community_disabled_variables',
                       'NE': 'valid_new_enrollee_variables', 'SNPE': 'valid_new_enrollee_variables',
                       'INS': 'valid_institutional_variables'
                       }

raf_type_lookup_esrd = {'DI': 'valid_dialysis_variables', 'DNE': 'valid_dialysis_new_enrollee_variables',
                        'GC': 'valid_functioning_graft_community_variables', 'GI': 'valid_functioning_graft_institutional_variables',
                        'GNE': 'valid_functioning_graft_new_enrolle_regression_variables'
                        }

sex_lookup = {'f': 'female', 'm': 'male'}

coefficients_file_path_v22 = 'v22/hcc_coefficients_cleaned.csv'

coefficients_file_path_esrd = "esrd/hcccoefn_cleaned.csv"

template = {
    'age': [],
    'entl': [],
    'diag': [],
    'none': []
}


def format_date(date): return ''.join(date.split('-'))

def get_score_variable(a): return "{}".format(a.replace('valid_','').replace('_variables', ''))


def get_RAF_contribution(temp_df, var):

    out = template.copy()

    for i in var:

        if i in temp_df['age']:

            out['age'].append({i: None})

        elif i in temp_df['entl']:

            out['entl'].append({i: None})

        elif i in temp_df['diag']:

            out['diag'].append({i: None})

        else:

            out['none'].append({i: None})

    return out


def get_scores(hicno, sex, dob, month_of_eligibility, year_of_eligibility, RAF_type=None, orec=0, medicaid=True, codes=[]):

    global Diagnosis, Beneficiary, ICDType, score, regvars, EntitlementReason, Vars, raf_type_lookup, get_age_entitlement_diag_vars, ScoreVar

    RAF_type = RAF_type.upper()

    if RAF_type in raf_type_lookup_v22.keys():

        from v22.hcc import Diagnosis, Beneficiary, ICDType, score, regvars, EntitlementReason, Vars, ScoreVar
        from v22.regvars import get_age_entitlement_diag_vars

        coefficients_file_path = coefficients_file_path_v22

        raf_type_lookup = raf_type_lookup_v22

    elif RAF_type in raf_type_lookup_esrd.keys():

        from esrd.hcc_esrd import Diagnosis, Beneficiary, ICDType, score, regvars, EntitlementReason, Vars, ScoreVar
        from esrd.regvars import get_age_entitlement_diag_vars

        coefficients_file_path = coefficients_file_path_esrd

        raf_type_lookup = raf_type_lookup_esrd

    else:
        print("invalid RAF_type: {}".format(RAF_type))
        return

    try:
        coefficients_df = pd.read_csv(
            coefficients_file_path, names=['raf_type', 'coeff'])

        matrix = get_age_entitlement_diag_vars()

        # print(coefficients_df.head())

    except:

        print('coefficients file not found : {}'.format(coefficients_file_path))

    def get_coeff(
        x): return coefficients_df[coefficients_df['raf_type'] == x].values[0][1]

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

        person = Beneficiary(hicno=hicno, sex=formatted_sex, dob=formatted_dob,
                             age_upto=formatted_age_upto, original_reason_entitlement=temp_orec, medicaid=medicaid, )

    for code in codes:

        add_diagnosis_code(person, code)

    pyDatalog.create_terms("Vars, ScoreVar")

    temp_raf_type = raf_type_lookup[RAF_type]

    hcc_reg_variables_list = regvars(person, temp_raf_type, Vars)

    t= get_score_variable(temp_raf_type)

    print(t)

    ben_score= score(person,t, ScoreVar)

    print(ben_score)

    out_df= {}

    out_df['RAF_TYPE']= RAF_type

    if len(hcc_reg_variables_list) > 0:

        condition_categories = hcc_reg_variables_list[
            0][0].split(',')

        raf_contribution = get_RAF_contribution(
            matrix[RAF_type], condition_categories)

        for contribution_type, temp_categories in raf_contribution.items():

            for e, temp_category_dict in enumerate(temp_categories):

                temp_category = list(temp_category_dict.keys()).pop()

                formatted_category = "{}_{}".format(
                    RAF_type.lower(), temp_category.lower())

                temp_coeff = get_coeff(formatted_category)

                temp_categories[e][temp_category] = temp_coeff

        # get condition_category coefficients

        out_df['raf_contribution']= raf_contribution

    else:
        out_df['raf_contribution']= template.copy()

    
    return out_df


def add_diagnosis_code(Beneficiary, code):
    Beneficiary.add_diagnosis(Diagnosis(Beneficiary, code, ICDType.TEN))
