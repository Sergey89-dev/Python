#Задание 5
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f"Запуск отрисовки {self.title}"

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f"Используется {self.title}, отрисовка выполнена чернилами"

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f"Используется {self.title}, отрисовку можно стереть ластиком"

class Handle(Stationery):
     def __init__(self, title):
        super().__init__(title)
     def draw(self):
        return f"Используется {self.title}, а вот теперь листочек можно выкинуть, отрисовка не сотрется"

a = Pen('Ручка')
b = Pencil('Карандаш')
c = Handle('Маркер')
print(a.draw())
print(b.draw())
print(c.draw())

