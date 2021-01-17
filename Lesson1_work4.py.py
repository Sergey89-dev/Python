A = int(input("введите целое число:"))
b = -1
while A> 10:
    c = A % 10
    A = A//10
    if c > b:
        b = c
print("Самая большая цифра в числе:", b)
input("Нажмите enter, чтобы выйти")