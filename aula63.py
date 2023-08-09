"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

# Minha resolução;

# import os
# while True:
    
#     cpf = input('Digite um Cpf: ')

#     if len(cpf) != 14:
#         os.system('cls')
#         print('Digite os 14 dígitos do cpf')
#         continue

        

#     cpf_numero_int = []

#     for digito in cpf:
#         if digito == '.' or digito == '-':
#             cpf_numero_int += []
             
                 
#         else:
#             try:

#                 digito_int = int(digito)
#                 cpf_numero_int.append(digito_int)

#             except ValueError:
#                 os.system('cls')
#                 print('Escreva o cpf em números.')
#                 cpf_numero_int = []

#                 break

#     if not cpf_numero_int:
#         continue
    

#     novo_cpf = cpf_numero_int[0:9]

    

#     numeros = []

#     for numero in range(2,10 +1):
#         numeros.append(numero)

#     numeros_inverter = (numeros[::-1])

#     i = 0
#     calculos = []

#     while i < 9:
#         calculo_mult = numeros_inverter[i] * novo_cpf[i]
#         calculos.append(calculo_mult)
#         i += 1

    

#     total = 0
    
#     for calculo in calculos:
#         total += calculo
        
    
    
#     mult_total = total * 10
    

#     resto_total = mult_total % 11
    
#     resultado = 0 if resto_total > 9 else resto_total

#     os.system('cls')
#     print(f'O primeiro dígito do cpf é {resultado}')
    

cpf = '588421450 25'
cpf_novo = ''



   
nove_digitos = cpf_novo[:9]
contador_regressivo = 10

resultado = 0

for digito in nove_digitos:
        resultado += int(digito) * contador_regressivo
        contador_regressivo -= 1

digito = (resultado * 10) % 11
digito = digito if digito <= 9 else 0

print(digito)


    

 


