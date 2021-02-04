#Задание 1
def My_work():
   jobtime = int(input("Введите введите выработку в часах:"))
   bid = int(input("Введите ставку в час:"))
   prize= int(input("Введите вашу премию:"))
   Money = (jobtime* bid ) + prize
   print(f"Ваша зарплата:{Money} ")

My_work()
input("Нажмите enter, чтобы выйти")
