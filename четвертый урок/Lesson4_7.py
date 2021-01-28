#Задание 7
from itertools import count
from math import factorial

def My_fact():
    for i in count(1):
        yield factorial(i)
oper = My_fact()
user_fact = int(input("Введите число, факториал которого нужно найти:"))
a = 0
for i in  oper:
    if a < user_fact:
        print(i)
        a+=1
    else:
        break
        
input("Нажмите enter, чтобы выйти")
        
