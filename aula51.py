"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
# nome = 'Luiz'
# noutra_variavel = nome
# nome = 'jão'
# print(nome)
# print(noutra_variavel)

lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() # Retorna os mesmos valores da lista para a lista b
# Em resumo, as mudanças que fazer na a, não será feita na b


lista_a[0] = 'qualquer coisa'
print(lista_a)
print(lista_b)