import handler


def main():
    out = handler.get_scores(hicno='1906072835999',
                                sex= 'M',
                                dob= '1956-03-16',
                                year_of_eligibility= '2018',
                                RAF_type= 'CNA',
                                orec= 1,
                                medicaid= True,
                                codes=['I209', 'I70203', 'E119', 'E119', 'E119', 'E119', 'E119']
                                )

    print(out)

    # output
    # [{'cna_f65_69': 0.312}, {'cna_hcc19': 0.10400000000000001}, {'cna_originallydisabled_female': 0.244}]


if __name__ == '__main__':
    main()
