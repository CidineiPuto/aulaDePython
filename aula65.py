import os
import random

while True:
    os.system
    cpf_quantidade = input('Digite o número de cpfs que deseja, no máximo 100: ')
    try:
        cpf_quantidade_int = int(cpf_quantidade)
        if cpf_quantidade_int > 100:
            print('Digite um número menor que 100.')
            continue
    except ValueError:
        print('Digite um número.')
        continue



    for item in range(cpf_quantidade_int):

        nove_digitos =''
        
        for i in range(9):
            nove_digitos += str(random.randint(0,9))


        contador_regressivo_1 = 10
        resultado_digito_1 = 0


        for digito in nove_digitos:
            resultado_digito_1 += int(digito) * contador_regressivo_1
            contador_regressivo_1 -= 1
        digito_1 = (resultado_digito_1 * 10) % 11

        digito_1 = digito_1 if digito_1 <= 9 else 0

        dez_digitos = nove_digitos + str(digito_1)

        contador_regressivo_2 = 11

        resultado_digito_2 = 0

        for digito in dez_digitos:
            resultado_digito_2 += int(digito) * contador_regressivo_2
            contador_regressivo_2 -= 1

        digito_2 = (resultado_digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0


        cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

        print(cpf_gerado_pelo_calculo)

    continuar = input('Deseja continuar ? [S]im [N]ão  ').lower().startswith('s') 
    if continuar is True:
        os.system('cls')
        continue
    else:
        os.system('cls')
        break

print('Tu saiu')