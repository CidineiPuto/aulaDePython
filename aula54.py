"""
Tipo tupla - Uma lista imutável
"""
# nomes = ('Maria', 'Helena', 'Luiz')
# print(nomes[-1])
# print(nomes,(type(nomes)))

# ou
nomes = ['Maria', 'Helena', 'Luiz']
nomes1 = tuple(nomes)
nomes2 = list(nomes1)
print(nomes1, type(nomes1))
print(nomes2, type(nomes2))


# nomes = tuple(nomes)
# nomes = list(nomes)