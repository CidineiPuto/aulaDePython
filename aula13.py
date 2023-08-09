nome = 'Rafael Alves'
altura = 1.77
peso = 69
imc = peso / altura ** 2

linha1 = 'Meu nome é {} tenho {} de altura, eu peso {} e meu imc é {}.'.format(nome,altura,peso, int(imc))

#ou


'f-strings'
linha2 = f'Meu nome é {nome} tenho {altura} de altura, eu {peso:.2f} peso e meu imc é {imc:.2f}'

trocar_linha = True

if trocar_linha == True:
    print(linha2)
else:
    print(linha1)
