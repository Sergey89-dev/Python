class Universal:
    def __init__(self, *numbs):
        self.just_list = []


    def use(self):

        while True:
            try:
                ab = int(input("Введите значеие:"))
                self.just_list.append(ab)
                print(f"Список на данный момент {self.just_list}")
            except:
                print("Не правильное значение.")
                close = input("Нажмите s, чтобы выйти или t , чтобы продолжить")

                if close == 't' or close == 'T':
                    print(first_use.use)
                elif close =='s' or close == 'S':
                    return f"Выход..."
    
first_use = Universal(1)
print(first_use.use())