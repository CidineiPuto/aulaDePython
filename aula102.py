# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes

# import sys

# platform = 'A MINHA'
# print(sys.platform) # O módulo está protegido pelo namespace, então só irá chamar o platform de lá;


# print(platform)

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo

# from sys import exit, platform
# Esses nomes NÃO estão defendidos pelo namespace, então variáveis com o mesmo nome
# Irá sobscrever o código importado

# print(platform)

# alias 1 - import nome_modulo as apelido # Os módulos importados caso tenha o nome de uma mesma
# Variável, podem ser sobscritos
# import sys as s # Agora o sys, irá ter o apelido de "s"

# sys = 'alguma coisa'
# print(s.platform) # é como se fosse o mesmo sys
# print(sys)


# alias 2 - from nome_modulo import objeto as apelido
# from sys import exit as ex
# from sys import platform as pf # importa e muda o nome deles

# print(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo

# from sys import *  # Tudo é importado, sem namespace.

# print(platform)
# exit()