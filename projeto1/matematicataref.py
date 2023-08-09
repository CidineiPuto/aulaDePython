

# while True:
#     import os

    
#     a = input('Digite o número que possui a raiz de 2: ')
#     b = input('Digite o número que acompanha o x: ')
#     c = input('Digite o número solitário: ')

#     try:
#         a_float = float(a)
#         b_float = float(b)
#         c_float = float(c)
#     except ValueError:
#         os.system('cls')
#         print('Escreva um número.')
#         continue

#     delta = ((b_float**2)-4*a_float*c_float)

#     if delta <= -1:
#         os.system('cls')
#         print(f'Seu delta foi "{delta}"')
#         print('A raiz, nunca será negativa.')
#         continue

#     bhaskara1 = -b_float
#     bhaskara2 = (delta**(1/2))
#     bhaskara3 = 2*a_float


#     try:
#         xl = ((bhaskara1+bhaskara2)/bhaskara3)
#         xll = ((bhaskara1-bhaskara2)/bhaskara3)
#     except ZeroDivisionError:
#         print('Escreva números válidos.')
#         continue
#     except Exception:
#         print('Erro desconhecido.')
#         continue

#     os.system('cls')
#     print(f'Seu delta é "{delta}"')
#     print(f'A raiz quadrada de seu delta foi "{bhaskara2}"')
#     print(f'O resultado x1 foi "{xl:.2f}"')
#     print(f'O seu resultado x2 foi "{xll:.2f}"')
    
#     continuar = input('Deseja continuar ? [S]im [N]ão ').lower().startswith('s')
#     if continuar == True:
#         os.system('cls')
#         continue
#     else:
#         break
# os.system('cls')
# print('Você saiu')



a = input('Digite o número que possui a raiz de 2: ')
b = input('Digite o número que acompanha o x: ')
c = input('Digite o número solitário: ')
try:
    a_float = float(a)
    b_float = float(b)
    c_float = float(c)
except ValueError:
    print('Escreva um número.')

delta = ((b_float**2)-4*a_float*c_float)

if delta <= -1:
    print(f'Seu delta foi "{delta}"')
    print('A raiz, nunca será negativa.')

bhaskara1 = -b_float
bhaskara2 = (delta**(1/2))
bhaskara3 = 2*a_float

try:
    xl = ((bhaskara1+bhaskara2)/bhaskara3)
    xll = ((bhaskara1-bhaskara2)/bhaskara3)
except ZeroDivisionError:
    print('Escreva números válidos.')
        
except Exception:
    print('Erro desconhecido.')   
print(f'Seu delta é "{delta}"')
print(f'A raiz quadrada de seu delta foi "{bhaskara2}"')
print(f'O resultado x1 foi "{xl:.2f}"')
print(f'O seu resultado x2 foi "{xll:.2f}"')
