from hcc import Diagnosis, Beneficiary, ICDType, score, regvars, EntitlementReason, Vars
from pyDatalog import pyDatalog

raf_type_lookup = {'CFA': 'valid_community_aged_variables', 'CFD': 'valid_community_disabled_variables',
                   'CNA': 'valid_community_aged_variables', 'CND': 'valid_community_disabled_variables',
                   'CPA': 'valid_community_aged_variables', 'CPD': 'valid_community_disabled_variables'}

sex_lookup = {'f': 'female', 'm': 'male'}


def format_date(date): return ''.join(date.split('-'))


def get_orec(RAF_type):

    char1, char2, char3 = RAF_type

    if char1 == 'E' and char3 == 'D':
        orec = 3
    else:
        orec = {'A': 0, 'D': 1}[char3]

    return orec


def get_scores(hicno, sex, dob, age_upto, RAF_type=None, orec=None, medicaid=True, codes=[]):

    formatted_dob = format_date(dob)

    formatted_age_upto = format_date(age_upto)

    formatted_sex = sex_lookup[sex.lower()]

    # if RAF_type:

    RAF_type = RAF_type.upper()

    if RAF_type not in raf_type_lookup.keys():
        print("invalid RAF_type: {}".format(RAF_type))
        return

    if not orec:

        temp_orec = get_orec(RAF_type)

        print('RAF_type :{} , Assuming OREC :{}'.format(RAF_type, temp_orec))

        person = Beneficiary(hicno=hicno, sex=formatted_sex, dob=formatted_dob,
                                age_upto=formatted_age_upto, original_reason_entitlement=temp_orec, medicaid=medicaid, )

    else:
        if orec not in [0, 1, 2, 3]:
            print("invaild original_reason_entitlement : {}".format(orec))
            return

        else:
            temp_orec = orec

            person = Beneficiary(hicno=hicno, sex=formatted_sex, dob=formatted_dob,
                                    age_upto=formatted_age_upto, original_reason_entitlement=temp_orec, medicaid=medicaid, )
    
    print(person)

    # else:
    #     print("caluclating codes for all the RAF types")

    #     cc
    #         if not orec:
    #             temp_orec = get_orec(RAF_type)

    #             print("calulating scores for RAF_type {}, assuming orec: {}".format(
    #                 RAF_type, temp_orec))

    #         else:
    #             temp_orec = orec

    #         person = Beneficiary(hicno=hicno, sex=formatted_sex, dob=formatted_dob,
    #                              age_upto=formatted_age_upto, original_reason_entitlement=temp_orec, medicaid=medicaid, )

    #         print(person)
    
    for code in codes:

        print('adding code :{}'.format(code))

        add_diagnosis_code(person, code)
    
    out_df= []

    for RAF_type in raf_type_lookup.keys():

        pyDatalog.create_terms("Vars")
        

        temp_raf_type= raf_type_lookup[RAF_type] 

        conditiion_categories= regvars(person, temp_raf_type, Vars)[0][0].split(',')

        temp = {temp_raf_type: conditiion_categories}

        print(temp)

        out_df.append(temp)

    return out_df



def add_diagnosis_code(Beneficiary, code):
    Beneficiary.add_diagnosis(Diagnosis(Beneficiary,code,ICDType.TEN))

