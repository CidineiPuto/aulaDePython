


# insira = ('[I]nserir'.lower.startwith('i'))


lista1 = []
import os


while True:
    print('Selecione uma opção')
    selecione_uma_opção = input('[i]nserir [a]pagar [l]istar: ')
    apagar_valor = ''
    

    if selecione_uma_opção == 'i':
        os.system('cls')
        inserir_pergunta = input('Insira um valor: ')
        lista1.append(inserir_pergunta)
        continue




    elif selecione_uma_opção == 'l':
        os.system('cls')

        if not lista1:
            print('Não tem nada em sua lista.')
            continue 
       
        for indice,nome in enumerate(lista1):
            print(indice,nome)
        
            
   
            
            
            
    elif selecione_uma_opção == 'a':
        os.system('cls')
        
        apagar_valor = (input('Selecione um índice para ser apagado: '))
       

        try:
            apagar_valor_int = int(apagar_valor)

            if apagar_valor_int <= -1:
                print('O valor está menor que 0')
                continue

            if apagar_valor_int <= len(lista1) -1:
                del lista1[apagar_valor_int]
                print(f'Indice "{apagar_valor_int}" apagado.')


            elif apagar_valor_int > len(lista1) -1:
                print('índice inexistente.')
                continue
        # except IndexError:
        #     print('Não foi possível apagar esse índice.')
        except ValueError:
            print('Não foi possível apagar esse índice.')
        

    

            

    else:
        os.system('cls')
        print('Por favor, escolha uma das opcões (i,a,l).')
        continue
    
     
    
