"""
Json é basicamente uma estrutura de dados que foi criada para que você transporte
ou salve dados. 
""" 
"""
Dados que podem ter no Json são  bolean, number(int ou float), null(nada), string,
array ("[]") são como se fosse uma lista, e por fim um "{}" igual aos objetos(dictionary)
"""


#Exemplo1 de arquivo json :

"""
[
    {"name": "Luiz", "lasName": "Miranda", "age": "22"},
    {"name": "Rafael", "lasName": "Alves", "age": "15"},
    {"name": "João", "lasName": "Henrique", "age": "16"},
    {"name": "Billy", "lasName": "Paul", "age": "16"},
    {"name": "Kayo", "lasName": "Gabriel", "age": "17"}
]

"""

# Exemplo2 de arquivo json :

# {
#     "name": "Luiz", 
#     "lasName": "Miranda", 
#     "age": "22",
#     "adresses": [
#         {"line1": "av. brasil"},
#         {"line2": "av. amapá"}
#     ]
# }






import json
import os


# pessoas = [
#     {
#     "nome": 'maria',
#     "sobrenome": 'santos',
#     "idade": 25,
#     "ativo": False,
#     "notas": ['A', 'A+'],
#     "telefones": {
#         "residencial": "00 0000-0000",
#         "celular": "00 0000-0000",
#     }
#     },
# {
#     "nome": 'Joana',
#     "sobrenome": 'Moreira',
#     "idade": 32,
#     "ativo": True,
#     "notas": ['B', 'A'],
#     "telefones": {
#         "residencial": "00 0000-0000",
#         "celular": "00 0000-0000",
#     }
#     },   
# ]

# BASE_DIR = os.path.dirname(__file__) # Criação do caminho completo do arquivo aonde está
# SAVE_TO = os.path.join(BASE_DIR, 'arquivo-python.json') # Este seria o arquivo
# # Irá ter o caminho (BASE_DIR) mais o nome do arquivo ^


# with open(SAVE_TO, 'w') as file: # File é o nome do arquivo
#      json.dump(pessoas, file, indent=2)  # salva o dictionary como json file.


# print(json.dumps(pessoas, indent=2))


# Carregar de fora para dentro o json___________________________________________________________

BASE_DIR = os.path.dirname(__file__) 
JSON_FILE = os.path.join(BASE_DIR, 'arquivo-python.json') 

# with open(JSON_FILE, 'r') as file:
#     pessoas = json.load(file)
    
#     for pessoa in pessoas:
#         print(pessoa['nome'], pessoa['notas'])


# with open(JSON_FILE, 'r') as file:
#     pessoas = json.load(file)
#     print(json.dumps(pessoas)) # Converte ele em dumps e o printa.


json_string = '''
[{"nome": "maria", "sobrenome": "santos", "idade": 25, "ativo": false, "notas": ["A", "A+"], "telefones": {"residencial": "00 0000-0000", "celular": "00 0000-0000"}}, {"nome": "Joana", "sobrenome": "Moreira", "idade": 32, "ativo": true, "notas": ["B", "A"], "telefones": {"residencial": "00 0000-0000", "celular": "00 0000-0000"}}]
''' # aqui foi usado para pegar a string

pessoas = json.loads(json_string) # Carrega as "pessoas" em formato de string
                        # ele lê isto, entende, e converte em uma lista python.

for pessoa in pessoas:
    print(pessoa['nome'])
# faz o for na lista e pega os dados de voltas

"""
 load = carrega um arquivo.
 dump = joga para fora.
 json.dump = O dump normal, em um arquivo.
 json.dumps = Seria o dump de uma string, fazendo dump em uma string.
 ident = Formata a string
"""