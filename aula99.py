# PARTE 1 ___________________________________________________________________________________

# (Parte1) try e except para tratar exceções



# try:
#     a = 18
#     b = 0
#     print(b[0])
#     print('Linha 1'[100])
#     c = a / b
#     print('Linha 2') # Não será executado pois o erro já aconteceu, e já pulou para except
# except ZeroDivisionError: # O erro é uma classe
#     print('Dividiu por zero.')
# except NameError:
#     print('Algum nome não foi definido')
# except (IndexError, TypeError): # Consegue pegar dois erros de uma vez
#     print('Erro de index ou type error.')
# except Exception: # Não existe outro erro, ela trata qualquer outro erro.
#     print('Erro desconhecido.')

# print('Continuar')


# (Parte 2) try e except para tratar exceções
# a = 18
# b = 0
# c = a / b

# PARTE 2 ___________________________________________________________________________________

try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e : 
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Algum nome não foi definido')
except (IndexError, TypeError) as error: # Irá definir a instância do  erro em uma variável
    print('Erro de index ou type error.')
    print('MSG:', error) # Mostrará a mensagem do erro 
    print('MSG:', error.__class__.__name__) # Irá pegar a classe do erro, e da classe irá tirar o nome
except Exception: 
    print('Erro desconhecido.')

# Istância = Objeto do erro