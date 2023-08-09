"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# Método 1 (Eu)

#digite_numero_par_ou_impar = (input('Digite um número inteiro: '))
#numero_e_par = (f'O número {digite_numero_par_ou_impar} é par.')
#numero_e_impar = (f'O número {digite_numero_par_ou_impar} é impar.')

#try:
#    digite_numero_par_ou_impar =  int(digite_numero_par_ou_impar)
#    numero_inteiro_calculo = (digite_numero_par_ou_impar % 2)
#    if numero_inteiro_calculo == 0:
#        print(numero_e_par)
#    elif numero_e_impar == -0:
#        print('Não existe kkkk')
#    else:
#        print(numero_e_impar)
#except:
#    print('Isso não é um número, ou não é um número inteiro.')

# Método 2 (Professor)

#if digite_numero_par_ou_impar.isdigit():
#    digite_numero_par_ou_impar_int = int(digite_numero_par_ou_impar)
#    par_impar = digite_numero_par_ou_impar_int % 2 == 0
#    par_impar_texto = 'ímpar'
#
#    if par_impar is True:
#        par_impar_texto = 'par'
#
#    print(f'O número {digite_numero_par_ou_impar_int} é {par_impar_texto}')
#else:
#    print('Você não digitou um número inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""




#quantas_horas_são = input('Escreva as horas em números INTEIROS e POSITIVOS:  ')
#try:
#    quantas_horas_são_int = int(quantas_horas_são)
#    bom_dia = quantas_horas_são_int >= 0 and quantas_horas_são_int <= 11
#    boa_tarde = quantas_horas_são_int > 11 and quantas_horas_são_int <= 17
#    boa_noite = quantas_horas_são_int > 17 and quantas_horas_são_int < 24
#
#    if  bom_dia:
#        print('Bom dia amigo, tenha um ótimo dia.\r\n')
#    elif boa_tarde:
#        print('Boa tarde, tenha uma ótima tarde.\r\n')
#    elif boa_noite:
#        print('Boa noite, durma bem.\r\n')
#    else:
#        print('Esse número não é válido.\r\n')
#except:
#    print('Tente novamente,desta vez, digite um número INTEIRO e POSITIVO.')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""


# Método 1 (Eu)

#nome = input('Digite seu nome: ')
#nome_4_digitos = (nome[0:4])
#nome_5_digitos = (nome[0:5])
#nome_6_digitos = (nome[0:6])
#
#
#nome_menor_que_1 = (nome[0:1])
#nome_pequeno = nome == nome_4_digitos
#nome_normal = nome >= nome_5_digitos and nome <= nome_6_digitos
#
#if nome <= nome_menor_que_1:
#    print('Digite mais de uma letra.')
#elif not nome:
#    print('Digite um nome')
#elif nome_pequeno:
#     print('Seu nome é pequeno.')
#elif nome_normal:
#    print('Seu nome tem um tamanho normal.')
#else:
#    print('Seu nome é grande.')


# Método 2 (Professor)

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto.')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é mediano.')
    else:
        print('Seu nome é muito grande.')

else:
    print('Digite um nome com mais de uma letra.')