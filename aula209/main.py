# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path

from PyPDF2 import PdfMerger, PdfReader, PdfWriter

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / "pdfs_originais"
PASTA_NOVA = PASTA_RAIZ / "arquivos_novos"
RELATORIO_BACEN = PASTA_ORIGINAIS / "R20230210.pdf"


PASTA_NOVA.mkdir(exist_ok=True)
reader = PdfReader(RELATORIO_BACEN)

# print(len(reader.pages))

# for page in reader.pages:
#     print(page)
#     print()

page1 = reader.pages[0]
imagem1 = page1.images[0]

# print(page1.extract_text())  # Consegue extrair e ler os textos um pouco.
# with open(PASTA_NOVA / imagem1.name, "wb") as fp:
#     fp.write(imagem1.data)
# wb significa, "writing bytes" caso o arquivo esteja em bytes

# writer = PdfWriter()


# with open(PASTA_NOVA / "NOVO_PDF.pdf", "wb") as archive:
#     for page in reader.pages:
#         writer.add_page(page)

#     writer.write(archive)

"""
Irá abrir um NOVO_PDF, irá abrir o arquivo, vai adicionar pagina por pagina,
e quando terminar o arquivo será escrito

Porém, se formos querer separar e fazer 2 páginas de pdf distintas, faremos o
seguinte;
"""

for i, page in enumerate(reader.pages):  # Enumerate é usado para fazer núm
    writer = PdfWriter()
    with open(PASTA_NOVA / f"page{i}.pdf", "wb") as archive:
        writer.add_page(page)
        writer.write(archive)

"""
O PdfMerger é usado exclusivamente para juntarmos dois ou mais, pdf em apenas
um pdf.
"""


files = [  # Aqui colocamos a pasta de maneira invertida.
    PASTA_NOVA / "page1.pdf",
    PASTA_NOVA / "page0.pdf",
]

merger = PdfMerger()
for file in files:
    merger.append(file)

# Nessa parte, pode usar o merger para criar o arquivo.

merger.write(PASTA_NOVA / "MERGED.pdf")
merger.close()  # É extremamente importante lembrar de fechar.
