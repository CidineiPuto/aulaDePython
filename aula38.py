"""
iterando strings com while
"""

#       0 1 2 3 4 5 6 7 8 9 10
nome = input('Escreva um nome: ')  # iteráveis
#      -11-10-9-8-7-6-5-4-3-2-1



#-------------------------
'''
while indice < len(nome):
    print(nome[indice],(indice))   
    indice += 1  
'''
#-------------------------
indice = 0
novo_nome = ''


while indice < len(nome):
     print(nome[indice],indice )
     letra = (nome[indice]) 
     novo_nome +=  f'*{letra}'
     indice += 1


novo_nome += '*'


print(f'\r\n{novo_nome}')
print(f'{novo_nome[::-1]}\r\n')



