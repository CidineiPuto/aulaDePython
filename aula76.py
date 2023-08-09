
#_________________________________________________________________________________

# def number_to_be_duplicated(number_duplicated):
#     def duplicator(number_duplicator):
#         return number_duplicated * number_duplicator
#     return duplicator


# user_number = int(input('Digite um número: '))
# number = number_to_be_duplicated(user_number)


# for duplicator in range(2,10 +1):
#     print(f'Numero duplicador = {duplicator} | Numero a ser duplicado = {user_number} |\
#           resultado =',number(duplicator))



# _________________________________________________________________________________

import random

def duplicator(number_duplicator):
    def number_to_be_duplicated(number_duplicated):
        return number_duplicated * number_duplicator
    return number_to_be_duplicated


duplicar = duplicator(2)
triplicar = duplicator(3)
quadruplicar = duplicator(4)

numero = 5 #int(input('Digite um número: '))

for item in range(numero, numero +1):
    print(duplicar(item))
    # print(triplicar(item))
    # print(quadruplicar(item))

#_________________________________________________________________________________



# def criar_multiplicador(multiplicador):
#     def multiplicar(numero):
#         return numero * multiplicador
#     return multiplicar

# duplicar = criar_multiplicador(2)
# triplicar = criar_multiplicador(2)
# quadruplicar = criar_multiplicador(2)


# print(duplicar(2))
# print(triplicar(2))
# print(quadruplicar(2))







