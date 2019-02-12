import handler as handler

def single_month_score_predcitor(**kwargs):

    out = handler.get_scores(**kwargs)

    return out


def aggregate_score_predcitor(**kwargs):
    print(kwargs)
    
    return 0