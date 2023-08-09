"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
'''
A primeira coisa que o "For" faz, é solicitar um ITERADOR do objeto, sendo ele, str,
int, e etc. É como se o string, pedisse ao ITERADOR para  ao ITERÁVEL um objeto 
no caso, uma letra de seu nome. Támbem existe o NEXT usado no ITER, como se o iterável
tivesse pedindo as letras, tanto que, quando o next, é colocado junto ao iter 5 vezes
em uma str que só tem 4 Digitos, acontece um erro chamado "Stop In" dizendo que não
tem mais o que pegar naquela str. E o next, seria um outro módulo. Mas támbem podendo ser uma função.


Iterável :  é um elemento que possui um método chamado 'Iter', um método é algo que vem depois
do ponto, como por exemplo .isdigit() que pode vir depois de um objeto. Os "()" é usado
como uma ação. E utiliza o ITER para retornar um ITERADOR, que vai fazer entregar um elemento
por vez em sua STR

'''
# for ITEM(pode ser qualquer nome como por exemplo "letra") in texto
# Neste momento o For já chama o ITER do iterável solicitando um objeto iterador.
# Tendo o objeto iterador dentro do for, ele irá solicitar NEXT.
texto = 'Luiz' # Iterável seria o str, no caso uma letra por indice.
# iterador = iter(texto) # Iterador pega os dados da iterável, solicitando o método thunderinter

# while True:
#     try:
#         letra = next(iterador)#Ele solicita o próximo valor pro iterador que é o iterador da str.
#         print(letra) # Exibe a LETRA, dos valores exibidos.
#     except StopIteration: # Quando todas as letras forem exibidas o erro ESPECÍFICO será gerado.
#         break # Isso fará com que o  Try caia no except, e por fim quebre o while.

# Esse código do while, faz exatamente isto :

for item in texto:
    print(item)

# E é assim que o for funciona.



# texto = iter('Luiz') #__iter__() # Entrega o objeto iterador
# print(texto.__next__()) # Next chama o próximo valor disponível.
# print(texto.__next__())
# print(next(texto))
# print(next(texto))

#print(texto.__next__()) ou print(next(texto)) ambos causariam um 'Stop interation'



