# senha_salva = '1234567'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print('Aquele laço acima pode ter repetições infinitas.')

texto = 'python'
novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(f'{novo_texto}*')


