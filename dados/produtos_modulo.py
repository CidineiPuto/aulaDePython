produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# isinstance() Argumento usado para saber qual será a instância

um_dois_tres = 1,2,3,'a'


for item in um_dois_tres:
    if  isinstance(item, int):
        print(f'O dígito {item} é int.')
    else:
        print(f'O dígito {item} não é int.')

