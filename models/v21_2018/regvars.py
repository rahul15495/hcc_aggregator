def HCCV21_list87():
    return ['HCC1', 'HCC2', 'HCC6', 'HCC8', 'HCC9', 'HCC10', 'HCC11', 'HCC12',
            'HCC17', 'HCC18', 'HCC19', 'HCC21', 'HCC22', 'HCC23', 'HCC27',
            'HCC28', 'HCC29', 'HCC33', 'HCC34', 'HCC35', 'HCC39', 'HCC40',
            'HCC46', 'HCC47', 'HCC48', 'HCC51', 'HCC52', 'HCC54', 'HCC55',
            'HCC57', 'HCC58', 'HCC70', 'HCC71', 'HCC72', 'HCC73', 'HCC74',
            'HCC75', 'HCC76', 'HCC77', 'HCC78', 'HCC79', 'HCC80', 'HCC82',
            'HCC83', 'HCC84', 'HCC85', 'HCC86', 'HCC87', 'HCC88', 'HCC96',
            'HCC99', 'HCC100', 'HCC103', 'HCC104', 'HCC106', 'HCC107',
            'HCC108', 'HCC110', 'HCC111', 'HCC112', 'HCC114', 'HCC115',
            'HCC122', 'HCC124', 'HCC134', 'HCC135', 'HCC136', 'HCC137',
            'HCC138', 'HCC139', 'HCC140', 'HCC141', 'HCC157', 'HCC158',
            'HCC159', 'HCC160', 'HCC161', 'HCC162', 'HCC166', 'HCC167',
            'HCC169', 'HCC170', 'HCC173', 'HCC176', 'HCC186', 'HCC188', 'HCC189']


def AGESEXV():
    #  age/sex variables for community and insititutional regression
    return ['F0_34', 'F35_44', 'F45_54', 'F55_59', 'F60_64', 'F65_69', 'F70_74',
            'F75_79', 'F80_84', 'F85_89', 'F90_94', 'F95_GT', 'M0_34', 'M35_44',
            'M45_54', 'M55_59', 'M60_64', 'M65_69', 'M70_74', 'M75_79', 'M80_84',
            'M85_89', 'M90_94', 'M95_GT']




def DIAG_CAT():
    # diagnostic categories necessary to create interaction variables
    return ['CANCER', 'DIABETES', 'IMMUNE', 'CHF', 'CARD_RESP_FAIL',
            'COPD', 'RENAL', 'COMPL', 'SEPSIS', 'PRESSURE_ULCER']


# def ORIG_INT():
#     # orig disabled interactions for Community Aged regressions
#     return ["OriginallyDisabled_Female", "OriginallyDisabled_Male"]


# def INTERRACC_VARSA():
#     # interaction variables for Community Aged regressions
#     return ["HCC47_gCancer", "HCC85_gDiabetesMellit", "HCC85_gCopdCF", "HCC85_gRenal",
#             "gRespDepandArre_gCopdCF", "HCC85_HCC96"]


def INTERRACC_VARS():
    # iinteraction variables for Community regressio
    return ['DISABLED_HCC6', 'DISABLED_HCC34', 'DISABLED_HCC46', 'DISABLED_HCC54',
            'DISABLED_HCC55', 'DISABLED_HCC110', 'DISABLED_HCC176', 'SEPSIS_CARD_RESP_FAIL',
            'CANCER_IMMUNE', 'DIABETES_CHF', 'CHF_COPD', 'CHF_RENAL', 'COPD_CARD_RESP_FAIL']





def INTERRACI_VARS():
    # interaction variables for Institutional regression
    return ["DISABLED_HCC85", "DISABLED_PRESSURE_ULCER",
            "DISABLED_HCC161", "DISABLED_HCC39", "DISABLED_HCC77", "DISABLED_HCC6",
            "CHF_COPD", "COPD_CARD_RESP_FAIL", "SEPSIS_PRESSURE_ULCER", "SEPSIS_ARTIF_OPENINGS",
            "ART_OPENINGS_PRESSURE_ULCER", "DIABETES_CHF", "COPD_ASP_SPEC_BACT_PNEUM", "ASP_SPEC_BACT_PNEUM_PRES_ULC",
            "SEPSIS_ASP_SPEC_BACT_PNEUM", "SCHIZOPHRENIA_COPD", "SCHIZOPHRENIA_CHF", "SCHIZOPHRENIA_SEIZURES"]


