# Herança simples - Relações entre classes
# Associação - Objeto usa o outro, Agregação - Objeto tem outro objeto
# Composição - Objeto é dono de um objeto, Herança - Um objeto é outro objeto
#
# Herança vs Composição
#
# Classe principal (Pessoa) # Classe generica # Vai ser extendida por outras classes
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

#__________ CLiente extende pessoa, por herança. Cliente, "herda" de pessoa.

# Herança > Uma classe, extende outra classe.

# Cliente é do tipo cliente, e é do tipo pessoa, pois cliente pela herança, é uma pessoa.


"""
Fazer herança é para  deixar uma classe que seria muito específica mais gênerica, e a gente 
poder utilizar essa classe para outras classes.
"""

# Classes sempre herdam de uma classe "ínvisivel" com o nome de "object"
"""
Como podemos ver aqui

Class foo(object)
    ...

"""

class Pessoa:
    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('Classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('EITA, nem saí da classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)

    

# Todo código que está dentro de pessoa, irá automaticamente para "cliente" 

class Aluno(Pessoa):
    cpf = 'cpf aluno'
    ...

c1 = Cliente('Luiz', 'Otávio')
c1.falar_nome_classe()
a1 = Aluno('Maria', 'Helena')
a1.falar_nome_classe()
print(a1.cpf)
# help(Cliente)