#Задание 4
n=[] 
u=1

User = input("Введите слова через пробел:")
for i in range(User.count('')+1):
    n= User.split()
    if len(str(n))<=10:
        print(f'{u} {n [i]}')
        u+=1
    else:
        print(f'{u} {n[i][0:10]}' )
        u+=1

