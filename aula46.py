"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""



#palavra_secreta = 'Almondega'
#numeros_tentavias = 0 
#letras_acertadas = ''
#
#while True:
#     letra_digitada = input('Digite uma letra: ')
#
#     numeros_tentavias += 1
#
#     if len(letra_digitada) > 1:
#         print('Escreva apenas uma letra.')
#         continue
#     
#     if letra_digitada in palavra_secreta:
#         letras_acertadas += letra_digitada
#
#     palavra_formada = ''
#
#     for letra_secreta in palavra_secreta:
#         if letra_secreta in letras_acertadas:
#             palavra_formada += letra_secreta
#         else:
#             palavra_formada += '*'
#
#     print('Palavra formada = ', palavra_formada)
#
#     if palavra_formada == palavra_secreta:
#         print('VOCÊ ACERTOU!!!')
#         print(f'Seu número de tentativas foi {numeros_tentavias}x.')
#         print(f'A palavra era {palavra_secreta}.')
#         letras_acertadas = ''
#         numeros_tentavias = 0

#  Minha lista 

while  True:
    import random
    lista1 = ('corredor', 'agasalho', 'banana', 'miojo', 'casa', 'nozes', 'abacaxi', 'aveia',\
           'alface', 'alabastro', 'gladiador', 'anime', 'abacate', 'azeite', 'ventilador', 'azeite',\
             'arroz', 'peixe', 'perfume', 'cassetete', 'jogo', 'metal', 'ouro','concreto',\
                'choveiro', 'cavalo', 'iguana', 'serpente', 'cachorro', 'gato','katana',
                'samurai','guereiro','abismo','sujeito','estranho','luz',
                'vencedor')
   
    palavra_secreta = random.choice(lista1) # Irá escolher uma str desta lista.
    letras_acertadas = ''
    numero_de_tentativas = 1
    letras_usadas = ''
    espaco = '\r\n'
    continuar = ''
   
    while True:
        import os
        
        print(espaco)
        letra_digitada = input('Digite uma letra: ')
        print(espaco)
        if len(letra_digitada) > 1: # Se letra digitada, tiver mais que um dígito.
       
            print('Digite apenas UMA letra.')
            numero_de_tentativas += 1 
            continue # Irá voltar do inicío

        # if numero_de_tentativas == 15:
        #      os.system('cls')
        #      print('Você excedeu o número de tentativas máxima.')
        #      print('O jogo irá recomeçar')
        #      print(20*'-')
        #      break
        os.system('cls') # Esse limpará o terminal
        if letra_digitada in letras_usadas: #SE letrada digitada, estiver nas letras usadas.
            print(f'A letra "{letra_digitada}" já foi utilizada.')
            print(f'Letras usadas "{letras_usadas}"')
            print(20*'-')
            numero_de_tentativas += 1
            continue # O programa irá voltar do inicío


        if letra_digitada in palavra_secreta: # Por acaso, a letra estiver na palavra
            print(f'"{letra_digitada}" está na palavra  '\
            'secreta')  
            print(espaco)
            letras_acertadas += letra_digitada # Letra acertada irá adicionar a letra da palavra
        else:
            print(f'"{letra_digitada}"não está na palavra secreta.')
            print(espaco)
   
   
        palavra_formada = ''
        for letra_secreta in palavra_secreta: # O for pegará as letras da palavra e irá conferir
            if  letra_secreta in letras_acertadas: # Se uma dessas letras, estiver na palavra acertada
                palavra_formada += letra_secreta # A letra será adicionada na palavra formada
            else:
                palavra_formada += '#' # As letras que não estiverem irão se tornar "#"
            
   
   
        letras_usadas +=  letra_digitada + ','  # A letra digitada, se tornará usada
        
        print(f'A palavra formada foi "{palavra_formada}"') 
        print(espaco)
        print(f'As letras que já foram utilizadas  são "{letras_usadas}".')
        numero_de_tentativas += 1 

        print(20*'-')
   
        if palavra_formada == palavra_secreta: # Quando a palavra estiver completa
            os.system('cls') # Esse limpará o terminal
            print('PARABÉNS VOCÊ ACERTOU!!!')
            print(espaco)
            print(f'A palavra secreta era {palavra_secreta}')
            print(espaco)
            print(f'Seu número de tentativas foi ({numero_de_tentativas}x)')
            print(espaco)
            # A letra acertada, as tentativas, e as letras usadas irão retornar ao
            letras_acertadas = ''  # Padrão.
            numero_de_tentativas = 0
            letras_usadas = ''
            
        elif palavra_formada != palavra_secreta: # Se não estiver terminado a palavra
            continue # O número voltará do inicío
        continuar = input('Deseja continuar ? [S]im [N]ão  ').lower().startswith('s') 
        if continuar == True: # O continuar poderá se tornar True ou false  
             os.system('cls') # Esse limpará o terminal
             print(20*'-')
             break
        else: # Se a pessoa escolher "N/n" irá sair, se escolher "S/s" irá continuar.
             break
    if continuar == False:
         break

os.system('cls')
print('Você saiu.')
        
    