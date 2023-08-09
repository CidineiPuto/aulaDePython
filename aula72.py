"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento

x, y, *resto = 1,2,3,4
print(x,y, resto)


# def soma(x,y):
#     return x +y 

def soma(*args):
    # args = list(args)
    # print(args, type(args))
    total = 0
    for numero in args:
        total += numero # Ou total + numero
    return total
        


soma1_2_3 = soma(1, 2, 3)
# print(soma1_2_3)

soma4_5_6 = soma(4, 5, 6)
# print(soma4_5_6)

numeros = 1,2,3,4,5,67,8,9,10,12
outra_soma = soma(*numeros) # Desempacota as tuplas

print(sum(numeros))

# print(sum((1,2,3,4,5,67,8,9,10,12)))
