salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

bag = 0

for k in range(1, months + 1):
    bag += spend
    spend *= increase + 1

bag -= salary * months

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(bag, 2))

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
