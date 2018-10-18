import handler


def main():
    out = handler.get_scores('1906072835999', 'F', '1948-03-16', '2018-02-01',
                             'CNA', codes=['E119', 'E119', 'E119', 'E119', 'E119', 'E119', 'E119'])

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
