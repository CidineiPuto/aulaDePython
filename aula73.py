# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def mult(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


numero = 1,4,5,6,7,9
multiplicacao = mult(*numero)
print(multiplicacao)




















# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
import random

def par_impar(x):
    multiplo_de_dois = x % 2 == 0 
    if multiplo_de_dois:
        return print(f'Número {x} é par.')
    return print(f'Número {x} é impar')

outro_par_impar = par_impar
numero_e_par = outro_par_impar 

