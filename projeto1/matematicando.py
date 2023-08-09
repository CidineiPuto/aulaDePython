def second_degree_equation(a, b, c):
    try:
        f_a = float(a)
        f_b = float(b)
        f_c = float(c)
    except ValueError:
        return "Escreva números"
    delta = (f_b**2) - 4 * f_a * f_c
    if delta <= -1:
        return f"Seu delta {delta}  deu negativo, NÃO EXISTE RAIZES NEGATIVAS.\n"
    bhaskara1 = -f_b
    bhaskara2 = delta ** (1 / 2)
    bhaskara3 = 2 * f_a
    try:
        xl = (bhaskara1 + bhaskara2) / bhaskara3
        xll = (bhaskara1 - bhaskara2) / bhaskara3
        res = f'O xl deu "{xl:.2f}", o xll deu "{xll:.2f}".'
        return res
    except ZeroDivisionError:
        return 'O resultado de sua equação foi "0" '


print("Cálculos disponíveis : [R]aiz de segundo grau ")
option = input("Que cálculo deseja fazer ? ")

if option == "R".lower():
    a = input("Digite a raiz acompanhada pelo quadrado : ")
    b = input("Digite o acompanhante do x: ")
    c = input("Digite o produto solitário: ")
    print(second_degree_equation(a, b, c))
