'''
O print, serve para como dito anteriormente, demonstrar algo na tela.
'''

print(123,456, sep=',', end='/\r\n')
print(34,23, sep="-", end='/\r\n')

# A vírgula está sendo usado para separar os valores.
'''
Existe uma outra função, chamado de SEP e ela serve
para dar ao separador, outra forma de separar como por exemplo sep=',' ou sep=","
'''

# o \r\n que é igual a CRLF é uma quebra de linha invisível que está no seu código.
# ( No linux e MAC eles são trocados por \n e LF)
# Esses códigos são representados como o comando "end"
# E a quebra de linha támbem pode ser mudada, como por exemplo dessa forma =

'''
print('atirirei o pau no gato' end='/\r\n')
'''

# Támbem podemo fazer NÃO ter quebra de linha.

print(123, end=('*'))
print(123)

# Print não existe, apenas print colocando o "p" como minúsculo

