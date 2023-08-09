# parte 1 ________________________________________________________________________________________________


# from sys import path


# from aula105_package.modulo import soma_do_modulo

# print(soma_do_modulo(2,6))

# import aula105_package.modulo

# print(aula105_package.modulo.soma_do_modulo(1,2))

# from aula105_package.modulo import modulo 

# print(modulo.soma_do_moduloo(1,2))

# from aula105_package.modulo import *

# print(variavel)
# print nova variavel # isso não iria funcionar pois o __all__ não deixou essa variavel ser importada

# print(*path, sep='\r\n')

# parte 2 ________________________________________________________________________________________________

# from aula105_package.modulo import  fala_oi, soma_do_modulo # fala_oi # Quando importa algo para um modulo támbem fica disponível
# # no outro



# fala_oi()

# Parte 3 ___________________________________________________________________________________

# Tudo importado do init poderá ser usado aqui

# import aula105_package

from aula105_package import soma_do_modulo, fala_oi


print(soma_do_modulo(2,3))
fala_oi()
