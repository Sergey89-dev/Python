class Complex:
    def __init__(self, a, b, *numbs):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма a1 и a2 равна')
        return f'a = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение a1 и b1 равно')
        return f'a = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'a = {self.a} + {self.b} * i'


t_1 = Complex(5, -10)
t_2 = Complex(48, 78)
print(t_1)
print(t_1 + t_2)
print(t_1 * t_2)