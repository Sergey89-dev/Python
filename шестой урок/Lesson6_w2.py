#Задание 2
class Road:
 
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
        
    def mass(self):
        return self._length * self._width

class Mass_Road(Road):
    def __init__(self, _length, _width, depth):
        super().__init__(_length, _width)
        self.depth = depth

     


user = Mass_Road(20, 300, 25)
user = print(user.mass())