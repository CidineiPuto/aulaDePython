# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
products = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

# Minha resolução _________________________________________________________________________

# import copy

# new_products = [
#     {**product,'preco': round(product['preco'] * 1.1,2)}
#     for product in copy.deepcopy(products)
#     ]

# def sorted_name(item):
#     return item['nome']
# def sorted_value(item):
#     return item['preco']

# products_sorted_by_name = copy.deepcopy(sorted(new_products,key=sorted_name, reverse=True))
# products_sorted_by_value = copy.deepcopy(sorted(new_products,key=sorted_value))

# for item in new_products:
#     print(item)


# Resolução Professor _________________________________________________________________________


import copy
from dados import produtos

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1,2)}
    for p in copy.deepcopy(produtos)
    ]

# **p cria um novo dicionário expandindo um dicionário.
 # 'preco' : # recria a chave preco 
 # round(p['preco'] * 1.1,2) round arredonta o float com apenas 2 decimais na frente por conta do ,2
# preco['preco'] * 1.1 aumenta o preco em 10%



produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos), 
    key=lambda p: p['nome'],
    reverse=True
)


#  copy.deepcopy(produtos),key=lambda p: p['nome'] 
# passa uma função lambda que recebe um produto e retorna o produto['nome'] dos produtos
# copiados por deepcopy 

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos), 
    key=lambda p: p['preco']
)

# FINAL

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')