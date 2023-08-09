# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears

# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

#listar = mostar lista de tarefas
#desfazer = desfazer a ultima operação
#refazer = refaz o que se desfez

#_______________________________________________________________________



# Minha solução


# principal_list = []
# deleted_letters = []
# def refazer(list):
#        return list.append(deleted_letters[-1])
# def desfazer(list):
#         deleted_letters.append(list[-1])
#         return list.pop()
# def listing(list):
#     return list
# import os
# while True:
#     try:    
#         print('Comandos : listar, desfazer, refazer.')
#         command_or_list  = input('Escreva uma tarefa ou comando: ')
#         print()
#         if command_or_list ==  '':
#             print('Digite alguma coisa')
#             continue
#         if command_or_list == 'clear':
#             os.system('cls')
#             continue
#         elif command_or_list == 'listar':
#             if principal_list == []:
#                 print('nada para listar')
#                 print()
#                 continue
#             for item in principal_list:
#                 print(item)
#                 continue
#             print()
#         elif command_or_list == 'refazer':
#             refazer(principal_list)
#             del deleted_letters[-1]
#             continue
#         elif command_or_list == 'desfazer':
#                 desfazer(principal_list)
#         else: 
#             principal_list.append(command_or_list)
#             continue
#     except IndexError:
#         print('Não há valores para desfazer, ou refazer.')
#         continue
    
#___________________________________________________________________________
# Resolução professor

# import os


# def listar(tarefas):
#     print()
#     if not tarefas:
#         return print('Nenhuma tarefa para listar')

#     print('Tarefas:')
#     for tarefa in tarefas:
#         print(f'\t{tarefa}') # \t é um tap então irá dar um espaço.
#     print()


# def desfazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para desfazer')
#         return

#     tarefa = tarefas.pop()
#     print(f'{tarefa=} removida da lista de tarefas.')
#     tarefas_refazer.append(tarefa)
#     print()


# def refazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas_refazer:
#         print('Nenhuma tarefa para refazer')
#         return

#     tarefa = tarefas_refazer.pop()
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()


# def adicionar(tarefa, tarefas):
#     print()
#     tarefa = tarefa.strip() # serve para retirar os espaços do começo e fim, se apenas colocar ' ' será inválido
#     if not tarefa:
#         print('Você não digitou uma tarefa.')
#         return
#     print(f'{tarefa=} adicionada na lista de tarefas.') # (tarefa =) irá ser a mesma coisa que "tarefa = tarefa"
#     tarefas.append(tarefa) 
#     print()


# tarefas = []
# tarefas_refazer = []

# while True:
#     print('Comandos: listar, desfazer e refazer')
#     tarefa = input('Digite uma tarefa ou comando: ')

#     if tarefa == 'listar':
#         listar(tarefas)
#         continue
#     elif tarefa == 'desfazer':
#         desfazer(tarefas, tarefas_refazer)
#         listar(tarefas)
#         continue
#     elif tarefa == 'refazer':
#         refazer(tarefas, tarefas_refazer)
#         listar(tarefas)
#         continue
#     elif tarefa == 'clear':
#         os.system('cls')
#         continue
#     else:
#         adicionar(tarefa, tarefas)
#         listar(tarefas)
#         continue



#_________________________________________________________________________________________

# EVITAR USO DE IF AULA

import os


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


tarefas = []
tarefas_refazer = []



while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar':  lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer':  lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()


    """
    O "comandos.get(tarefa)" irá retornar a chave  ele irá checar se o comando que
    a pessoa digitou está lá, se estiver irá retornar a chave. Por exemplo o que a pessoa digitar
    foi (listar) já que a tarefa será retornada em string, listar é uma chave que está lá
    e a chave irá retornar o "lambda: listar(tarefas)".
    Isso só irá ser feito se a chave estiver lá. Se a chave não estiver lá, irá retornar a 
    chave 'adicionar' por causa do 

    "if comandos.get(tarefa) is not None else \
        comandos['adicionar']"

    Então, ou é um comando(chave) que será retornado, ou se a pessoa escrever uma chave que não
    está lá, ela será taxada como "None" e por causa do else, será adicionada em tarefas. 

    O "lambda"  é usado para adiar a execução da função, pois vai envolver a execução
    da função dada como exemplo "lambda: refazer(tarefas, tarefas refazer)" Pois irá ser retornada
    a lambda, ao invés da execução desta função. Por isto, está sendo executada depois, com
    "comando()"
    
    """
    

   