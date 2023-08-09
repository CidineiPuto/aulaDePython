# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância ( objeto da classe ) de uma
# classe "callable".
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        retorno = nome, 'está chamando,', self.phone
        return retorno
call1 = CallMe('2342019445')
retorno1 = call1('Jailson penis')
print(*retorno1)