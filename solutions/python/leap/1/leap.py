def leap_year(year):
    # multiple_4 = year % 4 == 0
    # multiple_400 = year % 400 == 0
    # multiple_100 = year % 100 == 0
    # return multiple_4 and not multiple_100 or multiple_400
    return year % 400 == 0 or year % 4 == 0 and not year % 100 == 0

test_years = [
    1500, 1600, 1700, 1800, 1900, 2000, # Centenários (F, V, F, F, F, V)
    1996, 1997, 1998, 1999, 2001, 2002, # Sequência próxima ao 2000
    2020, 2021, 2022, 2023, 2024, 2025, # Anos atuais
    2100, 2200, 2300, 2400, 2500, 2600, # Futuros centenários
    2012, 2014, 2016, 2018, 1000, 4000  # Diversos
]

for i, y in enumerate(test_years):
    print(f'{i+1:02d}. Ano {y}: {leap_year(y)}')
