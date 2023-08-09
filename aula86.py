# Empacotamento e desempacotamento de dicionários
# a, b = 1, 2
# a, b = b, a # Desempacotamento  e empacotamento que já vimos
# print(a, b)

#------------------------------------

# !!!!EMPACOTAMENTO!!!!


# pessoa = {
#     'nome': 'Aline',
#     'sobrenome': 'Souza',
# }

# a,b = pessoa
# print(a,b) # Entrega a chaves

# a, b = pessoa.values()
# print(a,b) # Entrega os valores

# a, b = pessoa.items()
# print(a,b) # Entrega os items em forma de tuplas

#------

# (a1,a2), (b1,b2) = pessoa.items() 
# print(a1,a2)
# print(b1,b2) # Entrega os itens completamente, mostrando nome e sobrenome sem tuplas

# Mesma coisa que o de cima ^

# for chave,valor in pessoa.items():
#     print(chave,valor)


#------------------------------------

# !!!!DESEMPACOTAMENTO!!!!

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.3
}

# pessoa_completa = {**pessoa, **dados_pessoa} # Pode continuar adicionando outras keys
#pessoa_completa = {**pessoa, 'nome' : 'josé'} # O nome seria trocado.
# print(pessoa_completa)

#--------------------

# Kwargs

# args e kwargs
# args (já vimos) # Arhumentos não nomeados
# kwargs - keyword arguments (argumentos nomeados)


# ====Empacotando argumentos em kwargs====

def mostro_argumentos_nomeados(*args, **kwargs): # kwargs recebe apenas nomeados
    print('Não nomeados:', args)

    for chave,valor in kwargs.items():
        print(chave,valor)


# mostro_argumentos_nomeados(1,2,3,4 ,nome='Joana', qlq=123) # Caso o argumento não for nomeado, ele irá
# Ser separado em args

# ====Desempacotando argumentos em kwargs====

# pessoa_completa = {**pessoa, **dados_pessoa} 
# pessoa_completa = {**pessoa, 'nome' : 'josé'} 

# mostro_argumentos_nomeados(**pessoa_completa)


configuracoes = {
    'arg1' : 1,
    'arg2' : 2,
    'arg3' : 3,
    'arg4' : 4,
    'arg5' : 5,
}

mostro_argumentos_nomeados(**configuracoes)