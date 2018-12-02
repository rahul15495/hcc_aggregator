def ageSEX_1():

    # Age/sex cells used in dialysis CE model, functioning graft community
    #   model and functioning graft institutional model;
    return ['F0_34', 'F35_44', 'F45_54', 'F55_59', 'F60_64', 'F65_69', 'F70_74',
                'F75_79', 'F80_84', 'F85_89', 'F90_94', 'F95_GT', 'M0_34', 'M35_44',
                'M45_54', 'M55_59', 'M60_64', 'M65_69', 'M70_74', 'M75_79', 'M80_84',
                'M85_89', 'M90_94', 'M95_GT']

def moas_1():
    # Medicaid and Originally Disabled Interactions with Age and Sex used
    # in dialysis CE model and functioning graft community model
    return ['MCAID_Female_Aged', 'MCAID_Female_NonAged', 'MCAID_Male_Aged', 'MCAID_Male_NonAged',
            'OriginallyDisabled_Female', 'OriginallyDisabled_Male']

def oe():
    # Originally Disabled Interactions with ESRD and Sex
    return ['Originally_ESRD_Female', 'Originally_ESRD_Male']


def did():
    # Disease Interactions for dialysis CE model
    return ['MCAID_Female_Aged', 'MCAID_Female_NonAged', 'MCAID_Male_Aged',
            'MCAID_Male_NonAged', 'OriginallyDisabled_Female', 'OriginallyDisabled_Male']

def ddc():
    # Disabled/Disease Interactions for dialysis CE model and functioning graft community model
    return ['NONAGED_HCC6', 'NONAGED_HCC34', 'NONAGED_HCC46', 'NONAGED_HCC54',
            'NONAGED_HCC55', 'NONAGED_HCC110', 'NONAGED_HCC176']

def diag_cat():
     # Diagnostic categories necessary to create interaction variables
     return ['CANCER', 'DIABETES', 'IMMUNE', 'CHF', 'CARD_RESP_FAIL', 'COPD',
             'RENAL', 'COMPL', 'SEPSIS', 'PRESSURE_ULCER']
def dem_vars():
    return ['AGEF', 'DISABL', 'ORIGDS', 'F0_34', 'F35_44', 'F45_54', 'F55_59',
                'F60_64', 'F65_69', 'F70_74', 'F75_79', 'F80_84', 'F85_89', 'F90_94',
                'F95_GT', 'M0_34', 'M35_44', 'M45_54', 'M55_59', 'M60_64', 'M65_69',
                'M70_74', 'M75_79', 'M80_84', 'M85_89', 'M90_94', 'M95_GT', 'NEF0_34',
                'NEF35_44', 'NEF45_54', 'NEF55_59', 'NEF60_64', 'NEF65', 'NEF66', 'NEF67',
                'NEF68', 'NEF69', 'NEF70_74', 'NEF75_79', 'NEF80_84', 'NEF85_89', 'NEF90_94',
                'NEF95_GT', 'NEF85_GT', 'NEF65_69', 'NEM0_34', 'NEM35_44', 'NEM45_54', 'NEM55_59',
                'NEM60_64', 'NEM65', 'NEM66', 'NEM67', 'NEM68', 'NEM69', 'NEM70_74', 'NEM75_79',
                'NEM80_84', 'NEM85_89', 'NEM90_94', 'NEM95_GT', 'NEM85_GT', 'NEM65_69']


def HCCV21_list87():
    return ['HCC1', 'HCC2', 'HCC6', 'HCC8', 'HCC9', 'HCC10', 'HCC11', 'HCC12',
            'HCC17', 'HCC18', 'HCC19', 'HCC21', 'HCC22', 'HCC23', 'HCC27', 'HCC28',
            'HCC29', 'HCC33', 'HCC34', 'HCC35', 'HCC39', 'HCC40', 'HCC46', 'HCC47',
            'HCC48', 'HCC51', 'HCC52', 'HCC54', 'HCC55', 'HCC57', 'HCC58', 'HCC70',
            'HCC71', 'HCC72', 'HCC73', 'HCC74', 'HCC75', 'HCC76', 'HCC77', 'HCC78',
            'HCC79', 'HCC80', 'HCC82', 'HCC83', 'HCC84', 'HCC85', 'HCC86', 'HCC87',
            'HCC88', 'HCC96', 'HCC99', 'HCC100', 'HCC103', 'HCC104', 'HCC106', 'HCC107',
            'HCC108', 'HCC110', 'HCC111', 'HCC112', 'HCC114', 'HCC115', 'HCC122', 'HCC124',
            'HCC134', 'HCC135', 'HCC136', 'HCC137','HCC138', 'HCC139', 'HCC140', 'HCC141',
            'HCC157', 'HCC158', 'HCC159','HCC160', 'HCC161', 'HCC162', 'HCC166', 'HCC167',
            'HCC169', 'HCC170','HCC173', 'HCC176', 'HCC186', 'HCC188', 'HCC189']

