# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase(começa com letra maiúscula) para nomes de
# classes.
# Ex de pascal case : "CriarBaseDeDados"

# string = 'Luiz'  # é uma instância de string
# print(string.upper()) # .upper() é um método exclusivo de uma str  
# print(isinstance(string, str))  # string = 'luiz' é um objeto(instância) da classe "string"                                                                                                                                                                                                                                                                                                                                                                               
# 'luiz' é um atributo

class Pessoa:
    def __init__(self, nome, sobrenome): 
        self.nome = nome # atributo chamado nome
        self.sobrenome = sobrenome


# quando a função está dentro da classe, é chamada de método
# self reserva o objeto do primeiro param, a instância, como por exemplo o "p1"

p1 = Pessoa('Luiz','Otávio') # inicia um objeto
# p1.nome = 'Luiz' # Isto é um atributo
# p1.sobrenome = 'Otávio'

p2 = Pessoa('Maria','Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)