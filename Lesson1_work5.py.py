#Задание 5
Revenue = int(input("Введите значение выручки: "))
Costs = int(input("Введите значение издержек: "))

if Revenue>Costs:
    print("Вы находитесь в позиции прибыли.")
    profit = Revenue - Costs
    profitability = profit/ Revenue* 100
    profitability = int(profitability)
    print("Рентабельность выручки:", profitability, "%")
    quanity = int(input("Введите количество сотрудников:"))
    profit_quanity = profit/quanity
    profit_quanity = int(profit_quanity)
    print("Прибыль фирмы в расчете на одного сотрудника:", profit_quanity)
else:
    print("У вас убыток.")
input("Нажмите enter, чтобы выйти")