##############################################################################

# New Enrollee dialysis model

def AGESEX_DIAL_NE():

    return ['NEF0_34', 'NEF35_44', 'NEF45_54', 'NEF55_59', 'NEF60_64', 'NEF65_69',
                'NEF70_74', 'NEF75_79', 'NEF80_84', 'NEF85_GT', 'NEM0_34', 'NEM35_44',
                'NEM45_54', 'NEM55_59', 'NEM60_64', 'NEM65_69', 'NEM70_74', 'NEM75_79',
                'NEM80_84', 'NEM85_GT']

def MOAS_DIAL_NE():
    # Interaction variables
    return ['NEMedicaid_Female_Aged', 'NEMedicaid_Female_NonAged', 'NEMedicaid_Male_Aged',
            'NEMedicaid_Male_NonAged', 'ORIGDIS_FEMALE_GE65', 'ORIGDIS_FEMALE_LT65',
            'ORIGDIS_MALE_GE65', 'ORIGDIS_MALE_LT65']

##############################################################################

# Community Functioning Graft model

def dic():
    # Disease Interactions for Functioning graft community model;
    return ['SEPSIS_CARD_RESP_FAIL', 'CANCER_IMMUNE', 'DIABETES_CHF', 'CHF_COPD', 'CHF_RENAL',
            'COPD_CARD_RESP_FAIL']

# Institutional Functioning Graft model

def ddi():
    # Disabled/Disease Interactions for institutional Functioning graft 
    # model
    return ['NONAGED_HCC85', 'NONAGED_PRESSURE_ULCER', 'NONAGED_HCC161', 'NONAGED_HCC39',
            'NONAGED_HCC77', 'NONAGED_HCC6']

def dii():
    # Disease Interactions for institutional functioning graft model
    return ['CHF_COPD', 'COPD_CARD_RESP_FAIL', 'SEPSIS_PRESSURE_ULCER', 'SEPSIS_ARTIF_OPENINGS',
            'ART_OPENINGS_PRESSURE_ULCER', 'DIABETES_CHF', 'COPD_ASP_SPEC_BACT_PNEUM',
            'ASP_SPEC_BACT_PNEUM_PRES_ULC', 'SEPSIS_ASP_SPEC_BACT_PNEUM', 'SCHIZOPHRENIA_COPD',
            'SCHIZOPHRENIA_CHF', 'SCHIZOPHRENIA_SEIZURES']

##############################################################################

# New Enrollee Functioning Graft model 

def NE_AGESEX():

    return ['NEF0_34', 'NEF35_44', 'NEF45_54', 'NEF55_59', 'NEF60_64', 'NEF65', 'NEF66',
            'NEF67', 'NEF68', 'NEF69', 'NEF70_74', 'NEF75_79', 'NEF80_84', 'NEF85_89',
            'NEF90_94', 'NEF95_GT', 'NEM0_34', 'NEM35_44', 'NEM45_54', 'NEM55_59', 'NEM60_64',
            'NEM65', 'NEM66', 'NEM67', 'NEM68', 'NEM69', 'NEM70_74', 'NEM75_79', 'NEM80_84',
            'NEM85_89', 'NEM90_94', 'NEM95_GT']

def DEMOG_INTERACT_GRAFT_NE():

    return ['MCAID_female0_64', 'MCAID_female65', 'MCAID_female66_69', 'MCAID_female70_74',
            'MCAID_female75_GT', 'MCAID_male0_64', 'MCAID_male65', 'MCAID_male66_69',
            'MCAID_male70_74', 'MCAID_male75_GT', 'Origdis_female65', 'Origdis_female66_69',
            'Origdis_female70_74', 'Origdis_female75_GT', 'Origdis_male65', 'Origdis_male66_69',
            'Origdis_male70_74', 'Origdis_male75_GT']


##############################################################################

def dialysis_regression():
    # Variables for Dialysis regression
    return [] + ageSEX_1() + moas_1()+ oe()+ HCCV21_list87()+ did()+ ddc()

def dialysis_new_enrollee_regression():
    # Variables for Dialysis New Enrollees regression
    return [] +AGESEX_DIAL_NE() + MOAS_DIAL_NE()

def functioning_graft_community_regression():
    # Variables for Functioning Graft Community regression
    return [] +ageSEX_1() +moas_1()+ HCCV21_list87()+ dic()+ ddc()

def functioning_graft_institutional_regression():
    # Variables for Functioning Graft Institutional regression
    return []+ ageSEX_1()+ HCCV21_list87()+ ddi() +dii() + ['MCAID' ,'ORIGDIS']

def functioning_graft_new_enrolle_regression():
    # Variables for Functioning Graft New Enrollee regression
    return []+ NE_AGESEX()+ DEMOG_INTERACT_GRAFT_NE()
