#Задание 5
My_rating = [7, 4, 3, 3, 2]
print(My_rating)
user_answer = int(input("Введите числовой элемент:"))
max_value = max(My_rating)
if user_answer>max_value:
    My_rating.insert(0,user_answer)
elif user_answer in My_rating:
    My_rating.insert(My_rating.index(user_answer), user_answer)
else: 
    My_rating.append(user_answer)
print(My_rating)
input("Нажмите enter, чтобы выйти")