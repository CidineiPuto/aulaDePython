# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯
class Caneta:
    def __init__(self, cor):
        # private protected
        self.cor = cor
        self.cor_tampa = None



    @property
    def cor(self):
        print('ESTOU NO GETTER')
        return self._cor


    @cor.setter # este setter está ligado diretamente com o init
    def cor(self, valor): # bom para restringir determinada coisa 
        print('ESTOU NO SETTER')
        if valor == 'Rosa':
            raise ValueError('Não aceito cor de viado.')
        self._cor = valor



    @property
    def cor_tampa(self):
        return self._cor_tampa



    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor



# getter -> obter valor
"""
Property por ser um método executa ações, diferente de um atributo que salva ações, e pode 
atribuir um valor específico nelas. E por isso, necessita de algum lugar para salvar  o valor
esse lugar seria o próprio setter.
"""

caneta = Caneta('Azul')
caneta.cor = 'Preto'
caneta.cor_tampa = 'Azul'

print(caneta.cor)
print(caneta.cor_tampa)



"""
Agora que o setter foi feito, pode atribuir um valor no getter colocando por exemplo o 

instancia = Classe('valor')
instancia.atributo = 'outro valor'

agora, o getter irá salvar aquele valor na classe por conta do setter e se perguntarem
por exemplo uma cor de caneta que colocaram como "azul" por conta do setter a caneta sempre 
será azul, até que definem outro valor a ela. O getter, ele PEGA um atributo que já está na 
classe.




NO resumo total, o property apenas retorna um valor, alterado ou não, o setter altera o valor.


Se o setter estiver linkado ao atributo, é possível fazer ele passar no setter logo quando
a pessoa usar 

"class NomeDaClasse:" 
atributo = valor ( ele irá ver este valor logo no setter )
"""