'''
Flag (Bandeira) - Marcar um local
none = Não valor
is e is not = É ou não é (tipo, valor, identidade)
id = identidade
'''
# ID

# v1 = 'a'
# v2 = 'b'
# print(id(v1))
# print(id(v2))

# Flag (Is, Is not, None)

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça nada')

if passou_no_if is None:
    print('Não passou no if')

else:
    print('Passou no if')

# print(passou_no_if, passou_no_if is None)
# print(passou_no_if, passou_no_if is not None)

'''
O 'is' seria o '==' mas por estar sendo usado no none
o certo seria usar is, então, ele pergunta
se a condicao "passou no if" está definida como None.
'''
