# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

#________________________________________________________________________________________
# Criando caminho
# caminho_arquivo = 'C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\Novo arquivo Atenção\\'
# caso precise coloque "r" antes do arquivo
# r'C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\Novo arquivo Atenção\\'
# caminho_arquivo += 'aula122.txt'
# ^ Caminho completo do arquivo

# O arquivo NÃO está no caminho do projeto, pois no caminho_arquivo alteramos ele.
# Caso não tivesse alterado, o caminho ficaria dentro deste arquivo.

# arquivo = open(caminho_arquivo, 'w')
# # faz coisa no arquivo 
# arquivo.close()
#________________________________________________________________________________________
# Criando arquivo

# with open(caminho_arquivo, 'w') as arquivo:
#     ...

"""
Sempre feche o arquivo em python quando o abrir. Pode ser usado o :

with open(caminho_arquivo, 'w') as arquivo:
    ###comando###

assim ele já irá fechar após o comando ser passado
"""
#________________________________________________________________________________________
# write

caminho_arquivo = 'C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\Novo arquivo Atenção\\'
caminho_arquivo += 'aula122.txt'

# with open(caminho_arquivo, 'w') as arquivo:
#    arquivo.write('Hello world 1\n')
#    arquivo.write('Hello world 2\n')

# Não pode usar write e read ao mesmo tempo, no mesmo código.


# read

# with open(caminho_arquivo, 'r') as arquivo:
#    print(arquivo.read())
# mas se usar ('w+') é possível ler e escrever

# seek
# writelines
# readline

# with open(caminho_arquivo, 'w+') as arquivo:
#    arquivo.write('Hello world 1\n')
#    arquivo.write('Hello world 2\n')
#    arquivo.writelines(
#       ('Hello world 3\n', 'Hello world 4\n') # pode escrever mais de uma coisa
#    )            # Pode ser usado quando está com um iterável cheio de coisas
#    arquivo.seek(0, 0) # move o cursor
#    print(arquivo.read()) # lê o cursor movendo ele pra baixo do arquivo
#    print('Lendo')
#    arquivo.seek(0, 0)
#    print(arquivo.readline(), end='') # Tira os espaços do  fim
#    print(arquivo.readline().strip()) # Tira os espaços do começo e do fim
#    print(arquivo.readline().strip())
#    arquivo.seek(0, 0)
#    print('READLINES')
#    for linha in arquivo.readlines():
#      print(linha.strip())



# print(15*'#')


# with open(caminho_arquivo, 'r') as arquivo:
#    print(arquivo.read())


#______________________________________________________________________________________
# Diferença  do W e do A

# with open(caminho_arquivo, 'a+') as arquivo:
#    arquivo.write('Hello world 1\n')
#    arquivo.write('Hello world 2\n')
#    arquivo.writelines(('Hello world 3\n', 'Hello world 4\n')) 




"""
O w apaga o arquivo e reescreve ele, enquanto o a pega o arquivo e escreve apenas no final.
Por isso, é conhecido como append mode.
"""


# with open(caminho_arquivo, 'w', encoding='utf8') as arquivo: 
#    arquivo.write('Atenção\n')
#    arquivo.write('Hello world 1\n')
#    arquivo.write('Hello world 2\n')
#    arquivo.writelines(('Hello world 3\n', 'Hello world 4\n')) 

# enconding='utf8' permite escrever arquivos com acentos, sem dar erro.

#___________________________________________________________________________

# Modulo os

import os

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo: 
   arquivo.write('Atenção\n')
   arquivo.write('Hello world 1\n')
   arquivo.write('Hello world 2\n')
   arquivo.writelines(('Hello world 3\n', 'Hello world 4\n')) 


# os.unlink(caminho_arquivo) # ou os.remove(caminho_arquivo)
# apaga o arquivo.

# os.rename(caminho_arquivo, 'aula122-2.txt')
# Troca o  nome do arquivo, além de poder mover ele támbem.