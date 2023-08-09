# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str


class Ponto:
    def __init__(self, x, y, z='string'):
        self.x = x  
        self.y = y
        self.z = z

    def __str__(self): # usado para mostrar uma str do objeto.
        return f'({self.x, self.y})' # chama representação do str 

    def __repr__(self): # normalmente para desenvolverdores mostrar como é montado.
        class_name = type(self).__name__
        # class_name = self.__class__.__name__
        return f'{class_name}(x= {self.x!r}, y={self.y!r}, z={self.z!r})'
        # querendo saber partes de desenvolvimento daquele objeto

p1 = Ponto(13914, 82742)
p2 = Ponto(12451, 98412)


print(p1) # string
print(repr(p2)) # repr
print(f'{p2!r}')  # repr
print(f'{p2!s}') # string