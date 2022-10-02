def date(day, month, age):
    calc_month = month % 2
    month_2 = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    month_correct = month <= 12
    is_leap_year = (age % 4 == 0 and age % 100 != 0) or age % 400 == 0

    if month == 2:
        if is_leap_year:
            if day <= 29:
                print(f'{day} {month_2[month - 1]} {age}')
                exit()
        else:
            if day <= 28:
                print(f'{day} {month_2[month - 1]} {age}')
                exit()
    elif calc_month == 0 and month != 2 and month_correct and month <= 7:
        if day <= 30:
            print(f'{day} {month_2[month - 1]} {age}')
            exit()
    elif calc_month == 1 and month != 2 and month_correct and month <= 7:
        if day <= 31:
            print(f'{day} {month_2[month - 1]} {age}')
            exit()
    elif calc_month == 0 and month != 2 and month_correct and month >= 8:
        if day <= 31:
            print(f'{day} {month_2[month - 1]} {age}')
            exit()
    elif calc_month == 1 and month != 2 and month_correct and month >= 8:
        if day <= 30:
            print(f'{day} {month_2[month - 1]} {age}')
            exit()
    else:
        print('Data inválida.')


number_day = input('Digite o dia: ')
number_month = input('Digite o número do mês: ')
number_age = input('Digite o ano: ')

if number_day.isnumeric() and number_month.isnumeric() and number_age.isnumeric():
    number_day = int(number_day)
    number_month = int(number_month)
    number_age = int(number_age)
    date(number_day, number_month, number_age)
else:
    print('Ops! algo esta errado.')
