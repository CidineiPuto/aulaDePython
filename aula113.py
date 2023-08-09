"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

# Solução 1______________________________________

# Minha solução_______________________________________________________________________

# list_a  = [1, 2, 3, 4, 5, 6, 7]
# list_b  = [1, 2, 3, 4]


# def sum_items(l1, l2):
#     intervalo = min(len(l1), len(l2))
#     return [(l1[i] + l2[i]) for i in range(intervalo)]

# list_total = sum_items(list_a, list_b)

# print(list_total)

# Solução 2__________________________________________


# lista_soma =  [(list_a[i] + list_b[i]) for i in range(min(len(list_a), len(list_b)))]


# Solução professor___________________________________________________________________


# list_a  = [1, 2, 3, 4, 5, 6, 7]
# list_b  = [1, 2, 3, 4]
# lista_soma = []

# Solução 1______________________________________

# for i in range(len(list_b)):
#     lista_soma.append(list_a[i] + list_b[i])
# print(lista_soma)

# Solução 2______________________________________

# for i, _ in enumerate(list_b): # "_" Está lá para dizer que quer somente o indice.
#     lista_soma.append(list_a[i] + list_b[i])
# print(lista_soma)

# Solução 3_____________________________________

# lista_soma = [x + y for x , y in zip(list_a, list_b)] # Zip faz a mesma coisa que
# " def sum_items(l1, l2):
#                                        intervalo = min(len(l1), len(l2))
#                                       return [(l1[i] + l2[i]) for i in range(intervalo)] "


# _____________________________________________________________________________

# O problema é que zip só une as listas até o tamanho da menor lista
# (como proposto no exercício).

# Uma outra possibilidade é usar zip_longest para capturar os valores da lista maior.

from itertools import zip_longest

lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]

# Neste caso, usamos o "fillvalue" como 0 (zero),
# assim conseguimos capturar os valores restantes da lista maior,
# realizando contas, sem obter um erro em nosso programa.
