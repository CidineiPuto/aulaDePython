#____________________________________________________________________________________

# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

# try:
#     import sys
#     sys.path.append('/home')
# except ModuleNotFoundError:
#     ...
# import aula103_m

# print('Este módulo se chama', __name__)
# print(*sys.path, sep='\r\n')

#____________________________________________________________________________________

import aula103_m
from aula103_m import soma, variavel_modulo

# print('Este módulo se chama', __name__)
print(aula103_m.variavel_modulo)
print(variavel_modulo)
print(aula103_m.soma(1,5))
print(soma(1,12))