print(
    'Você importou ',__name__
)

# É como se init fosse um módulo

print(
    'Você importou', __name__   
)

# def dobra(x):
#     return x * 2

# from .modulo import nova_variavel, soma_do_modulo, variavel

# a * é uma má pratica se for usado em certas ocasiões mas se for usado neste caso =

from aula105_package.modulo import * 
# e
from aula105_package.modulo_b import *


# A pratica se torna boa 