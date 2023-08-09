"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 3))

# O ponto flutuante pode ser impreciso, por isso
#tem algumas formas de arrumar tal imprecissão

numero_1d = decimal.Decimal('0.1')
numero_2d = decimal.Decimal('0.7')
numero_3d = numero_1d + numero_2d
print(numero_3d)