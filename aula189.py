# pathlib

from pathlib import Path

# from shutil import rmtree

print(97 * "#")


caminho_projeto = Path()
# print(f'Caminho absoluto "{caminho_projeto.absolute()}"')

# print()

caminho_arquivo = Path(__file__)
# print(f'Caminho do arquivo "{caminho_arquivo}"')

# print()

# print(f'Caminho do módulo "{caminho_arquivo.parent}"')

# print()

# print(f'Caminho da pasta "{caminho_arquivo.parent.parent}"')
# .parent = pasta acima

ideias = caminho_arquivo.parent / "ideias"
# print(ideias / "arquivos.txt")


# arquivo = Path.home() / "OneDrive" / "Área de Trabalho" / "arquivo.txt"
# arquivo.touch()  # Cria arquivo
# arquivo.write_text("Hello world")
# print(arquivo.read_text())
# arquivo.unlink()  # Apaga arquivo


archive_path = Path.home() / "OneDrive" / "Área de Trabalho" / "archive.txt"

# archive_path.write_text("")
# with archive_path.open("a+", encoding="utf8") as file:
#     file.write("Uma linha\n")
#     file.write("Duas linha\n")
#     file.write("Três linha\n")

# print(archive_path.read_text())

caminho_pasta = Path.home() / "OneDrive" / "Área de Trabalho" / "python  legal"
print(97 * "#")
caminho_pasta.mkdir(exist_ok=True)
sub_pasta = caminho_pasta / "subpasta"
sub_pasta.mkdir(exist_ok=True)
outro_arquivo = sub_pasta / "arquivo.txt"
outro_arquivo.touch()
outro_arquivo.write_text("siii")  # escreve

# caminho_pasta.rmdir()

files = caminho_pasta / "files"
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f"file_{i}.txt"

    if file.exists():
        file.unlink()
    else:
        file.touch()
    with file.open("a+", encoding="utf8") as text_file:
        text_file.write("Hello World")
        text_file.write(f"file_{i}.txt")


def rmtree(root: Path, remove_root: bool = True):
    for file in root.glob("*"):
        if file.is_dir():
            print("DIR: ", file)
            rmtree(file)
            file.rmdir()
        else:
            print("FILE: ", file)
            file.unlink()

    if remove_root:
        root.rmdir()

    # if remove_root:
    #     root.rmdir()


# rmtree(caminho_pasta) # com shutil

# isfile = Checa se é um arquivo
# isdir = checa se é um diretório
# exists = Checa se existe
