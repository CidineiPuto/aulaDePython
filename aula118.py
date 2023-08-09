# filter é um filtro funcional
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

# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 10
# ]

def filtrar_preco(produto):
    return produto['preco'] > 100

novos_produtos = filter( 
    # lambda p: p['preco'] >= 10,
    filtrar_preco,
    produtos)

print_iter(produtos)
print_iter(novos_produtos)


"""
filter_________________________________________________________________________________
Filter irá filtrar tal valor se o valor for maior,ou menor, ou igual a tal número. Isso quer dizer
que o filter poderá fazer uma lista menor, ou do mesmo tamanho. MAS NUNCA, maior que a 
original.
________________________________________________________________________________________
"""