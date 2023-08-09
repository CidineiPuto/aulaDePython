# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}

# s1 = set('Luiz')
# print(s1) # Quando se escreve sem {} ele irá deixar as letras aleatórias na string
# s2 = set()  # vazio
# print(s2, type(s2))
# s3 = {'Luiz', 1, 2, 3}  # com dados
# print(s3)
#______________________________________________________________________________________

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis; # Porém é aceito tuplas como exemplo s1 = {(134,)}
# - Seus valores serão sempre únicos;
# - não tem índexes; # Quer dizer que não tem indices
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Demonstração sobre os digitos repetidos

# s1 = { 1, 2, 3,3,3,3,2,1}
# print(s1)

# Método para tirar digitos repetidos
# l1 = [1,2,3,3,3,3,3,3,1,2,2,2,3]
# s1 = set(l1)
# l2 = list(s1)
# print(l2)

# Usando IN no set

# s1 = {1,2,3}
# print(3 in s1)
# print(3 not in s1)
# print(4 in s1)
# print(4 not in s1)

# For  em set
# s1 = {1, 2, 3}
# for numero in s1:
#     print(numero)
#______________________________________________________________________________________

# Métodos úteis:
# add, update, clear, discard

s1 = set()

# -----add------ 

# s1.add('Bungas')
# s1.add(69)
# print(s1)

# -----update------ 

# s1.update('Hello World') # Se for feito assim, os digitos serão aleatórios
# s1.update(('Hello World',1,2,3,4,5)) # Mas se for assim, e adicionar valores na frente não serão mais                                                                                                   

# -----clear------

# s1 = {1,2,3,4,5,5}
# s1.clear()
# print(s1)

# -----discard------

# s1 = {1,2,3,4,5,5}
# s1.discard(1)
# s1.discard(2)
# print(s1)

#______________________________________________________________________________________

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos


s1 = {1,2,3}
s2 = {1,3,4,5}

# ----- union -----

# s3 = s1 | s2
# print(s3)

# ----- intersection -----

# s3 = s1 & s2
# print(s3)

# ----- difference -----

# s3 = s1 - s2 # ou # s3 = s2 - s1
# print(s3)

# ----- symmetric difference -----

s3 = s1 ^ s2 # Itens que só estão em um conjunto apenas.
print(s3)

lista1 = [1,2,3]

lista1.append(0)

print(lista1)