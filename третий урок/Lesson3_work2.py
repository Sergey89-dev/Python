def funk_User_data(name, name2, Year_of_birth, city, email, phone_number):
    print(f"Вас зовут {name}, ваша фамилия {name2}, вы родились {Year_of_birth} года, ваш город {city},ваш email {email}, ваш номер телефона {phone_number}")
    
a = input("Введите ваше имя")
b = input("Введите вашу фамилию")
Birt = input("Ваш год рождения")
d= input("Ваш город")
rt=input("введите email:")
phone = input("И ваш номер телефона:")
funk_User_data(city = d, email = rt, name = a, phone_number = phone, Year_of_birth = Birt, name2 = b)

input("Нажмите enter, чтобы выйти.")
