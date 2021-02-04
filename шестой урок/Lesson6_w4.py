#Задание 4
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.speed = speed

    def go(self):
        print(f"Автомобиль {self.name} начал движение")

    def stop(self):
        print(f"Автомобиль {self.name} остановился")

    def turn_legt(self):
        print(f"Автомобиль {self.name} повернул налево")
    def turn_right(self):
        print(f"Автомобиль {self.name} повернул направо")
    def show_speed(self):
        print(f"Скорость автомобиля {self.name} - {self.speed}")

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f"Скорость автомобиля {self.name} - {self.speed}")

        if self.speed > 60:
            print(f"Осторожно скорость автомобиля {self.name} превышена")
        else:
            print(f"Скорость автомобиля {self.name} допустимая")

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f"Скорость автомобиля {self.name} - {self.speed}")
        if self.speed > 60:
            print( f"Осторожно скорость автомобиля {self.name} превышена")
        else:
            print(f"Скорость автомобиля {self.name} допустимая")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    
auto_1 = TownCar(120, 'red', 'bumer', False)
auto_2 = SportCar(100, 'green', 'lada', True)
auto_3 = WorkCar(40, 'black', 'renault', False)
auto_4 = PoliceCar(90, 'white', 'ford', True )

auto_3.go()
auto_3.turn_legt()
auto_3.stop()

auto_1.go()
auto_1.show_speed()
print(f"Этот автомобиль марки {auto_1.name}")
auto_4.show_speed()
auto_4.turn_right()

print(f"Цвет автомобиля {auto_4.name}-{auto_4.color}")