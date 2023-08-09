# reduce - faz a redução de um iterável em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

# def funcao_do_reduce(acumulador,produto): # O acumalador seria o inicio
#      print('acumulador', acumulador) #E o produto que estaria sendo repassado
#      print('produto', produto)
#      print()
#      return acumulador + produto['preco']

# total = reduce(
#     funcao_do_reduce, 
#     produtos,
#     0
# )

total = reduce(
    lambda ac,p: ac + p['preco'], 
    produtos,
    0
)

print('Total é', total)

# total = 0
# for p in produtos:
#     total += p['preco']

# print(total)

# print(sum([p['preco'] for p in produtos]))

"""
reduce__________________________________________________________________________________
Reduz um iterável, como o "Produtos" em um único valor. Nesta function :

def funcao_do_reduce(acumulador,produto):

O acumulador, ou o "prev", normalmente, salva o último valor usado. E ele é igual as outras
funções anteriores, passando de um número um por um como se fosse um for item.
O reduce, irá precisar 

total = reduce(funcao_do_reduce, produtos,0)
             da função       da variável  do inicio
função : Diz o que ele deve fazer.
variavel : Irá fazer a modificação dentro da mesma
inicio : Diz aonde deve começar.

Támbem o valor inicial diz qual tipo  de produto irá usar. Por isso, sempre haverá chance
de dar erro em seus cálculos, por isso é sempre bom usar o valor inicial.
________________________________________________________________________________________
"""