# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]

# lista = [1,32,2,5,7,0,6,21,6,36]
# # lista.sort() # Ordena a lista a deixando de menor para maior
# # sorted(lista) = mesma coisa
# lista.sort(reverse=True) # O deixa de maior para menor



lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


# def ordena(item):
#     return item['nome']


# lista.sort(key=ordena) # A chave será igual a função ordena, que diz para ordenar o nome
# for item in lista: # Usado o sort na lista, junto com a função, ela será ordenada pelo alfabeto
#     print(item)



# lista.sort(key=lambda item: item['nome']) # Faz a mesma coisa que a função acima, porém irá ordenar
# E usar apenas 1  linha
# Ou
# sorted(lista,key=lambda item: item['nome'])


def exibir(lista): 
    for item in lista:
        print(item)

l1 = sorted(lista, key=lambda item: item['nome']) # O sorted serve para ordenar a lista
l2 = sorted(lista, key=lambda item: item['sobrenome']) # Não será alterado o valor da lista




print(20*'-')
print('Ordenado por nome')
exibir(l1)
print(20*'-')
print('Ordenado por sobrenome')
exibir(l2)
print(20*'-')


'''
Lambda seria como exemplo o Def, e ele  irá direto ao valor, não tem parênteses
irá direto ao parâmetro. Além de não precisar o return, então se fosse fazer essa função sem lambda :

_____________________________
def ordena(item):
    return item['nome']
lista.sort(key=ordena) 
for item in lista: 
    print(item)
_____________________________
    
agora se adicionar o lambda seria :

_____________________________
lista.sort(key=lambda item: item['nome'])
for item in lista: 
    print(item)
_____________________________


sort aletera a função
já sorted, cria uma copia raza da função

'''