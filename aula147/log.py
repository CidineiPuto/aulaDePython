# Abstração · Encapsulamento · Herança · Polimorfismo ·
# pilares da programação orientada a objetos

# abstração
# Herança - é um

from pathlib import Path
LOG_FILE = Path(__file__).parent / 'log.txt'
class Log:
    def _log(self,msg):
        raise NotImplementedError('implimente o método log')
    def log_error(self,msg):
        return  self._log(f'Error: {msg}')
    def log_success(self,msg):
        return  self._log(f'Success: {msg}')


# logfilemixin é um log

class LogFileMixin(Log):
    def _log(self,msg): # assinatura do método
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log:', msg_formatada)

        with open(LOG_FILE, 'a', encoding='utf8') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\r\n')
        


class LogPrintMixin(Log):
    def _log(self,msg): 
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Qualquer coisa')
    lp.log_success('Que legal')
    lf = LogFileMixin()
    lf.log_error('Qualquer coisa')
    lf.log_success('Que legal')
    print(LOG_FILE)




"""
exemplo de abstração : O desenvolvedor não quer que você utilize a classe que está com o 
notimplementederror diretamente, e este erro, serve para avisar que você está usando a super class
a que não pode ser usada. E ela quer que você use a subclass 


se for sobrepor um método, sua assinatura tem que ser idêntica 

fala para outros desenvolvedores que o mixin serve para adicionar novas funcionalidades na sua
herança múltipla, ou seja você vai adicionar coisas dentro da outra classe.
Ela tem uma funcionalidades em que vai adicionar as funcionalidades em outras classes que 
não podem não ser desta família de log.





if __name__ == '__main__':
    l = LogFileMixin()
    l.log('Qualquer coisa')

Se o nome  for main, quer dizer que está executando o módulo diretamente
Então, isto só será executado no arquivo main



    

classe log é uma super, e não há intenção de permitir de usar a classe log. Abstração é abstrair
alguma coisa e tem um método que quer repassar para outras classes. Neste momento, está sendo 
passado por herança

LOG_FILE = Path(__file__).parent # pega o caminho absoluto
__file__ = Caminho do módulo

"""