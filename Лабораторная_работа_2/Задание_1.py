money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month = 1
rest = money_capital + salary - spend

while rest >= 0:
    spend *= (increase + 1)
    rest += salary - spend
    if rest < 0:
        break
    else:
        month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов