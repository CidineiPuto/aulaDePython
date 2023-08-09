# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.
#
# Ex:
# with open('aula156.txt', 'w') as arquivo:
#     ...

class MyOpen:
    def __init__(self, archive_path, mode):
        self.archive_path = archive_path
        self.mode = mode
        self._arquivo = None
        print('INIT')
    def __enter__(self):
        print('ENTER')
        print('...ABRINDO ARQUIVO...')
        self._arquivo = open(self.archive_path, self.mode, encoding='utf8')
        return self._arquivo
    def __exit__(self, class_exception, exception_, traceback_):
        print('EXIT')
        print('FECHANDO ARQUIVO')
        self._arquivo.close()

        # raise class_exception(*exception_.args).with_traceback(traceback_) # para a execução
        # raise ConnectionError('Não deu para conectar')
        # exception_.add_note('Minha nota')

        # return True # tratei a exceção


with MyOpen('aula156.txt', 'w') as archive:
    archive.write('linha1\n')
    archive.write('linha2\n',123)
    archive.write('linha3\n')
    print('WITH', archive)

"""
retorno do ENTER vai para a variável depois do "as"
"""