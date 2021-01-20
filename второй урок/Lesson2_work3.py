seasons = ['зима', 'весна', 'лето', 'осень']

variant = int(input("Введите месяц от 1 до 12:"))
if variant == 1 or variant ==2 or variant == 12:
    print(seasons[0])
elif variant == 3 or variant == 4 or variant == 5:
    print(seasons[1])
elif variant == 6 or variant == 7 or variant == 8:
    print(seasons[2])
elif variant == 9 or variant ==10 or variant == 11:
    print(seasons[3])
else:
    print("Сказано же , от 1 до 12 : )")

seasons_2 ={1:'Зима', 2:'Весна', 3:'Лето', 4:'Осень'}
User = int(input("Введите номер месяца:"))
if User == 1 or User ==2 or User == 12:
    print(seasons_2.get(1))
elif User == 3 or User == 4 or User == 5:
    print(seasons_2.get(2))
elif User == 6 or User == 7 or User == 8:
    print(seasons_2.get(3))
elif User == 9 or User ==10 or User == 11:
    print(seasons_2.get(4))
else:
    print("Такого значения нет.")

input("Нажмите enter, чтобы выйти")