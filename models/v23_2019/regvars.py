def HCCV23_list83():
    return ['HCC1', 'HCC2', 'HCC6', 'HCC8', 'HCC9', 'HCC10', 'HCC11',
            'HCC12', 'HCC17', 'HCC18', 'HCC19', 'HCC21', 'HCC22', 'HCC23',
            'HCC27', 'HCC28', 'HCC29', 'HCC33', 'HCC34', 'HCC35', 'HCC39', 'HCC40',
            'HCC46', 'HCC47', 'HCC48', 'HCC54', 'HCC55', 'HCC56', 'HCC57', 'HCC58',
            'HCC59','HCC60', 'HCC70', 'HCC71', 'HCC72', 'HCC73', 'HCC74', 'HCC75',
            'HCC76', 'HCC77', 'HCC78', 'HCC79', 'HCC80', 'HCC82', 'HCC83', 'HCC84',
            'HCC85', 'HCC86', 'HCC87', 'HCC88', 'HCC96', 'HCC99', 'HCC100', 'HCC103',
            'HCC104', 'HCC106', 'HCC107', 'HCC108', 'HCC110', 'HCC111', 'HCC112',
            'HCC114', 'HCC115', 'HCC122', 'HCC124', 'HCC134', 'HCC135', 'HCC136',
            'HCC137', 'HCC138', 'HCC157', 'HCC158', 'HCC161', 'HCC162', 'HCC166',
            'HCC167', 'HCC169', 'HCC170', 'HCC173', 'HCC176', 'HCC186', 'HCC188', 'HCC189']


def AGESEXVA():
    # age/sex variables for Community Aged regression
    return ['F65_69', 'F70_74', 'F75_79', 'F80_84', 'F85_89',
            'F90_94', 'F95_GT', 'M65_69', 'M70_74', 'M75_79',
            'M80_84', 'M85_89', 'M90_94', 'M95_GT']


def AGESEXVD():
    # age/sex variables for Community Disabled regression
    return ["F0_34", "F35_44", "F45_54", "F55_59", "F60_64",
            "M0_34", "M35_44", "M45_54", "M55_59", "M60_64"]


def DIAG_CAT():
    # diagnostic categories necessary to create interaction variables
    return ['CANCER', 'DIABETES', 'CHF', 'CARD_RESP_FAIL',
            'gCopdCF', 'RENAL_V23', 'SEPSIS', 'PRESSURE_ULCER',
            'gSubstanceAbuse_V23', 'gPsychiatric_V23',
            'gSubstanceAbuse_gPsychiatric_V23']


def ORIG_INT():
    # orig disabled interactions for Community Aged regressions
    return ["OriginallyDisabled_Female", "OriginallyDisabled_Male"]


def INTERRACC_VARSA():
    # interaction variables for Community Aged regressions
    return ["HCC47_gCancer", "HCC85_gDiabetesMellit", "HCC85_gCopdCF", "HCC85_gRenal_V23",
            "gRespDepandArre_gCopdCF", "HCC85_HCC96"]


def INTERRACC_VARSD():
    # interaction variables for Community Disabled regressions
    return ["HCC47_gCancer", "HCC85_gDiabetesMellit", "HCC85_gCopdCF", "HCC85_gRenal_V23",
            "gRespDepandArre_gCopdCF", "HCC85_HCC96", "disable_substAbuse_psych_V23"]


def AGESEXV():
    # age/sex variables for Insititutional regression
    return ["F0_34", "F35_44", "F45_54", "F55_59", "F60_64", "F65_69",
            "F70_74", "F75_79", "F80_84", "F85_89", "F90_94", "F95_GT",
            "M0_34", "M35_44", "M45_54", "M55_59", "M60_64", "M65_69",
            "M70_74", "M75_79", "M80_84", "M85_89", "M90_94", "M95_GT"]


def INTERRACI_VARS():
    # interaction variables for Institutional regression
    return ["DISABLED_HCC85", "DISABLED_PRESSURE_ULCER",
            "DISABLED_HCC161", "DISABLED_HCC39", "DISABLED_HCC77", "DISABLED_HCC6",
            "CHF_gCopdCF", "gCopdCF_CARD_RESP_FAIL", "SEPSIS_PRESSURE_ULCER", "SEPSIS_ARTIF_OPENINGS",
            "ART_OPENINGS_PRESS_ULCER", "DIABETES_CHF", "gCopdCF_ASP_SPEC_B_PNEUM", "ASP_SPEC_B_PNEUM_PRES_ULC",
            "SEPSIS_ASP_SPEC_BACT_PNEUM", "SCHIZOPHRENIA_gCopdCF", "SCHIZOPHRENIA_CHF", "SCHIZOPHRENIA_SEIZURES"]


