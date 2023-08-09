"""
For + Range
range -> range(start, stop, step)
"""

numeros1 = range(10 +1)
numeros2 = range(5,10 +1) 
numeros3 = range(5,10 +1,2)  # COMEÇA (Start) com 5, TERMINA (Stop) com 10, e PULA (Step) 2 numeros
#No caso o Start, define qual primeiro numero o Stop, diz aonde ele terminará
#e o step, será usado para pular os número de X em X
numeros4 = range(0, -10 -1, -2)

# print(numeros1[5])
# print(numeros2[3])
# print(numeros3)

'''
No while teriamos que pegar o  índice I, e pelo Indice buscar o valor.
Enquanto no for, temos o "Valor" em 'For [valor] in [variavel] ele vai pegar
o valor da variavel, e a recortar fazendo ser escrita de baixo pra cima.
'''
espaco = 10*'-'

print('Numeros1')
for numero1 in numeros1:
    print(numero1)
print(espaco)
print('Numeros2')
for numero2 in numeros2:
    print(numero2)
print(espaco)
print('Numeros3')
for numero3 in numeros3:
    print(numero3)
print(espaco)
print('Numeros4')
for numero4 in numeros4:
    print(numero4)
print(espaco)


#(O PROGRAMA A SEGUIR NÃO ESTÁ COMPLETO, É APENAS UM PEQUENO TESTE COM O RANGE, E FOR IN)

# print('Escreva 2 numeros, e os números que aparecerem em seguida, são os pares de um entre outro.')
# print('\r\n')
# descubra_se_numero_par = input('Escreva o primeiro número: ')
# descubra_se_numero_par2 = input('Escreva o segundo número: ')

# descubra_se_numero_par_int = 0
# descubra_se_numero_par2_int = 0
# resultado = 0

# try:
#     descubra_se_numero_par_int = int(descubra_se_numero_par)
#     descubra_se_numero_par2_int = int(descubra_se_numero_par2)
#     print('Os pares desse número são: ')
#     resultados = range(descubra_se_numero_par_int, descubra_se_numero_par2_int +1, 2)
#     for resultado in resultados:
#         print(resultado)

# except:
#     print('Escreva um número válido e inteiro.')


