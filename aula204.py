# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4
import re

import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:3333"
response = requests.get(url)  # ler os dados da url
raw_html = response.text
bytes_html = response.content
parsed_html = BeautifulSoup(bytes_html, "html.parser", from_encoding="utf-8")
# Converte a string para objetos python (códigos)

# if parsed_html.title is not None:
#     print(parsed_html.title.text)

top_jobs_heading = parsed_html.select_one("#intro > div > div > article > h2")
# select é para escolher mais de uma coisa, select_one, escolhe apenas uma.

if top_jobs_heading is not None:
    article = top_jobs_heading.parent  # pega o pai do elemento
    if article is not None:
        for p in article.select("p"):  # Select neste momento seleciona todas
            # as tags p no article.
            print(re.sub(r"\s{1,}", " ", p.text).strip())
            # todos espaços maior que 1 espaço substitui para apenas 1 espaço.
            # O strip tira o espaço do início e do fim do texto.


"""
Quando irá selecionar algo em um html, copiar alguma coisa, vá em inspecionar,
selecione o que você quer com o botão direito, e vá em "copy selector" para
copiar o seletor css do mesmo.
"""


"""
ANOTAÇÃO DO PROFESSOR:

Adicionando "encoding" no BeautifulSoup 4 para evitar problemas com caracteres
Uma coisa comum de ocorrer quando trabalhamos com o bs4.BeautifulSoup. é
problemas com caracteres. Isso ocorre devido a uma falha na detecção do
encoding.

Eu explico mais sobre codificação de caracteres no artigo abaixo:

https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/

Caso queira mudar a codificação de caracteres, envie os bytes diretamente para
o BeautifulSoup e passe o valor da codificação de caracteres no atributo
"from_encoding". Exemplo (para utf-8):

BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')
Perceba que troquei "response.text" para "response.content" para obter os
bytes ao invés da string.

Nesse caso, nosso código completo das aulas anteriores ficaria assim:

import re

import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:3333/'
response = requests.get(url)
bytes_html = response.content
parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding='utf-8')

top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')

if top_jobs_heading is not None:
    article = top_jobs_heading.parent

    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{1,}', ' ', p.text).strip())

Assumindo que a codificação de caracteres da página é utf-8.

Você pode detectar isso no HTML pela tag meta charset dentro da <head>:

<meta charset="UTF-8">
"""
