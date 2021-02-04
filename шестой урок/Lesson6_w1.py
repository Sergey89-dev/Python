#Задание 1
import time 
class TrafficLight:
    __color_r = 'Красный'
    __color_e = 'Желтый'
    __color_g = 'Зеленый'
    def __init__(self):
        print("Запуск\n")
      
a = TrafficLight()
print(a._TrafficLight__color_r)
time.sleep(7)
print(a._TrafficLight__color_e)
time.sleep(3)
print(a._TrafficLight__color_g)
time.sleep(4)
