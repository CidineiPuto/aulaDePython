# Variáveis de ambiente com Python
# Para variáveis de ambiente
# Windows PS: $env:VARIAVEL="VALOR" | dir env:
# Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL
# Para obter o valor das variáveis de ambiente
# os.getenv ou os.environ['VARIAVEL']
# Para configurar variáveis de ambiente
# os.environ['VARIAVEL'] = 'valor'
# Ou usando python-dotenv e o arquivo .env
# pip install python-dotenv
# from dotenv import load_dotenv
# load_dotenv()
# https://pypi.org/project/python-dotenv/
# OBS.: sempre lembre-se de criar um .env-example
# NUNCA mande seu ".env" para ninguém.
# _________________________________________________________________________
# import os

# senha = os.getenv("SENHA")
# print(senha)  # por algum motivo não funciona no pc

import os

from dotenv import load_dotenv  # type: ignore

load_dotenv()  # necessário ser usado no inicío

# print(os.environ)
print(os.getenv("BD_PASSWORD"))


"""
Os que estão como .env-example, é para tirar o "example" e assim transformar
ele em um .env, fazendo alterações no que a pessoa está pedindo para
alterar.
"""


"""
Explicação do dotenv
https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/35508398#questions
"""
