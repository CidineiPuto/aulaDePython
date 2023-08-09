"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}' , '|', 'x + y + z=' ,x + y + z)

soma(1,2,3)
soma(y=2,z=3, x=1) # Se o 2 por exemplo for nomeado o 3 támbem terá que ser nomeado.
soma(1, 2, z=5)
soma(1,y=4,z=8)







