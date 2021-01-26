#3 Задание
def Max_Funk(a, b, i):
    two_list = [a,b,i]
    print(f"Вы ввели 3 значения:{two_list}")
    my_list =[]
    just=max(two_list)
    my_list.append(just)
    two_list.remove(just)
    just2 = max(two_list)
    my_list.append(just2)
    print(f"Выберем 2 наибольших:{my_list}")
    user = sum(my_list)
    return user

g = int(input("Введите первое значение:"))
p = int(input("Введите второе значение:"))
b = int(input("Введите третье значение:"))
test = Max_Funk(g, p, b)
print("И получим их сумму:",test)
input("Нажмите enter, чтобы выйти.")