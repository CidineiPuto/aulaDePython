"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)

#         0    1     2     3      4   (Diferente de STR as listas guardam itens, não só letras)
lista = [123,True, 2.2, 'Bungas',[]] # = ''
#         -5  -4    -3    -2      -1
# print(bool([])) # False
# print(lista, type(lista)) # Tipo 'lista'
# print(lista[-2].upper(), type(lista[3]))
lista[3] = 'Fanfas' # Pode mudar o objeto da lista que você escolher
print(lista)
print(lista[-2], type(lista[3]))