def NE_AGESEXV():
    # age/sex variables for non-ORIGDS New Enrollee and SNP New Enrollee
    #  interactions
    return ['NEF0_34', 'NEF35_44', 'NEF45_54', 'NEF55_59',
            'NEF60_64', 'NEF65', 'NEF66', 'NEF67', 'NEF68',
            'NEF69', 'NEF70_74', 'NEF75_79', 'NEF80_84',
            'NEF85_89', 'NEF90_94', 'NEF95_GT', 'NEM0_34',
            'NEM35_44', 'NEM45_54', 'NEM55_59', 'NEM60_64',
            'NEM65', 'NEM66', 'NEM67', 'NEM68', 'NEM69',
            'NEM70_74', 'NEM75_79', 'NEM80_84', 'NEM85_89',
            'NEM90_94', 'NEM95_GT']



def ONE_AGESEXV():
    # age/sex variables for ORIGDS New Enrollee and SNP New Enrollee
    #  interactions
    return ['NEF65', 'NEF66', 'NEF67', 'NEF68', 'NEF69', 'NEF70_74', 'NEF75_79', 'NEF80_84', 'NEF85_89', 'NEF90_94', 'NEF95_GT',
            'NEM65', 'NEM66', 'NEM67', 'NEM68', 'NEM69', 'NEM70_74', 'NEM75_79', 'NEM80_84', 'NEM85_89', 'NEM90_94', 'NEM95_GT']


def NE_REG():
    # variables for New Enrollee and SNP New Enrollee regression
    return ['NMCAID_NORIGDIS_NEF0_34', 'NMCAID_NORIGDIS_NEF35_44', 'NMCAID_NORIGDIS_NEF45_54', 'NMCAID_NORIGDIS_NEF55_59',
            'NMCAID_NORIGDIS_NEF60_64', 'NMCAID_NORIGDIS_NEF65', 'NMCAID_NORIGDIS_NEF66', 'NMCAID_NORIGDIS_NEF67', 'NMCAID_NORIGDIS_NEF68',
            'NMCAID_NORIGDIS_NEF69', 'NMCAID_NORIGDIS_NEF70_74', 'NMCAID_NORIGDIS_NEF75_79', 'NMCAID_NORIGDIS_NEF80_84', 'NMCAID_NORIGDIS_NEF85_89',
            'NMCAID_NORIGDIS_NEF90_94', 'NMCAID_NORIGDIS_NEF95_GT',  'NMCAID_NORIGDIS_NEM0_34', 'NMCAID_NORIGDIS_NEM35_44', 'NMCAID_NORIGDIS_NEM45_54',
            'NMCAID_NORIGDIS_NEM55_59', 'NMCAID_NORIGDIS_NEM60_64', 'NMCAID_NORIGDIS_NEM65', 'NMCAID_NORIGDIS_NEM66', 'NMCAID_NORIGDIS_NEM67',
            'NMCAID_NORIGDIS_NEM68', 'NMCAID_NORIGDIS_NEM69', 'NMCAID_NORIGDIS_NEM70_74', 'NMCAID_NORIGDIS_NEM75_79', 'NMCAID_NORIGDIS_NEM80_84',
            'NMCAID_NORIGDIS_NEM85_89', 'NMCAID_NORIGDIS_NEM90_94', 'NMCAID_NORIGDIS_NEM95_GT',  'MCAID_NORIGDIS_NEF0_34', 'MCAID_NORIGDIS_NEF35_44',
            'MCAID_NORIGDIS_NEF45_54', 'MCAID_NORIGDIS_NEF55_59', 'MCAID_NORIGDIS_NEF60_64', 'MCAID_NORIGDIS_NEF65', 'MCAID_NORIGDIS_NEF66', 'MCAID_NORIGDIS_NEF67',
            'MCAID_NORIGDIS_NEF68', 'MCAID_NORIGDIS_NEF69', 'MCAID_NORIGDIS_NEF70_74', 'MCAID_NORIGDIS_NEF75_79', 'MCAID_NORIGDIS_NEF80_84', 'MCAID_NORIGDIS_NEF85_89',
            'MCAID_NORIGDIS_NEF90_94', 'MCAID_NORIGDIS_NEF95_GT',  'MCAID_NORIGDIS_NEM0_34', 'MCAID_NORIGDIS_NEM35_44', 'MCAID_NORIGDIS_NEM45_54',
            'MCAID_NORIGDIS_NEM55_59', 'MCAID_NORIGDIS_NEM60_64', 'MCAID_NORIGDIS_NEM65', 'MCAID_NORIGDIS_NEM66', 'MCAID_NORIGDIS_NEM67',
            'MCAID_NORIGDIS_NEM68', 'MCAID_NORIGDIS_NEM69', 'MCAID_NORIGDIS_NEM70_74', 'MCAID_NORIGDIS_NEM75_79', 'MCAID_NORIGDIS_NEM80_84',
            'MCAID_NORIGDIS_NEM85_89', 'MCAID_NORIGDIS_NEM90_94', 'MCAID_NORIGDIS_NEM95_GT',  'NMCAID_ORIGDIS_NEF65', 'NMCAID_ORIGDIS_NEF66',
            'NMCAID_ORIGDIS_NEF67', 'NMCAID_ORIGDIS_NEF68', 'NMCAID_ORIGDIS_NEF69', 'NMCAID_ORIGDIS_NEF70_74', 'NMCAID_ORIGDIS_NEF75_79',
            'NMCAID_ORIGDIS_NEF80_84', 'NMCAID_ORIGDIS_NEF85_89', 'NMCAID_ORIGDIS_NEF90_94', 'NMCAID_ORIGDIS_NEF95_GT',
            'NMCAID_ORIGDIS_NEM65', 'NMCAID_ORIGDIS_NEM66', 'NMCAID_ORIGDIS_NEM67', 'NMCAID_ORIGDIS_NEM68', 'NMCAID_ORIGDIS_NEM69', 'NMCAID_ORIGDIS_NEM70_74',
            'NMCAID_ORIGDIS_NEM75_79', 'NMCAID_ORIGDIS_NEM80_84', 'NMCAID_ORIGDIS_NEM85_89', 'NMCAID_ORIGDIS_NEM90_94', 'NMCAID_ORIGDIS_NEM95_GT',  'MCAID_ORIGDIS_NEF65',
            'MCAID_ORIGDIS_NEF66', 'MCAID_ORIGDIS_NEF67', 'MCAID_ORIGDIS_NEF68', 'MCAID_ORIGDIS_NEF69', 'MCAID_ORIGDIS_NEF70_74', 'MCAID_ORIGDIS_NEF75_79', 'MCAID_ORIGDIS_NEF80_84',
            'MCAID_ORIGDIS_NEF85_89', 'MCAID_ORIGDIS_NEF90_94', 'MCAID_ORIGDIS_NEF95_GT',   'MCAID_ORIGDIS_NEM65', 'MCAID_ORIGDIS_NEM66', 'MCAID_ORIGDIS_NEM67',
            'MCAID_ORIGDIS_NEM68', 'MCAID_ORIGDIS_NEM69', 'MCAID_ORIGDIS_NEM70_74', 'MCAID_ORIGDIS_NEM75_79', 'MCAID_ORIGDIS_NEM80_84', 'MCAID_ORIGDIS_NEM85_89', 'MCAID_ORIGDIS_NEM90_94', 'MCAID_ORIGDIS_NEM95_GT']


