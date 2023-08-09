# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('João',35)

print(p1.__dict__)
# ou
print(vars(p1))
# támbem através disto é possível adicionar novos valores no dicionário dentro do atributo
# por mais que não é comum.
#  p1.__dict__['outra'] = 'coisa'

# ou pode alterar até mesmo o atributo que está lá 
# p1.__dict__['nome'] = 'EITA'