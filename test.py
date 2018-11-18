import handler


def main():
    out = handler.get_scores(hicno='1906072835999',
                                sex= 'F',
                                dob= '1948-03-16',
                                year_of_eligibility= '2018',
                                RAF_type= 'CNA',
                                orec= 1,
                                codes=['E119', 'E119', 'E119', 'E119', 'E119', 'E119', 'E119']
                                )

    print(out)

    # output

    # [{'valid_community_aged_variables': ['F65_69', 'HCC19']},
    #  {'valid_community_disabled_variables': ['HCC19']},
    #  {'valid_community_aged_variables': ['F65_69', 'HCC19']},
    #  {'valid_community_disabled_variables': ['HCC19']},
    #  {'valid_community_aged_variables': ['F65_69', 'HCC19']},
    #  {'valid_community_disabled_variables': ['HCC19']}]


if __name__ == '__main__':
    main()
