# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

# import json

# save_peoples = []

# class Pessoa:
#     def __init__(self,nome,idade, cpf):
#         self.nome = nome
#         self.idade = idade
#         self.cpf = cpf

    
#     def save_peoples_in_json(self):
#         peoples_saved = save_peoples.append(self.__dict__)
#         return peoples_saved
    
# ARCHIVE_PATH = 'aula135.json'

# p1 = Pessoa('João',16, '01163369004')
# p2 = Pessoa('Billy',16,'65495787951')
# p3 = Pessoa('Kayo',17,'20730896072')
# p4 = Pessoa('Marcos',16,'44104769398')
# p5 = Pessoa('Rafael',15,'09786875230')
# p6 = Pessoa('Gustavo',16,'48620965140')

# p1.save_peoples_in_json()
# p2.save_peoples_in_json()
# p3.save_peoples_in_json()
# p4.save_peoples_in_json()
# p5.save_peoples_in_json()
# p6.save_peoples_in_json()



# with open(ARCHIVE_PATH, 'w', encoding='utf8') as archive:
#     json.dump(
#     save_peoples,
#     archive,
#     ensure_ascii=False,
#     indent=2
#     )


# professor resolução

import json

CAMINHO_ARQUIVO = 'aula135.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)
bd = [vars(p1), p2.__dict__, vars(p3)]


def fazer_dump(): # é usado para ele não ser executado junto com a leitura após sua importação na segunda função
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)


if __name__ == '__main__': # se caso este for o arquivo "main" execute o dump
    print('ELE É O __main__')
    fazer_dump()




"""
Curiosidades sobre convenções de nomes
Como você viu na aula anterior, usamos certas convenções para nomes de variáveis, 
funções, classes e assim por diante. Essas convenções tem um nome que podemos usar 
para nos referir ao modo como estamos
nomeando determinados objetos em nosso programa: PascalCase, camelCase e snake_case.

PascalCase - significa que todas as palavras iniciam com letra maiúscula e nada é usado para 
separá-las, como em: MinhaClasse, Classe, MeuObjeto, MeuProgramaMuitoLegal. 
Essa á a convenção utilizada para classes em Python;

camelCase - a única diferença de camelCase para PascalCase é a primeira letra. 
Em camelCase a primeira letra sempre será minúscula e o restante das palavras 
deverá iniciar com letra maiúscula. Como em: minhaFuncao, funcaoDeSoma, etc... 
Essa conversão não é usada em Python (apesar de eu confundir as duas e às vezes 
acabar chamando camelCase de PascalCase ou vice-versa, mas agora você sabe a diferença);

snake_case - este é o padrão usado em Python para definir qualquer coisa que não for uma classe. Todas as letras 
serão minúsculas e separadas por um underline, como em: minha_variavel, funcao_legal, soma.

Os padrões usados em Python são: snake_case para qualquer coisa e PascalCase para classes.
"""