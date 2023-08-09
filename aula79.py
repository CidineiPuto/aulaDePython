# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro 

pessoa = {
    'nome':'Rafael',
    'sobrenome':'Alves Queiroz',
    'idade': 15,
    # 'altura': 1.8,
}

#----------------------------len------------------------------
# print(len(pessoa)) #ou (pessoa.__len__()) 
#-----------------------------keys----------------------------
# print(tuple(pessoa.keys())) # ou print(list (pessoa.keys()))

# for chave in pessoa.keys():
#      print(chave)

#--------------------------values-----------------------------

# print(list(pessoa.values())) # ou print(tuple(pessoa.values()))

# for valor in pessoa.values():
#     print(valor)

#-------------------------items-------------------------------

print(list(pessoa.items())) # ou print(tuple(pessoa.items()))

for chave,valor in pessoa.items():
    print(chave,valor)

#-------------------------check--------------------------------

# pessoa.setdefault('altura', 1.8)
# print(pessoa['altura'])

#-------------------------copy--------------------------------


# -- Shallow copy  --

# d1 = {
#     'c1' : 1,
#     'c2' : 2,
#     'c3' : 3,
#     'l1' : [0,1,2]
# }


# d2 = d1
# d2['c1'] = 1000 # O valor c1 será alterado no d1. 
# print(d1)

# d2 = d1.copy()  # Ou d2 = copy.copy(d1)

# d2['c1'] = 1000

# d2['l1'][1] = 99999 # Justamente por causa da lista ser mutável, o L1 dentro do D1
# # Será alterado, já que o valor será lincado.

# print(d1)  # Valor não será alterado.
# print(d2) # Porem o shallow copy só irá copiar valores imutáveis.

#--Deep copy--

# import copy 

# d2 = copy.deepcopy(d1) # Agora a copia será feita completamente

# d2['c1'] = 1000

# d2['l1'][1] = 99999  # MEsmo sendo valor mutável, nada irá ocorrer com o d1, apenas com o d2

# print(d1)  
# print(d2)


#-------------------------get--------------------------------
# p1 = {
#     # 'nome':'Rafael',
#     'sobrenome':'Alves Queiroz',
# }


# print(p1.get('nome')) # = print(p1['nome'])

# print(p1.get('idade')) # None
# print(p1.get('nome','Não existe')) # Se Nome = None, nome 'não existe'

#-------------------------pop--------------------------------

# p1 = {
#     'nome':'Rafael',
#     'sobrenome':'Alves Queiroz',
# }

# nome = p1.pop('nome')
# print(nome)
# print(p1)

#----pop item----
# p1 = {
#     'nome':'Rafael',
#     'sobrenome':'Alves Queiroz',
# }

# ultima_chave = p1.popitem()  # Se fazer "ultima_chave = p1.popitem('nome') = TypeError"
# print(ultima_chave)
# print(p1)

#-------------------------update--------------------------------
 
# Atualiza os dados.

# p1 = {
#     'nome':'Rafael',
#     'sobrenome':'Alves Queiroz',
# }

# Forma 1

# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })

# Forma 2

# p1.update(nome='novo valor', idade=30)

# Forma 3

# tupla = (('nome','novo valor'),('idade',30)) # ou ('nome','novo valor'),('idade',30)
# lista = [['nome','novo valor'],['idade',30]] # ou ['nome','novo valor'],['idade',30]

# p1.update(tupla) # Ou p1.update(('nome','novo valor'),('idade',30))
# p1.update(lista) # ou p1.update[['nome','novo valor'],['idade',30]]

# print(p1)

