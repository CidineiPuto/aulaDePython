# requests para requisições HTTP.
# Tutorial -> https://youtu.be/Qd8JT0bnJGs
import requests

# http:// -> está rodando na porta 80
# https:// -> está rodando na porta 443

# Se não informado a porta, uma das duas acima serão usadas.


"""
O protócolo HTTP como dito, é algo relacionado ao cliente e servidor, mas agora
que não há um navegador, o cliente seria o código, e o servidor o site que
está sendo acessado.

Como dito antes na aula 201;

"faz uma requisição ao servidor"

O HTTP faz uma REQUISIÇÃO ao servidor, aí que se relaciona com o módulo
request. E o servidor responde.
"""

url = "http://localhost:3333"
response = requests.get(url)
# Quer uma resposta, em que o request irá fazer a requisição, e o método é
# get.

# print(response.status_code) Pega o código de status.
# print(response.headers) Pega os cabeçalhos.
# print(response.content) Desta forma, o conteúdo fica na resposta em bytes
# print(response.text) E este é direcionado para texto.
print(response.json())  # Este é caso a resposta vier em texto.
