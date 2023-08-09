# Variáveis livres + nonlocal (locals, globals)

# print(globals()) # mostra tudo que está definido globalmente
# def fora(x):
    
#     a = x
#     def dentro(): # está função é livre, por estar dentro de outra função
#         print(locals()) # Variavéis que tem acesso dentro da função "dentro"
#         print(dentro.__code__.co_freevars)  # Mostra as funções livres
#         return a # Está é uma variável livre, pois não está definido dentro do escopo desta função
#     return dentro 

# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())


def concatenar(string_inicial):
    valor_final = string_inicial
    def interna(valor_a_concatenar=''):
        nonlocal valor_final # Vai identificar que o valor final é do escopo acima.
        valor_final += valor_a_concatenar # impossível isto dar certo sem usar o "nonlocal"
        return valor_final # Pois o "Valor final" não tem nada definido neste escopo 
    return interna # apenas no escopo anterior, o que deixa ser impossível pegar tal valor

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)


"""
A variável livre, não poste  ser alterado em outro escopo dentro do escopo. A não
ser se for usado "nonlocal" podendo alterar a tal variável
"""