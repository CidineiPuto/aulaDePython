"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
Refatorar: Editar o seu código.
"""
# Z = None

def soma(x, y,z=None):
    if z is not None:
        print(f"{x=} {y=} {z=}","|", x + y + z)
    else:
        print(f"{x=} {y=}","|", x + y)


soma(1,2)
soma(3,5)
soma(200,100,0)
soma(y=9, z=0, x=7)