for i in range(10): # Pega item por item do Range de 0 a 9, para pegar 10 terá que colocar +1
    if i == 2:  # Se o I for 2 ele irá voltar no começo do while. 
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break # Ele irá quebrar no 8 e fará o Else não executar, quebrando o For.

    for j in range(1, 3): # É como se o J for as colunas, então irá ter 2 colunas neste instante.
        print(i, j) # Irá exibir o I ao lado do J
else:
    print('For completo com sucesso!')


# Em resumo, é idêntico ao while, você apenas não irá controlar a iteração.