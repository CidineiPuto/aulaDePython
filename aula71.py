"""
retorno dos valroes das funções (return)
"""
def soma(x,y):
    if x > 10:  # Se for verdadeiro, ele irá retornar o valor e sair da função
        return 10,20 # No caso só pode ter um return por função
    return x+y # Indica para parar TUDO e retornar este valor
               # Como se ele fosse uma váriavel

soma1 = soma(2,2)
soma2 = soma(3,3)
print(soma1)
print(soma2)
# print(soma1 + soma2)
print(soma(11,55))

# variavel = soma(1,2)
# variavel = int('1')
# print(variavel)

# variavel = print('Bungas')
# variavel = None
# print(variavel)
# print(variavel is None)