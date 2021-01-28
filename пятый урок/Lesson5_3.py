#задание 3
from statistics import mean
statist = []

with open('worker.txt', 'r') as finger:
    for i in finger:
        last_name, money = i.split()
        money = int(money)
        if money<20000:
            print(last_name)
            statist.append(money)
print(round(mean(statist)))


