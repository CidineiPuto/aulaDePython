
# Exemplo de uso dos sets

letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('Bungas, você finalmente encontrou a letra misteriosa')
        break


    print(letras)
 