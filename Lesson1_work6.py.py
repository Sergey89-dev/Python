#Задание 6
distance= int(input("Введите конечное значение дистанции в км: "))
first_result = int(input("Введите начальное значение дистанции  в км:"))
day=1
print(day, "день:", first_result, "км" )
while first_result<distance:
    first_result= (first_result/10) + first_result
    day +=1
    print( day, "день:","%.2f"% first_result, "км")
print("Ответ: на ",day, "день спортсмен достиг результата- не менее", distance, "км")
input("Нажмите enter, чтобы выйти")

