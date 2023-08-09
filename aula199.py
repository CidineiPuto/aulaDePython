# sys.argv - Executando arquivos com argumentos no sistema
# Fonte = Fira Code
import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print("Você não passou argumentos")
else:
    try:
        print(f"Você passou os argumentos {argumentos[1:]}")  # 1: pega do 1
        # adiante.
        print(f"Faça alguma coisa com {argumentos[1]}")
        print(f"Faça outra coisa com {argumentos[2]}")
    except IndexError:
        print("Faltam argumentos")

# para passar um argumento
# python (nome do módulo).py (argumentos)


"""
Para usar o python do ambiente virtual mesmo estando sem ele ativado, coloque o
caminho;
ex: venv/bin/python aula199.py

Isso é um exemplo claro, mas neste caso, irá ocorrer uma ação dentro do venv.

O primeiro argumento sempre será o script que você executar.
"""
