# Decoradores com parâmetros
def fabrica_de_decoradores(a=None,b=None,c=None): # Pega os parâmetros do DECORADOR
    def fabrica_de_funcoes(func): # Fabrica de função # pega a função, no caso é o decorador
            print('Decoradora 1')

            def aninhada(*args, **kwargs): # Cria uma função interna # é a função que será executada
                print('Pârametros do decorador, ', a, b, c)
                print('Aninhada')
                res = func(*args, **kwargs) # Executa a função SOMA guardada na memória passando pra ela
                # Os args e kwargs desempacotados, retornandos os resultados
        
                return res # Pode alterar o resultado           
            return aninhada
    return fabrica_de_funcoes


@fabrica_de_decoradores(1,2,3)
def soma(x,y):
      return x + y


decoradora =  fabrica_de_decoradores()
multiplica =(lambda x,y: x*y)

dez_mais_cinco = soma(10, 5) # Quando for executada, a aninhada támbem é.
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)







# def blablabla(a,b,c):
#       print(a,b,c)
#       return decoradora
# @blablabla(1,2,3) # a partir do momento em que você cria a função e executa tal função, 
             # O python tenta a executar como um decorador
# def soma(x, y):
#     return x + y



