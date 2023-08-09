

#======================Syntaxe======================

# Para que usar o listcomprehenshion = Pegar um iterável e gerar um outro iterável a partir do iterável anterior


# numeros = [1,2,3,4,5]
# novos_numeros = numeros # Isto apenas aponta para esta lista, então se a mesma for mudada, essa támbme será
# assim o novos numeros será alterado


# se tiver valores imutáveis na lista, poderá usar o shallow copy, e copiar o que está naquela lista

# novos_numeros = numeros.copy()

# deep copy é melhor pois  copia tudo, até valores mutáveis.


# novos_numeros = [numero 
#                  for numero in numeros] # para cada numero em numeros 
                                    # Jogue o valor desta variável no novo numeros, em uma nova lista


# Se fosse usado com o for normal, ficaria assim =

# novos_numeros = []

# for numero in numeros:
#     novos_numeros.append(numero)





#======================Utilização======================


#______________map______________
# numbers = [1,2,3,4,5]

# def divisionFn(x,y):
#     return x / y
# def MultiplicationFn(x,y):
#     return x * y
# def PotentiationFn(x,y):
#     return x ** y

# division = [divisionFn(number, 2 )for number in numbers]
# multiplication = [ MultiplicationFn(number, 2)  for number in numbers]
# potentiation = [ PotentiationFn(number, 2) for number in numbers]


# print(numbers)
# print(division)
# print(multiplication)
# print(potentiation)


# Mapeando uma lista para outra lista
# A diferença é que tem um processamento antes de gerar a lista


# Na mapeação os valores podem ser diferente, mas o tamanho da lista sempre será o mesmo


#======================Condicionais======================

#______________Filter______________


# numbers= [1,2,3,4,5,6,7,8,9,10]

# new_numbers = [
#     number for number in numbers if number > 5
# ]  # Numero vai ser igual a cada numero se os numeros forem maior que 5


# def odd(number):
#     return number % 2 != 0
# def pair(number):
#     return number % 2 == 0


# odd_numbers = [number for number in numbers if odd(number)]   # Numeros impares
# pair_numbers =  [number for number in numbers if pair(number) ]


# other_if = [
#     number
#     if number != 6  else 600 # Se o numero não for igual a 6 ele vai ser igual ele mesmo
#     for number in numbers  # Mas se for igual a 6, o número será igual a 600
#     if pair(number)
# ]

# print(numbers)
# print(new_numbers)
# print(odd_numbers)
# print(pair_numbers)
# print(other_if)

#======================linha_e_colunas======================

# for x in range(10 +1):
#     for y in range(5 +1):
#         print(x,y)


# Os dois são iguais

# rows_and_columns = [
#     (x,y) 
#     for x in range(1,11)
#     for y in range(1,6)
# ]

# Caso queira pular o valor pode fazer desta forma = 
'''
rows_and_columns = [
    (x,y) 
    for x in range(1,11)
    for y in range(1,6)
    if x != 2 
]
'''


# rows_and_columns = [
#     (x,y) 
#     if y != 2 else (x * 1000, y * 1000) # Se Y for igual a 2 ele será 2, se não irá exibir o else
#     for x in range(1,11)
#     for y in range(1,6)
#     if x  != 2
# ]
# # Demonstra você tem um forte poder em List comprehendion, podendo alterar os valores o quanto quiser.

# print(rows_and_columns)



#======================String======================

# string = 'Bungas e fanfas'

# # string_alteration = ''.join([letra + '*' for letra in string])  # passa em cada letra e os junta de volta

# cpf = '24924458520'
# cpf_numbers = 3

# cpf_alteration = '.'.join([ 
#     cpf[indice:indice + cpf_numbers] 
#     for indice in range(0, len(cpf), cpf_numbers)
# ])
# print(cpf_alteration)

#======================Listas======================

# names = ['Alice','Bungas','Fafas','Funfas','Sus','Cid']
# new_names = [f'{name[:-1].lower()}{name[-1].upper()}' # irá pegar a lista do 0 ao -1 no caso do inicio ao fim
#                                  # Todavia, por conta do mesmo não pegar o último, todos serão menores, por causa do .lower()
#              # E o outro "name[-1]" irá pegar o numero que foi excluído no caso, o -1 
#              # Lá irá o transformar em maiúsculo através do upper


#               for name in names] # Por ter controle sobre os nomes na lista
# print(new_names) # Pode por exemplo os deixarem minúsculos

# pode ser usado támbem, "name.lower()" letras minúsculas,
# "name.title()" letras com o inicío maiúsculo,
# "name.upper()" Letras com tudo maiúsculo.


#======================Flat map======================

numbers = [[number,number ** 2]for number in range(10)]
flat = [y for x in numbers for y in x] # Ele irá gerar uma lista para o X, e o outro for, fará ele dentro do x
print(numbers)