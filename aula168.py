from dataclasses import dataclass


# Não pode alterar o método
@dataclass(frozen=True)  # order = True
class Pessoa:
    nome: str
    sobrenome: str


"""
Frozen é boa prática de programação, " sempre é melhor criar uma nova variável
do alterar uma existente "
"""

if __name__ == '__main__':
    # p1 = Pessoa('Bungas', 'Fanfas')
    # p1.nome = 'Maria' # Daria erro, por conta do Frozen.
    # print(p1)

    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    # ordenadas = sorted(lista, reverse=True)  # se order não for True, o
    # "ordenadas" não irá funcionar.
    # Para ele funcionar sem isto, é necessário
    # ordenadas = sorted(lista, reverse=False, key=lambda p: p.nome)
    # ou
    ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
    print(ordenadas)