##############################################################################

def community_regression_aged():
    # variables for Community Aged regressions
    return [] + AGESEXVA() + ORIG_INT() + HCCV23_list83() + INTERRACC_VARSA()


def community_regression_disabled():
    # variables for Community Disabled regressions
    return [] + AGESEXVD() + HCCV23_list83() + INTERRACC_VARSD()


def institutional_regression():
    # variables for Institutional regression;
    return [] + AGESEXV() + INTERRACI_VARS() + HCCV23_list83() + ["LTIMCAID", "ORIGDS"]


def new_enrollee_regression():
    # variables for New Enrollee and SNP New Enrollee regression
    return [] + NE_REG()

##############################################################################


def get_age_entitlement_diag_vars():

    temp_dict= {

        ("CFA", "CNA", "CPA"): {
            "age": AGESEXVA(),
            "entl": [] + ORIG_INT() + INTERRACC_VARSA(),
            'diag': HCCV23_list83()
        },

        ("CFD", "CND", "CPD"): {
            "age": AGESEXVA(),
            "entl": INTERRACC_VARSA(),
            'diag': HCCV23_list83()
        },

        ("NE", "SNPE"): {
            "age": [],
            "entl": NE_REG(),
            'diag': []
        },

        "INS": {
            "age": AGESEXVA(),
            "entl": []+INTERRACI_VARS()+ ["LTIMCAID", "ORIGDS"],
            'diag': HCCV23_list83()
        }
    }

    out_dict= {}


    for k,v in temp_dict.items():
        if type(k)==tuple :
            for e in k:
                out_dict[e]= v
        else:
            out_dict[k]= v

    return out_dict