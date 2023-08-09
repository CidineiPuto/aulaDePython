"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista_a = [1,2,3,4,5]
lista_b = [6,7,8]
lista_ab = lista_a + lista_b
lista_a.extend(lista_b) # Não é possível obter o valor com uma variável
# Pois ele aumenta a lista A adicionando a lista B em sua frente
lista_c = ['bungas','fanfas','lalaus']
del lista_a[1]
print(lista_a)
