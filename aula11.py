
#Ordem de precendencia;
#1. (n + n) parênteses 
# 2. ** potenciação
# 3. * / // % Modulo, divisão e multiplicação.
# 4. + -  Soma e subtração.

conta_1 = (1 + int(0.5 + 0.5)) ** (5 + (5**1)) # 1024 
print(conta_1)