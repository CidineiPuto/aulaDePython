# Generator expression, Iterables e Iterators em Python

#____________________________Iterador/iterable____________________________
iterable = ['Eu', 'Tenho', '__iter__']


iterator = iter(iterable)  # tem __iter__ e __next__
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))





#____________________________generator____________________________

import sys

# Todo generator é um iterator, mas nem todo iterator é um generator
# Generator pausa em lugar, depois volta, e logo pausa novamente.

lista = [n for n in range(1000000)] # A lista neste iterável está todo na memória
print(sys.getsizeof(lista)) # a lista tem 85176 bytes 

generator = (n for n in range(1000000)) # Generator 

print(sys.getsizeof(generator)) # <generator object <genexpr> at 0x000002055FC34110>
# Generator tem 104 bytes
# Já o generator, espera pedir por um valor

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# Generator sempre pega um valor por vez.
'''
Uma desvantagem do generator é que diferente da lista, não pode pegar o índice
e nem ver quantos itens tem lá, ele apenas sabe o seu próximo valor.
Ele é uma função que pode pausar.
'''

# sys.getsizeof() mostra o tamanho da lista



