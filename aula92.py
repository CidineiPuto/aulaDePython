# Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

# for chave,valor in produto.items():
#     print(chave,valor)

dc = {
    chave: valor
    # if isinstance(valor, str) else valor # Se for string o valor será maiúsculo, se não, ele apenas será o proprio valor
    # ou 
    if isinstance(valor,(int,float))  else valor.upper()


    for chave, valor 
    in produto.items() 
    # if chave == 'categoria' # Só vai inclur a chave categoria
    if chave != 'categoria' # Só categoria não será incluido

} # Agora, poderá mudar os valores 







lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]

dc = {
    chave: valor 
    for chave, valor in
    lista
} # Pode transformar listas que parecem dictionary em dictionary

print(dc)
print(dict(lista)) # Transforma em dict



s1 = { 2 ** i  for i in range(10)} # Cria um set com 10 valores
print(s1)