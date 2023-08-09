"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

digite_nome = input('Digite seu nome: ')
digite_idade = (input('Digite sua idade: '))

if not digite_idade:
    print('Desculpe você deixou campos vazios.')
elif not digite_nome:
    print('Você deixou campos vazios.')
else:
    print(f'Seu nome é {digite_nome}.')
    print(f'Seu nome invertido é {digite_nome[::-1]}')
    if ' ' in digite_nome:
        print('Seu nome contém epaços')
    elif ' ' not in digite_nome:
        print('Seu nome não contém espaços')
    print(f'Seu nome tem "{len(digite_nome[::])}" letras.')
    print(f'A primeira letra do seu nome é "{digite_nome[0]}".')
    print(f'A última letra do seu nome é "{digite_nome[len(digite_nome) -1: len(digite_nome)]}".')
    if digite_idade >=  '18':
        print('Você é maior de idade')
    else:
        print('Você é menor de idade.')