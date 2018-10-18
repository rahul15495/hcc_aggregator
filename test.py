import handler

def main():
    out=handler.get_scores('1906072835999','F', '1948-03-16', '2018-02-01','CNA' ,codes= ['E119', 'E119', 'E119', 'E119', 'E119', 'E119', 'E119'])

    print(out)

    

if __name__ == '__main__':
    main()
