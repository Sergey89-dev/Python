#Задание 1
def position_funk(a, b):
    if b==0:
        return "На 0 делить нельзя!"
    return a/b
number1 = int(input("Введите делимое:"))
number2 = int(input("Введите делитель:"))

print( position_funk(number1, number2))
input("Нажмите enter, чтобы выйти")