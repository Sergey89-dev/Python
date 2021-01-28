#Задание4
Just_list = [10, 105, 11, 10, 87, 105, 60, 11, 28, 10, 87]

new_list = [i for i in Just_list if Just_list.count(i) ==1 ]
print(new_list)
input("Нажмите enter, чтобы выйти")