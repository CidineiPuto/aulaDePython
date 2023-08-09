""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]
    if letra == ' ':
        break

    print(letra)
    i += 1
else:   
    print('Não encontrei um espaço na string.')
print('Fora do while.')
#Se o while for fechado de uma vez com o 'break' o Else não será executado.