#Зажание 2
time = int(input("Введите время в секундах: "))

hours = time/3600
Minuts = hours * 60
sec= Minuts*60
print(  'ЧЧ: {0:.2f}; ММ: {1:.2f}; СС: {2:.2f}'.format(hours, Minuts, sec))
input("Нажмите enter, чтобы выйти")