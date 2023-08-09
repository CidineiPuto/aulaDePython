# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.


# O decorador precisa receber a função, decorar com uma função interna, e por fim
# pode alterar a função, caso queira.

# def criar_funcao(func):
#     def interna(*args,**kwargs): # Cria uma nova função
#         print('Vou te decorar')
#         for arg in args: # Daqui já pode começar a alterar sua função decorada.
#              is_string(arg)

#         print(f'O seu resultado foi {resultado}.')
#         resultado = func(*args, **kwargs)
#         print('Ok, agora você foi decorada.')
#         return resultado # Que vai decorar a função anterior
   
#     return interna 
"""
Função decoradora é a função "criar_funcao" o trabalho dela é receber uma função, criar
uma função interna, que não será executada, mas retornada sem execução, para que a pessoa 
utilizando tal função decoradora no momento, possa executar está função e logo executar
a função que está sendo decorada. Na decoração desta função pode fazer alguma coisa, 
podendo executar coisas antes ou depois do resultado de sua função. Podendo adicionar,
remover, restringir e alterar o resultado da função interna.
"""



# def inverte_string(string):
#     return string[::-1]

# def is_string(param):
#     if not isinstance(param, str): # Se a instância NÃO for string
#         raise TypeError('Param deve ser uma string') # Levanta type error dizendo que param
#                                         # Tem que ser string


# inverte_string_chegando_parametro = criar_funcao(inverte_string)
# invertida = inverte_string_chegando_parametro('123')
# print(invertida)



#_________________________________parte2_____________________________________________

# Decoradores são "Syntax Sugar" (Açúcar sintático)


def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna



              # Colocando isto encima de tal função. Ele irá passar a função abaixo
              # para a outra função que fez isto. fazendo esta função, virar a função "interna"
                # É como se a inverte string fosse guardada, lá dentro da "func" 
              # E logo depois sumisse ao executar a interna, invertendo as duas.

@criar_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]
             
def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')





invertida = inverte_string('123')
print(invertida)