# Yield from

def gen1():
    print('COMEÇOU GEN 1')
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    print('ACABOU GEN 1')

# def gen2():
#     yield from gen1() # Começa já do "gen1"
#     yield 6
#     yield 7
#     yield 8

# Assim só precisa pegar o "gen2"

# g = gen2()

# for numero in g:
#     print(numero)

# ____________________________________________________________________


# Mas para ser feito de maneira mais dinâmica apenas fazer isto :

def gen2(gen=None):
    print('COMEÇOU GEN 2')
    # yield from gen() # Irá começar da função que selecionar # támbem pode ser feito assim : yield from gen
    if gen is not None:
        yield from gen
    yield 6
    yield 7
    yield 8
    print('ACABOU GEN 2')

def gen3():
    print('COMEÇOU GEN 3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN 3')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()

for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)
print()