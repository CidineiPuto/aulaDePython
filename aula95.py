# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'upper'
# print(dir(string)) # Vai trazer todos os atribudos/nomes definidos no método

if hasattr(string, 'upper'): # Irá ver se tal método estará na STR 
    print('Existe Upper')
    print(getattr(string, metodo)()) # Executa um método que está dentro do módulo
else:
    print('Não existe o método', metodo)