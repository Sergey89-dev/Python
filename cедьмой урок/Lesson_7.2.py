
class Clothes:
    def __init__(self, volume, hight):
        self.v = volume
        self.h = hight
    
    def my_coat(self):
        return self.v / 6.5 + 0.5 
 

    def my_costume(self):
        return self.h*2 + 0.3 

    @property
    def total_area(self):
        return str(f"Общая площадь ткани:"  
        f"{ (self.v / 6.5 + 0.5) + ( self.h * 2 + 0.3 )}")
    
 
class Blazer(Clothes):
    def __init__(self, volume, height):
        super().__init__(volume, height)
        self.costume = round(self.h * 2 + 0.3)
    def __str__(self):
        return f"Площадь на пиджак {self.costume}"


class Slicker(Clothes):
    def __init__(self, volume, height):
        super().__init__(volume, height)
        self.coat = round(self.v / 6.5 + 0.5)
    def __str__(self):
        return f"Площадь на плащ {self.coat}"


blaz = Blazer(3,7)
slick = Slicker(8,5)
print(slick)
print(blaz)
print(slick.total_area)
print(blaz.total_area)
