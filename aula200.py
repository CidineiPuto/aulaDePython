# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html

# para passar um argumento
# python (nome do módulo).py (argumentos)
# isso também serve para executar um argumento

# ex:
"""
python aula200.py -b "Wilson" -b "Susa"
python aula200.py -v "lalaus"
"""

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    "-b",
    "--basic",
    help='Mostra "Hello world" na tela.',
    # type=str,
    metavar="STRING",
    # default="Hello world",  # Add um valor default
    required=False,  # Se for true, passar um valor para b, é obrigatório
    # nargs="+",  # Cria uma lista de coisas, agora pode passar mais argumentos
    # isso caso o nargs for "+".
    action="append",  # O "append" é um tipo de lista, permite adicionar os
    # elementos de forma "-b 1 -b 2 -b 3"
)
parser.add_argument(
    "-v",
    "--verbose",
    help="Mostra logs.",
    action="store-true",  # Se for recebido ele diz que é true, se não, diz
    # que é false.
)
args = parser.parse_args()  # Faz o parse, do argumento "-b(-basic)"

if args.basic is None:
    print("Você não passou o valor de basic.")
    print(args.basic)
else:
    print("O valor de basic é", args.basic)
print(args.v)
"""
Se for usar o argument parser, é recomendado quando você precisa/quer, algo bem
mais robusto em seu script. Com coisas rápidas é bom usar o sys argv.

Existe várias coisas com que pode se fazer com argumentparser.


Fazendo desta forma

parser.add_argument("-b")
args = parser.parse_args()
print(args.b)

É bom, pois está checando a chave "-b" e um valor, vendo se a pessoa passou
alguma chave e algum valor, caso você coloque "python aula200.py -b".

Agora, o elemento dá erro, pois ele espera um argumento mais verboso "--basic"
isso quando você coloca o elemento assim;

parser.add_argument("-b", "--basic")


Caso não saiba usar o script, escreva "--help", ou "-h".

O "BASIC" é o que você quer passar para seu arg, se passarmos;


parser.add_argument(
    "-b",
    "--basic",
    help='Mostra "Hello world" na tela.',
    type=str,
    metavar="STRING",
)


-b STRING, --basic STRING
                        Mostra "Hello world" na tela.

Falamos que o -b mostra "Hello world" na tela, é um tipo str, e o metavar, quer
dizer o que devemos passar, que no caso seria uma str qualquer, por isso está
"STRING".

"""
