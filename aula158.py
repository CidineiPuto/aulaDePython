# Funções decoradoras e decoradores com classes

# Composição_____________________________________________________________________________________

def meu_repr(self): # é para funcionar como se estivesse dentro de uma classe 
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

# Ou "Time = adiciona_repr(Time)"

@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

# Ou "Planeta = adiciona_repr(Planeta)"

brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

# Herança_____________________________________________________________________________________ 

# class MyReprMixin:
#     def __init__(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'
#         return class_repr

# class SuperTeam:
#     ...

# class Team(MyReprMixin):
#     def __init__(self, nome):
#         self.nome = nome



# class Planet(MyReprMixin):
#     def __init__(self, nome):
#         self.nome = nome
