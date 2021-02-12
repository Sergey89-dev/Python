class Organic:
    def __init__(self, amount):
        self.amount = int(amount)

    def __add__(self, two):
        return Organic(self.amount + two.amount)

    def __sub__(self, two):
        return self.amount - two.amount if (self.amount - two.amount) > 0 else  print('Ошибка') 
    
    def __mul__(self, two):
        return Organic(int(self.amount * two.amount))
    
    def __truediv__(self, two):
        return Organic(round(self.amount // two.amount))

    def make_order(self, my_numb):
        numb = ""
        for i in range(int(self.amount / my_numb)):
            numb += f'{"*" * my_numb} \n'
        numb += f'{"*" * (self.amount % my_numb)}'
        return numb
    

cell_1 = Organic(24)
cell_2 = Organic(5)

print(cell_1 + cell_2)

print(cell_1 - cell_2)

print(cell_1 / cell_2)

print(cell_1.make_order(6))

print(cell_2.make_order(14))





