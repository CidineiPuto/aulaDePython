import pprint


produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]


novos_produtos = [
    
    {**produto, 'preco': produto['preco'] * 1.05 }
    if produto['preco']  > 20  else {**produto}  
    for produto in produtos                      
]      


# print(*novos_produtos,sep='\r\n')
def p(v):
    pprint.pprint(v, sort_dicts=False,width=40)  
                                            # (width) largura de linha
                                            # (sort_dicts=) Isto é ordenamento de chaves

# Agora quando for utilizar oquele tipo de dado, é bom se fazer uma função
# print(novos_produtos)
# p(novos_produtos)




# lista = [n for n in range(10) if n < 5] # Irá incluir o numero se o mesmo for menor que 5
# Filtro é diferente de map. 
# Filtro não irá incluir determinada coisa em sua lista se a condição que passar for verdadeira
# Por isso não possui else

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05  }
    if produto['preco']  > 20  else {**produto}  
    for produto in produtos   
    if  (produto['preco'] >= 20 and produto['preco']* 1.05 ) > 10               
]      
'''
se apenas colocar o if produto['preco'] > 10   ele apenas irá pegar o valor antigo
sem fazer cálculo, então para fazer o calculo do for que aconteceu dentro dele, é necessário colocar

    if  (produto['preco'] >= 20 and produto['preco']* 1.05 ) > 10 

se o preço do produto for maior ou igual a 20, e o preço do produtor for multiplicado por 1.05
for maior que 10, o for in deste numero  será executado
'''

p(novos_produtos)