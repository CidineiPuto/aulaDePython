# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]


# novos_produtos = [
#     produto['preco']
#     for produto in produtos   # Mapeando os dados, e os criando com o mesmo tanto de iteráveis
# ]

# print(*novos_produtos,sep='\r\n') # ele vai tirar a variavel dos colchetes e pular a linha

# novos_produtos = [
#     {'nome':produto ['nome'], 'preco': produto['preco']} # Irá criar um novo dicionário usando o anteriro
#     for produto in produtos
# ]
# print(*novos_produtos,sep='\r\n')

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05 }  # irá pegar o dicionário de antes e o mudar  
    if produto['preco']  > 20  else {**produto}  # O if tem que vir atrás do for, para repetir a lista
    for produto in produtos                      # Se o preço do produto for maior que 20
                                            # O valor será aumentado em 5%
]
print(*novos_produtos,sep='\r\n')

'''
O if está funcionando de baixo pra cima, então se o valor de produto for maior que 20
o valor vai ser aumentado. Se não será o mesmo, e outra coisa, o if está na frente do codigo
pois ele diz o que acontecerá se o if for verdadeiro, se não o else será executado,
e ele só será desempacotado. Por ser valores com nomes, o certo seria usar '**' ou melhor
Kwargs
'''