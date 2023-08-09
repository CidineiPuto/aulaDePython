# Context manager com função - Criando e usando gerenciadores de contexto

from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        archive = open(caminho_arquivo, modo, encoding='utf8')
        yield archive

    except Exception as e:
        print('Ocorreu erro', e)

    finally: # ocorre com erro, ou sem erro.
        print('Fechando arquivo')
        archive.close()

with my_open('Aula157.txt', 'w') as archive:
    archive.write('Linha 1\n')
    archive.write('Linha 2\n')
    archive.write('Linha 3\n')
    print('WITH', archive)