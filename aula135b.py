# from aula135 import  ARCHIVE_PATH
# import json

# peoples = []

# with open(ARCHIVE_PATH, 'r', encoding='utf8') as archive:
#     peoples = json.load(archive)
#     print(peoples)

import json

from aula135 import CAMINHO_ARQUIVO, Pessoa, fazer_dump 

# fazer_dump() 
# Por conta da importação o  dump seria executado, mas já que está envolto em uma função
# e ele só sera executado se o arquivo for o main, e o main, será o que foi importado.


with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)

