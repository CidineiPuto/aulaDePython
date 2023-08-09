"""
enumerate - enumera iteráveis (índices)
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('Jão')
lista.append('Tiagão')
lista.append('billyzão')
lista.append('Kayão')


# lista_enumerada = enumerate(lista) # Tipo de iterador
# print(next(lista_enumerada))


# Quando a lista acaba o enumerate, não consegue dar mais itens

# print('Itens que sobraram no enumerate :', lista_enumerada)

# for item in lista_enumerada:
#     print(item)

# for item in enumerate(lista): # Maneira de contornar o "erro"
#      indice,nome = item
#      print(indice,nome) # Pode desempacotar os valores  
                # Se usar o A e B seria o indice e o nome


for indice,nome in enumerate(lista): # É como se fosse um for dentro de outro
      print(indice,nome, type(lista[indice])) # tem o mesmo efeito que o anterior, só que é mais eficaz

# for tupla_enumerada in enumerate(lista):
#       print('FOR da tupla:')
#       for valor in tupla_enumerada:
#             print(f'\t{valor}')


# for item in enumerate(lista): # E assim ele nunca irá esgotar
#     print(item)


# lista_enumerada = list(enumerate(lista)) # Pode começar de qualquer outro índice
# Como "lista_enumerada = list(enumerate(lista, start =10))"

# print(lista_enumerada)


# O enumerade cria um TUPLA com índice e valor.






























