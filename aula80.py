# Exercício - sistema de perguntas e respostas


# --------------------Minha resolução--------------------

# import os 

# perguntas = [
#     {
#         'Pergunta': 'Quanto é 2+2?',
#         'Opções': ['1', '3', '4', '5'],
#         'Resposta': '4',
#     },
#     {
#         'Pergunta': 'Quanto é 5*5?',
#         'Opções': ['25', '55', '10', '51'],
#         'Resposta': '25',
#     },
#     {
#         'Pergunta': 'Quanto é 10/2?',
#         'Opções': ['4', '5', '2', '1'],
#         'Resposta': '5',
#     },
# ]

# def resposta(resposta_certa):
#         def resposta_usuario(resposta_usuario):
#             return  resposta_certa == resposta_usuario
#         return resposta_usuario

# perguntas1 = []

# for pergunta in perguntas:
#     perguntas1.append(pergunta)



# questoes_acertadas = 0
# numeros_questoes = len(perguntas1)


# for pergunta in perguntas:
    

#     print(pergunta['Pergunta'])
    
   
#     resposta_certa = 0

#     for indice,questoes in enumerate(pergunta['Opções']):
#         print(f'{indice}) {questoes}')
#         if questoes == pergunta['Resposta']:
#             resposta_certa = resposta(indice)

#     resposta_usuario = input('Digite uma resposta: ')


#     try:
#         resposta_usuario_int = int(resposta_usuario)
#     except ValueError:
#          print('Você errou :(')
#          continue

#     if resposta_certa(resposta_usuario_int) == True:
#           os.system('cls')
#           print('Você acertou !!!')
#           questoes_acertadas += 1
#     else:
#           os.system('cls')
#           print('Você errou :(')

# os.system('cls')
# print(f'Você acertou {questoes_acertadas} de {numeros_questoes} questões.')




# --------------------Resolução professor--------------------

# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
        },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']

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
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')


# --------------------Resolução Outros alunos--------------------

# quest_set = 0
# quest_miss = 0
 
# perguntas = [
#     {
#         'question': 'Quanto é 2+2?',
#         'options': ['1', '2', '4', '5'],
#         'response': '4',
#     },
#     {
#         'question': 'Quanto é 8-3?',
#         'options': ['1', '2', '4', '5'],
#         'response': '5',
#     },
#     {
#         'question': 'Quanto é 5*5?',
#         'options': ['25', '55', '10', '51'],
#         'response': '25',
#     },
#     {
#         'question': 'Quanto é 10/2?',
#         'options': ['4', '5', '2', '1'],
#         'response': '5',
#     },
    
# ]


# for numero_da_pergunta in range(len(perguntas)):
#     question = perguntas[numero_da_pergunta]['question']
#     option = perguntas[numero_da_pergunta]['options']
#     response = perguntas[numero_da_pergunta]['response']
    
#     print(f'\n{question}\n{option[0]}\n{option[1]}\n{option[2]}\n{option[3]}')
#     get_response = input('--> ')
    
#     if get_response == response:
#         print('\nAcertou')
#         quest_set += 1
#     else:
#         print('\nErrou')
#         quest_miss += 1
    
# print(f'Você acertou {quest_set} de {len(perguntas)} perguntas!')