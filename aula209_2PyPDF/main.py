from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import AnnotationBuilder

ROOT_FOLDER = Path(__file__).parent
ORIGINAL_FOLDER = ROOT_FOLDER / "original_pdf"
NEW_FOLDER = ROOT_FOLDER / "new_pdfs"
BACEN_REPORT = ORIGINAL_FOLDER / "R20230210.pdf"

NEW_FOLDER.mkdir(exist_ok=True)

reader_bacen = PdfReader(BACEN_REPORT)
first_page = reader_bacen.pages[0]
second_page = reader_bacen.pages[1]
writer = PdfWriter()

"""
Usando o "visitante", você pode usar o "visitor" para controlar a parte do
texto que você quer processar e extrair.

A função que será usada, terá 5 argumentos, matriz de transformação atual
( current transformation matrix ) = cm, matriz do texto (text matrix) = tm,
dicionário da fonte (font dictionary) = fontDict, tamanho da fonte (fontsize) =
fontsize, e é claro, o texto(text) = text.

Na maioria dos casos, as coordenadas x e y, da posição atual é reprensentadas
pelo index 4 e 5 da transformação da matriz atual.

O dicionário da fonte pode ter casos de ser None caso a fonte for desconhecida.
Se não for "None" a Key, "/BaseFont" terá o valor "/Arial,Bold".

Os argumentos que irão ter na função de visitante_operando_antes, ou
visitor_operand_before, terá os argumentos; operando (operando),
operand_arguments (Operando argumentos.), current_transformation_matrix
(matriz de transformação atual) e text_matrix (matriz_do_texto)
"""

# Exemplo 1 Ignore header and footer

# parts = []


# def visitor_body(text, cm, tm, fontDict, fontsize):
#     y = tm[4]
#     if y > 50 and y < 720:
#         parts.append(text)


# first_page.extract_text(visitor_text=visitor_body)
# text_body = "".join(parts)
# print(text_body)

# with open(NEW_FOLDER / "NEW_PDF.pdf", "wb") as archive:
#     for page in reader_bacen.pages:
#         writer.add_page(page)

#         writer.write(archive)


# with open(NEW_FOLDER / "page1rotate.pdf", "wb") as fp:
#     writer.add_page(first_page.rotate(90))  # Roda a página em 90 graus.
#     writer.write(fp)

# with open(NEW_FOLDER / "page2half_size.pdf", "wb") as sp:
#     second_page.mediabox.upper_right = (  # type: ignore
#         second_page.mediabox.right / 2,
#         second_page.mediabox.top / 2,
#     )
#     writer.add_page(second_page)
#     writer.write(sp)


with open(NEW_FOLDER / "page1annotation.pdf", "wb") as fp:
    writer.add_page(first_page)
    annotation = AnnotationBuilder.free_text(
        "Hello World\nThis is the second line!",
        rect=(50, 550, 200, 650),
        font="Arial",
        bold=True,
        italic=True,
        font_size="20pt",
        font_color="00ff00",
        border_color="0000ff",
        background_color="cdcdcd",
    )
    writer.add_annotation(page_number=-1, annotation=annotation)
    writer.write(fp)
