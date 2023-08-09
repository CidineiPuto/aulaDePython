# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

# def generator(n=0):
#     yield 1  # Pausa a execução para chamar ela é necessário usar "next()" e chamar o próximo
#     print('continuando...') 
#     yield 2 # Pausar
#     print('mais uma vez')
#     yield 3
#     print('Vou terminar ')
#     return('acabou')

# # Toda função que possui o yield é uma generator function

# gen = generator(n=0)

# # print(next(gen))
# # print(next(gen))

# for n in gen:
#     print(n)

def generator(n=0,maximum=10):
    while True:
        yield  n
        n += 1
        
        if n >= maximum:
            return
# Isto seria um "Generator"
# range feito na mão, além de ser possível chamar com o next.

gen = generator(n=5, maximum=100)


for n in gen:
    print(n)