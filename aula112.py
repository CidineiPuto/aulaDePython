# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]



# Atividade não resolvida


def zipper(l1, l2):
    intervalo = min(len(l1), len(l2)) # Pega a lista que possui o menor I no caso, a menor lista
    return [(l1[i], l2[i]) for i in range(intervalo)]
 
l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']




# FUNÇÃO ZIP ______________________________________________________________________




# from itertools import zip_longest

# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA', 'SP', 'MG', 'RJ']


# print(list(zip(l1, l2))) # Faz list(zip) faz uma função zip
# print(list(zip_longest(l1, l2), fillvalue='Sem cidade')) # Ao invés de usar a lista menor, usa a maior
# # O valor que está faltando irá se chamar "Sem cidade"