"""
Higher Order Functions
Funções de primeira classe
"""
def saudacao(msg,name):
    return f'{msg}, {name}!'
 

def execute(function, *args):
    return function(*args)

print(
    execute(saudacao, 'bom dia', 'Rafael')
)
print(
    execute(saudacao, 'boa noite', 'Jão')
)

# v = saudacao_2('Bom dia')
# print(v)

"""
Termos técnicos: Higher Order Functions e First-Class Functions
Academicamente, os termos Higher Order Functions e First-Class Functions têm significados
 diferentes.

Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns
 (strings, inteiros, etc...)

Não faria muita diferença no seu código, mas penso que deveria lhe informar isso.

Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.
"""