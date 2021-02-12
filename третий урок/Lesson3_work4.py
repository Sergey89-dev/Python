#Задание 4
def My_funk(x, y):
    construstion = x**-y
    return construstion

def My_funk2(x, y):
  i=0
  a =1
  if y ==0:
    return a
  while i != y:
    i+=1
    a*=x
  b =1/a
  return b
    

user = int(input("Введите число:"))
user2 = int(input("Введите степень числа:"))
 
print( My_funk2(user, user2))
print(My_funk(user, user2))

input("Нажмите enter, чтобы выйти.")