money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month = 0  # Количество месяцев

while True:
    money_capital += salary     # Добавление зарплаты к подушке
    money_capital -= spend      # Вычитание ежемесячных расходов из подушки

    if money_capital < 0:
        break                   # Прерывание цикла если подушка опустошилась

    spend += spend * increase   # Увеличение ежемесяных трат за счёт роста цен
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
