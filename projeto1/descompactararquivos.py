from pathlib import Path
from zipfile import ZipFile

RAIZ_ARQUIVO = Path.home() / "OneDrive" / "Área de Trabalho" / "jogos"

CAMINHO_COMPACTADO = RAIZ_ARQUIVO / "CharmStudies-1.1.5-pc.zip"
CAMINHO_DESCOMPACTADO = RAIZ_ARQUIVO / "Caminho_Para_O_Jogo"
print(CAMINHO_COMPACTADO)

with ZipFile(CAMINHO_COMPACTADO, "r") as zip:
    for arquivo in zip.namelist():
        print(arquivo)


# with ZipFile(CAMINHO_COMPACTADO, "r") as zip:
# zip.extractall(CAMINHO_DESCOMPACTADO)
