# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código
# exemplo : self.nome = 'Fusca' 

class Carro:
    def __init__(self,nome): # Método init sempre retorna None
        self.nome = nome
    def acelerar(self): # o primeiro param deve ser self
        print(f'{self.nome} faz  ZUUUUUN e acelera')

fusca = Carro('fusca')
print(fusca.nome)
# fusca.acelerar()
Carro.acelerar(fusca)

celta = Carro(nome='celta')
print(celta.nome)
# celta.acelerar()
Carro.acelerar(celta)

 
"""
o "self" pode ser qualquer coisa, dês de self, ou blabla o importante é ele ser o primeiro 
param, pois ele irá representar o objeto.
Entendendo self em classes Python
Classe - Molde (geralmente sem dados)
Instância da class (objeto) - Tem os dados
Uma classe pode gerar várias instâncias.
Na classe o self é a própria instância.
"""