# Atributos de classe

class Pessoa:
    ano_atual = 2022 # atributo da classe


    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade 
        # se tiver "self.ano_atual = numero" támbem pode atrapalhar
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade  # o erro acima pode ser consertado se colocar 
             #"Pessoa.ano_atual"

"""
O atributo da classe vai estar disponível a todas as instâncias da classe, 
e será protegida por teu escopo, 
sem ser possível alterar seu valor por fora da mesma.
Mas é possível usar dentro do escopo com o "self.(atripudo_da_classe)" ou 
"Classe.atripudo_da_classe" além disto. 
Pode ser usada fora do escopo apenas se usar, 
Classe.atripudo_da_classe. 
Se utilizar, "Classe.atripudo_da_classe = (qualquer coisa)" 
o número/str será alterado, e o valor será alterado dentro do escopo, 
então irá mudar por completo este atributo. 
"""

p1 = Pessoa('João', 25)
p2 = Pessoa('Helena', 11)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
