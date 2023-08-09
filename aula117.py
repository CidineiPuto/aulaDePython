from functools import partial

# map - para mapear os dados
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem=1.1)

# novos_produtos = [
#     {**p, 
#     'preco': aumentar_dez_porcento(p['preco'])} 
#     for p in produtos
# ]

def muda_preco_de_produtos(produto):
    return {
        **produto, 
        'preco': aumentar_dez_porcento(produto['preco'])} 


novos_produtos = map(
    muda_preco_de_produtos,
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)




"""
PARTIAL________________________________________________________________________________

A função partial é usada como uma função closer ( Uma função que recebe outra função,
um ou mais argumentos da sua função. Passa a ela as funções parcialmente.
). 
_______________________________________________________________________________________
"""

"""
MAP________________________________________________________________________________
Faz igual ao mapeamento da list compreendion, passando a função X em cada um dos 
produtos. Támbem é um iterador, necessário de um next, ou um for item para puxar item em
item. Caso queira ver o valor de um map é necessário fazer o seguinte :
"print(list(novos_produtos))"

O iterador é esgotado, então se não quiser esgotar ele
é necessário transformar o map em lista antes de usar ele fazendo o seguinte :

"novos_produtos = list(map(
    muda_preco_de_produtos,
    produtos
))"

Pode se fazer isto para ficar reutilizando o map, pois ele não será mais um iterador, e sim
uma lista.
___________________________________________________________________________________
"""




print(hasattr(novos_produtos, '__iter__'))
print(hasattr(novos_produtos, '__next__')) # Mostra que map é iterador





# Todo generator é um iterador, mas nem todo iterador é um generator.
# Como saber se a função é generator ? Simples, utilize isto.

# from types import GeneratorType

# novos_produtos = (x for x in produtos)

# print(novos_produtos)
# print(hasattr(novos_produtos, '__iter__'))
# print(hasattr(novos_produtos, '__next__'))
# print(isinstance(novos_produtos, GeneratorType))

print(list(
    map(
    lambda x: x * 3, [1,2,3,4]
    )
    ))
