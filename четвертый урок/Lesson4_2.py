#Задание 2
just_list = [57, 2, 44, 10, 190, 25] 
new_list = [el for numbers, el in enumerate(just_list) if just_list[numbers - 1] < just_list[numbers]]
print(f"Исходный список:{just_list}")
print(f"Новый список{new_list}")
input("Нажмите enter, чтобы выйти")