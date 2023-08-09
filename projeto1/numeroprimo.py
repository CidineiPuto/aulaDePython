def calculo_numero_primo(numero, total):
    try:
        numero_int = int(numero)
    except ValueError:
        return print(f'"{numero}" Não é um número')

    for calculo in range(1, numero_int + 1):
        if numero_int % calculo == 0:
            print("\033[33m", end=" ")  # amarela
            total += 1
        else:
            print("\033[31m", end=" ")  # vermelho

        print(f"{calculo}", end="")  # faz a linha não ter quebras
    print(f"\r\n\033[m O número {numero_int} foi dívisivel {total} vezes.")

    if total == 2:
        return print("E por isso ele É primo.")
    print("E por isso ele NÃO primo.")


número = input("Digite um número inteiro, e veja se é primo: ")
total = 0
calculo_numero_primo(número, total)


# obs :

# A variável \033 deixa a cor significa um código de cor
# "print(f'{calculo}', end='')" Vai dar print no número, até chegar ao número
# primo
# Se o núm for divisivel, será amarelo, se não, será vermelho

# '\r\n\033[m' a cor fica normal
# '\033[33m' a cor fica amarela
# '\033[31m' a cor fica vermelha
