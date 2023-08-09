# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations,permutations, product

def print_iter(iterador):
    print(*list(iterador), sep='\r\n')  # List pode ser usado como um for item in range
                                       # Para mostrar todos os next


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]


# Combinations ____________________________________________________________

# print(combinations(pessoas, 2)) # Fazer combinação das pessoas em grupo de dois
# Não importando a ordem, em resumo, pode ser "João e Joana, ou, Joana e João" 
# Sem uma ordem predefinida
# Além disto, ele é um iterador



# print_iter(combinations(pessoas, 2)) # Com combinations não tera repetição de um do valor da 
             # direita  pro valor da esquerda

# permutations ____________________________________________________________

# print_iter(permutations(pessoas,2)) # A ordem importa, e vem todas as combinações possiveis 


# product ____________________________________________________________________

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

print_iter(product(*camisetas)) # Funciona de maneira melhor quando coloca "*"
