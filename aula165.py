# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value
import enum

# Direcoes = enum.Enum('Direcoes',['ESQUERDA','DIREITA']) # está em maiúsculo pois
# é uma constante e constantes são feitas para não ser alteradas

class Direcoes(enum.Enum):
                           # os valores sempre podem ser escolhidos pelo dev
    ESQUERDA = enum.auto() # mesma coisa que "1"
    DIREITA = enum.auto() # mesma coisa que "2"
    CIMA = enum.auto() # mesma coisa que "3"
    BAIXO = enum.auto() # mesma coisa que "4"


print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)
print(Direcoes(1).name, Direcoes.ESQUERDA.value)

def mover(direcao: Direcoes): # informa que direcao é do tipo "Direcoes"
                            # Pois enum é um tipo.
    

    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')

    print(f'Movendo para {direcao.name} ({direcao.value})')

mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.CIMA)
mover(Direcoes.BAIXO)
# mover('lado')

