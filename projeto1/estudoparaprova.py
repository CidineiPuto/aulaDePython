def questões(perguntas):
    qtd_acertos = 0
    for pergunta in perguntas:
        print('Pergunta:', pergunta['questão'])
        print()

        opcoes = pergunta['opção']
        for i, opcao in enumerate(opcoes):
            print(f'{i})', opcao) 
        

        print()
        escolha = input('Escolha uma opção: ')
        acertou = False
        escolha_int = None
        qtd_opcoes = len(opcoes)
        if escolha.isdigit():
            escolha_int = int(escolha)

        if escolha_int is not None:
            if escolha_int >= 0 and escolha_int < qtd_opcoes:
                if opcoes[escolha_int] == pergunta['resposta']:
                    acertou = True
        print()
        if acertou:
            qtd_acertos += 1
            print('Acertou 👍')
        else:
            print('Errou ❌')

        print()
    return print(f'Sua quantidade de acertos foi "{qtd_acertos}".\n')
 


perguntas = [
    {
        'questão': 'Quanto é 2+2 ?',
        'opção': ['bungas', '2', '4', '5'],
        'resposta': '4',
    },
    {
        'questão': 'Quanto é 8-3?',
        'opção': ['1', '2', '4', '5'],
        'resposta': '5',
    },
    {
        'questão': 'Quanto é 5*5?',
        'opção': ['25', '55', '10', '51'],
        'resposta': '25',
    },
    {
        'questão': 'Quanto é 10/2?',
        'opção': ['4', '5', '2', '1'],
        'resposta': '5',
    },
    
]

questões(perguntas)