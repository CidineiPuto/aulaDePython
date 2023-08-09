"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1  2  3
#       -4   -3 -2 -1             
lista = [1, 4, 8, 2] # Mesmo que ("lista = list()")]
# numero = lista[2] # = 8
# lista[2] = 300 # Depois dessa linha o valor será alterado
# del lista[2] # irá deletar o terceiro(2) valor da lista, o fazendo parar de existir.
# print(lista)
# print(lista[2])

lista.append(50) # Adiciona , Objetos,Na lista
# ultimo_valor = lista.pop() # Usado para remover o ultimo objeto
lista.append(60) 
lista.append(70) 
# ultimo_valor = lista.pop() # E ele retorna o valor removido
# O pop  támbem pode ser usado para remover mais de um valor por vez 
ultimo_valor = lista.pop(3) # Como usado desta forma.
print(lista, 'Removido', ultimo_valor)

