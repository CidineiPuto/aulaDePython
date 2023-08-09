"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
# Pode acessar os escopos da função acima, mas não das funções internas

x = 1 # MAs o melhor seria definir ele antes da função.

def escopo():
    global x # Agora x é globao dentro DESTE escopo,logo o X será alterado
    x = 10 # Este X é diferente do anterior, pois foi definido do escopo.
    # E ele vai ser o X que estão nas funções 
    def outra_funcao():
        x = 11 # Agora este x será protegido, e só será executado se chamar essa função.
        y = 2
        print(x,y) 
        # Tudo feito na função irá ficar na função, dentro do "Escopo"

    outra_funcao() # Para o escopo dentro do escopo funfar, é necessário 
                   # Utilizar o escopo 2 dentro do escopo 1 e não o chamar depois, pois não será
                   # Executado

    print(x)

# x = 1 # Agora o X está fora do escopo, no caso, ele é acessável. 
# Pode ser definido abaixo da função, mas claro, sem chamar o escopo acima antes de o definir


#print(x) Isso daria um NameError pois a função não está definida externamente, apenas
# internamente dentro do escopo

print(x) # Ele pegará o X do escopo do módulo no caso o escopo universal

escopo() # Já neste, irá definir o X do escopo interno 1

print(x) # Irá continuar sendo o X1 pois o x interno (X=10) estará protegido pelo escopo.