#Задание 5
from functools import reduce

def My_funk(el_1,  el_2):
    return el_1 * el_2

 
print(f"Исходный список{[el for el in range(100, 1001) if el % 2==0]}")
print(f"Итоговое число:{reduce(My_funk, [el for el in range(100, 1001) if el % 2==0])}")
input("Нажмите enter, чтобы выйти.")