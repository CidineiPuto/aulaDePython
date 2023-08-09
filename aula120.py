# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

# PART 1____________________________________________________________

# def recursiva(inicio=0, fim=10):
#     print(inicio,fim)

#     # Caso base
#     if inicio >= fim:
#         return fim
     
   
#     # Caso recursivo
#     # Contar até chegar ao final
#     inicio += 1
#     return recursiva(inicio, fim)


# print(recursiva())


"""
Função recursiva, vai "esfarelando" a função e a diminuindo, resolvendo os problemas.
por exemplo, esta função aqui :

def recursiva(inicio=0, fim=10):
    print(inicio,fim)
    if inicio >= fim:
        return fim
    inicio += 1
    return recursiva(inicio, fim)

irá repetir o módulo da função e fará o inicio sempre ser + 1, então isso pode dar erro
já que pode gerar infinitas call stacks, que armazena o escopo de uma função, esperando
ela ser resolvida. MAS se adicionar o "if inicio >= fim" ela terá um fim, e após
chegar no fim. A call stack ficará resolvendo todas as funções anteriores,
então se o fim for muito grande, poderá gerar um erro.
"""


# PART 2____________________________________________________________


# import sys

# sys.setrecursionlimit(1004)


# def recursiva(inicio=0, fim=10):
#     print(inicio,fim)

#     # Caso base
#     if inicio >= fim:
#         return fim
     
   
#     # Caso recursivo
#     # Contar até chegar ao final
#     inicio += 1
#     return recursiva(inicio, fim)


# print(recursiva(0,1000))

"""
Quando for usar uma função recursiva o escopo inteiro tem que ser salvo na memória
na call stack.
"""

def factorial(n):
    if n <= 1 or n <= 0:
        return 1
    
    return n * factorial(n - 1)


print(factorial(5))

