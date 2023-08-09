# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe


class A(object):
    def __new__(cls, *args, **kwargs): # new cria o objeto ( new cria o self )
        print('Antes de criar o fanfas')
        instance = object.__new__(cls) # cria o new
        print('Depois do fanfas')
        instance.x = 213
        return  instance

    def __init__(self, x):
        self.x = x 
        print('Sou o bungas')
    
    def __repr__(self):
        return f'A()'
    

a = A('D')
# a = object.__new__(A) # cria o new
# a.__init__()
print(a.x)