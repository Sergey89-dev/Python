# Задание 6
from itertools import cycle, count
ending = int(input("Введите конечное число:"))
for i in count(1):
    if i> ending:
        break
    else:
        print(i)
a =0
Just_list = ['кошка', 545, None, 'микросхема', 12]
for i in cycle(Just_list):
    if a>ending:
        break
    print(i)
    a+=1
    
input("Нажмите enter, чтобы выйти")