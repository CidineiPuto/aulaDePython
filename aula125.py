# Problema dos parâmetros mutáveis em funções Python

def adiciona_clientes(nome, lista=[]):
    lista.append(nome)
    return lista

# cliente1 = adiciona_clientes('luiz')
# adiciona_clientes('Joana', cliente1)
# print(cliente1)

# cliente2 = adiciona_clientes('Helena')
# adiciona_clientes('Maria', cliente2)
# print(cliente1)


"""
Caso por exemplo não passe um parâmetro para  a lista, apenas colocar por exemplo :

cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
print(cliente1)

O cliente 1 será usado sempre, então a lista será apenas uma. A única maneira de realmente
adicionar outras listas, é sempre passando o nome das listas para não dar este erro de 
param.
Pois por ser um parâmetro  mutável o python sempre irá utilizar a mesma lista, já que
nenhuma hora passou uma lista específica.

"""

# lista1 = []
# cliente1 = adiciona_clientes('luiz', lista1) # está seria uma maneira de consertar o erro acima.
# adiciona_clientes('Joana', cliente1)
# print(cliente1)



# cliente2 = adiciona_clientes('Helena')
# adiciona_clientes('Maria', cliente2)
# print(cliente2)

"""
O ideal seria, quando for definir um param padrão com argumento padrão, 
se for mútavel o recomendado é não jogar o valor no parametro, como por exemplo

def adiciona_clientes(nome, lista=[])

o recomendado não seria jogar exatamente no "lista=[]" já que este valor sempre será o mesmo
quando for usar a função. 
Coloque valores imutáveis como por exemplo um "lista=None"  a função ficaria assim
"""

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)
print(cliente1)

"""
No final, nunca deixe um valor padrão mutável, coloque o valor mutável tipo 
"lista=[]" faça ela virar "lista=None" neste pensamento, faça o parâmetro mutável dentro
da função pois se a pessoa não enviar nada, o param será criado. 


def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


"""