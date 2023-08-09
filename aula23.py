# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  R a f a e l
# -6-5-4-3-2-1
#nome = 'Rafael'
#print(nome[2])
#print(nome[-4])
#print('a' in nome)
#print('afa' in nome)
#print('fo' in nome)
#print(10 * '-')
#print('fs'not in nome)
#print('zero'not in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que quer encontrar no seu nome: ')

if encontrar in nome: 
    print(f'{encontrar} está em {nome}.')
else:
    print(f'{encontrar} não está em {nome}.')