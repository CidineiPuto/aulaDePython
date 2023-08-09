# for dentro de for na lista compreendion

lista = []
for x in range(3):  # irá ter 2 x ou seja, quantos você colocar
    for y in range(3):
        # Para cada X vai ter 2 ou a quantidade que colocou Y
        lista.append((x, y))

# Ambos são o mesmo

# lista = [
#     (x, y) # Se colocar apenas x ele irá ser '000,111,222' pois irá repetir o valor, e não adicionar outro
#     for x in range(3)
#     for y in range(3)

# ]

'''
!!!!!!!!LEMBRETE IMPORTANTE!!!!!!!!
o lado esquerdo do for do list compreendion é SEMPRE usado para o mapeamento.
'''


lista = [
    # Para cada x gera uma nova lista compreendion gerando um novo valor
    [[x, letra] for letra in 'Bungas']
    for x in range(3)

    # isto é uma lista compreendion dentro do valor de uma lista compreendion


]
print(lista)
