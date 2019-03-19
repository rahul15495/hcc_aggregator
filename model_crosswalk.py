from query_collections import exceptions
from query_collections.query_structs import query_list, query_dict, Stream, Optional
from query_collections.search import query
from query_collections import filters
import traceback

coeff_path= lambda x : "coefficients/{}.csv".format(x)

model_override= {'2018' :['v22', 'v21']}

model_crosswalk= query_dict({'model_crosswalk':[

    {'payment_year' :'2020' , 'year_of_eligibility':'2019' , 'dx_time_period': '2018' , 'lookup': 
        [
            {
                'raf_types': ['CFA','CNA','CPA','CFD','CND','CPD','INS','NE','SNPNE'],
                'models': [('v23', 0.25, 'v23_2019'), ('v22', 0.75, 'v22_2019')],
                'lob': ['MA', 'ACO']
            },
            {
                'raf_types': ['DI','DNE','GC','GI','GNE','TRANSPLANT','GE65','LT65'],
                'models': [('esrd', 1, 'esrd_2019')],
                'lob': ['MA', 'ACO']
            },
            {
                'raf_types':['CE','INS','NE'],
                'models': [('v21', 1, 'v21_2019')],
                'lob': ['PACE']
            }
        ]
    },
    {'payment_year' :'2019' , 'year_of_eligibility':'2018' , 'dx_time_period': '2018' , 'lookup': 
        [
            {
                'raf_types': ['CFA','CNA','CPA','CFD','CND','CPD','INS','NE','SNPNE'],
                'models': [('v22', 1, 'v22_2018')],
                'lob': ['MA', 'ACO']
            },
            {
                'raf_types': ['DI','DNE','GC','GI','GNE','TRANSPLANT','GE65','LT65'],
                'models': [('esrd', 1, 'esrd_2018')],
                'lob': ['MA', 'ACO']
            },
            {
                'raf_types':['CE','INS','NE'],
                'models': [('v21', 1, 'v21_2018')],
                'lob': ['PACE']
            }
        ]
    }
    
]})



select_year=lambda x: model_crosswalk.query('model_crosswalk:*:year_of_eligibility$',filters.eq(x))


def select_model(year,raf_type, lob): ##### arguments year--> '2019', raf_type --> 'CFA'

    temp_df= select_year(year)

    _payment_year= temp_df[0]['payment_year']

    selected_element = None

    for sub_list,lob_list in zip(temp_df.query('*:lookup:*:raf_types')[0], temp_df.query('*:lookup:*:lob')[0]) :

        if( raf_type in sub_list) and (lob in lob_list) :

            selected_element= sub_list

    models= temp_df.query('*:lookup:*:raf_types$', filters.eq(selected_element))[0][0]['models']

    out= []

    for model in models:

        model= list(model)

        model.append(coeff_path(model[2]))

        if model[0] in list(model_override.values())[0] :

            model[2]= "{}_{}".format(model[0],list(model_override.keys()).pop())

        model.append(_payment_year)

        out.append(model)

    ####################################################
    ################### sample output ##################

    # [['v22', 0.75, 'v22_2018', 'coeffcients/v22_2019.csv'],
    # ['v23', 0.25, 'v23_2019', 'coeffcients/v23_2019.csv']]

    # format--> [model, weightage, <model file>, <coeffcient path>]

    ####################################################

    return out


