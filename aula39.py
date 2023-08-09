"""Calculadora com while"""

# Minha resolução

"""
while True:

    print('\r\n')
    num_1 = input('Escolha o primeiro número: ')
    print('\r\n')
    num_2 = input('Escolha o segundo número: ')
    while True:
        try:
            num_1_float = float(num_1)
            num_2_int = float(num_2)
            adicao = num_1_float + num_2_int
            subtracao = num_1_float - num_2_int 
            multiplicacao = num_1_float * num_2_int
            divisao = num_1_float / num_2_int
            print('\r\n')
            operacao = (input('Escolha qual operação deseja usar. Se quiser multiplicação escolha "+" para adição, "-" para subtração, "/" para divisão e "*" para multiplicação: '))
            print('\r\n')
            if operacao == '+':
                print(f'{num_1_float} + {num_2_int} = {adicao}')
            elif operacao == '-':
                print(f'{num_1_float} - {num_2_int} = {subtracao}')
            elif operacao == '*':
                print(f'{num_1_float} * {num_2_int} = {multiplicacao}')
            elif operacao == '/':
                print(f'{num_1_float} / {num_2_int} = {divisao}')
            else:
                print('Escreva uma operação certa.')
                
            print('\r\n')
            break

        except:
            print('Escreva um número.')
            print('\r\n')
            break
    sair = input('Quer sair? [S]im ')
        if sair == 'S' or sair == 's':
            print('Você saiu da calculadora.')
            break

"""

# sair = input('Quer sair? [S]im ')
# if sair == 'S' or sair == 's':
#     print('Você saiu da calculadora.')
#     break

# Professor resolução =

""" Calculadora com while """
while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite o operador (+-/*): ")

    num_1_float = 0
    num_2_float = 0

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um ou ambos os números digitados são inválidos.")
        continue

    operadores_permitidos = "+-/*"

    if operador not in operadores_permitidos:
        print("Operador inválido.")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue

    print("Realizando sua conta. Confira o resultado abaixo: ")
    if operador == "+":
        print(f"{num_1_float} + {num_2_float} =", num_1_float + num_2_float)
    elif operador == "-":
        print(f"{num_1_float} - {num_2_float} =", num_1_float - num_2_float)
    elif operador == "*":
        print(f"{num_1_float} * {num_2_float} =", num_1_float * num_2_float)
    elif operador == "/":
        print(f"{num_1_float} / {num_2_float} =", num_1_float / num_2_float)
    else:
        ("Nunca deveria chegar aqui.")

    sair = input("Quer sair? [s]im: ").lower().startswith("s")

    if sair is True:
        break
