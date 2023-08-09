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
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Bungas')
nome = lista.pop() # Puxa o ultimo valor
lista.append(1230)
del lista[-1] 
# lista.clear()
lista.insert(0,5) # O primeiro, é o índice aonde irá adicionar
# E o segundo, é o que vai adicionar lá
# Caso coloque um índice maior do que seu último índice ele irá
# Enviar o número ao último índice
lista.insert(10000,23) # Como por exemplo nesse caso
lista.insert(1,'fanfas')
print(lista[6])