def NE_AGESEXV():
    # age/sex variables for non-ORIGDS New Enrollee and SNP New Enrollee
    #  interactions
    return ['NEF0_34', 'NEF35_44', 'NEF45_54', 'NEF55_59',
            'NEF60_64', 'NEF65', 'NEF66', 'NEF67', 'NEF68',
            'NEF69', 'NEF70_74', 'NEF75_79', 'NEF80_84', 'NEF85_89', 'NEF90_94', 'NEF95_GT', 'NEM0_34', 'NEM35_44',
            'NEM45_54', 'NEM55_59', 'NEM60_64', 'NEM65', 'NEM66', 'NEM67', 'NEM68', 'NEM69', 'NEM70_74', 'NEM75_79',
            'NEM80_84', 'NEM85_89', 'NEM90_94', 'NEM95_GT']


def ONE_AGESEXV():
    # age/sex variables for ORIGDS New Enrollee and SNP New Enrollee
    #  interactions
    return ['NEF65', 'NEF66', 'NEF67', 'NEF68', 'NEF69', 'NEF70_74', 'NEF75_79', 'NEF80_84', 'NEF85_89', 'NEF90_94', 'NEF95_GT',
            'NEM65', 'NEM66', 'NEM67', 'NEM68', 'NEM69', 'NEM70_74', 'NEM75_79', 'NEM80_84', 'NEM85_89', 'NEM90_94', 'NEM95_GT']


def NE_REG():
    # variables for New Enrollee and SNP New Enrollee regression
    return ['NEF0_34', 'NEF35_44', 'NEF45_54', 'NEF55_59', 'NEF60_64', 'NEF65', 'NEF66', 'NEF67', 'NEF68', 'NEF69', 'NEF70_74',
            'NEF75_79', 'NEF80_84', 'NEF85_89', 'NEF90_94', 'NEF95_GT', 'NEM0_34', 'NEM35_44', 'NEM45_54', 'NEM55_59',
            'NEM60_64', 'NEM65', 'NEM66', 'NEM67', 'NEM68', 'NEM69', 'NEM70_74', 'NEM75_79', 'NEM80_84', 'NEM85_89',
            'NEM90_94', 'NEM95_GT', 'MCAID_FEMALE0_64', 'MCAID_FEMALE65', 'MCAID_FEMALE66_69', 'MCAID_FEMALE70_74',
            'MCAID_FEMALE75_GT', 'MCAID_MALE0_64', 'MCAID_MALE65', 'MCAID_MALE66_69', 'MCAID_MALE70_74',
            'MCAID_MALE75_GT', 'Origdis_female65', 'Origdis_female66_69', 'Origdis_female70_74',
            'Origdis_female75_GT', 'Origdis_male65', 'Origdis_male66_69', 'Origdis_male70_74', 'Origdis_male75_GT']


##############################################################################

def community_regression():
    # variables for Community Aged regressions
    return [] + AGESEXV() + HCCV21_list87() + INTERRACC_VARS() + ['MCAID_Female_Aged',
                'MCAID_Female_Disabled', 'MCAID_Male_Aged', 'MCAID_Male_Disabled',
                'OriginallyDisabled_Female', 'OriginallyDisabled_Male']



def institutional_regression():
    # variables for Institutional regression;
    return [] + AGESEXV() + INTERRACI_VARS() + HCCV21_list87() + ["MCAID", "ORIGDS"]


def new_enrollee_regression():
    # variables for New Enrollee and SNP New Enrollee regression
    return [] + NE_REG()

##############################################################################


def get_age_entitlement_diag_vars():

    temp_dict= {

        ("CFA", "CNA", "CPA"): {
            "age": AGESEXV(),
            "entl": [] + ORIG_INT() + INTERRACC_VARSA(),
            'diag': HCCV21_list87()
        },

        ("CFD", "CND", "CPD"): {
            "age": AGESEXV(),
            "entl": INTERRACC_VARSA(),
            'diag': HCCV21_list87()
        },

        ("NE", "SNPE"): {
            "age": [],
            "entl": NE_REG(),
            'diag': []
        },

        "INS": {
            "age": AGESEXV(),
            "entl": []+INTERRACI_VARS()+ ["MCAID", "ORIGDS"],
            'diag': HCCV21_list87()
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