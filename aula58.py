"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',') # Támbem pode exibir qual caracter
#Que irá dividir a frase


# for i,frase in enumerate(lista_frases):
#     print(lista_frases[i].strip()) # Corta os espaços do começo
                                    # e do fim.
                                    # L strip, corta o da esquerda
                                    #E o R strip, cortará da direita

# para alterar a lista é necessário o seguinte.
lista_frases = []
for i,frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)

frases_unidas = ', '.join(lista_frases) # Serve para juntar ou unir
print(frases_unidas)


