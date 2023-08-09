# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.

# import json
import locale
import string
from datetime import datetime
from pathlib import Path

CAMINHO_DO_ARQUIVO = Path(__file__).parent / "aula195.txt"

locale.setlocale(locale.LC_ALL, "")


def converte_para_brl(numero: float) -> str:
    brl = "R$ " + locale.currency(numero, symbol=False, grouping=True)
    return brl


data = datetime(2022, 12, 28)
dados = dict(
    nome="João",
    valor=converte_para_brl(1_234_456),
    data=data.strftime("%d/%m/%Y"),
    empresa="O.M.",
    telefone="+55 (11) 7890-5432",
)

# _____________________________________________________________________________
# texto = """
# Prezado(a) $nome,

# Informamos que sua mensalidade será cobrada no valor de ${valor} no dia
# $data. Caso deseje cancelar o serviço, entre em contato com a $empresa
# pelo $telefone.

# Atenciosamente,

# ${empresa},
# Abraços
# """

# template = string.Template(texto)
# print(template.substitute(dados))
# ou
# print(template.safe_substitute(dados))
# _____________________________________________________________________________


class MyTemplate(string.Template):
    delimiter = "%"  # muda o delimitador, obrigando a pessoa a usar % ao invés
    # de $


with open(CAMINHO_DO_ARQUIVO, "r", encoding="utf8") as arquivo:
    texto = arquivo.read()
    template = MyTemplate(texto)  # ou string.Template(texto)
    print(template.substitute(dados))
