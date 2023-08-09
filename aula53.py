"""

Introdução ao empacotamento e desempacotamento
"""


# nomes = ['Maria','Helena', 'Luiz']
# nome1, nome2, nome3 = nomes
_,_,nome3, *resto = ['Maria','Helena', 'Luiz'] # É usado "*" para empacotar
# o resto dos valores que sobrar
print(nome3)
# Valores que não vão usar são trocados por '__'

#0     #1     #2





# nome2 = nomes[1]
# print(nome2)
# for letra in nome2:
#     print(letra)