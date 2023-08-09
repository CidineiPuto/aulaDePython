import json

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('aula124.json', 'w', encoding='utf8') as arquivo: # cria um arquivo json
    json.dump(
            pessoa, 
            arquivo, 
            ensure_ascii=False,
            indent=2
            )
                            #    ensure_ascii coloca os acentos certo.
                            #    ident ajuda o dado a ficar formatado


"""
json é simples e não suporta coisas específicas, como métodos, funções set e etc.
"""



# Voltando os dados json para dentro do programa python______________________________________

with open('aula124.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa)) 
    print(pessoa['nome'])

# quando puxa o arquivo de json ele irá convertar os valores e etc. Nos valores de acordo com,
# o da linguagem.