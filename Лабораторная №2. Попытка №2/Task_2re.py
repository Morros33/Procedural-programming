money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов





month = 0

while True:
    monthly_trade = spend - salary
    money_capital += monthly_trade
    spend *= 1 * increase
    month += 1
    if money_capital < 0:
        break
print("Количество месяцев, которое можно протянуть без долгов:", month)