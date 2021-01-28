# Задание 2
n = list(map(str, input('Введите значения через пробел:').split()))
k=0
for i in range(int(len(n)/2)):
    n[k], n[k+1] =n[k+1], n[k]
    k+=2
print(n)
input("Нажмите enter, чтобы выйти")
