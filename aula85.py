def executa(funcao, *args): # Args vai ser os parâmetros
    return funcao(*args) # Executa está servindo para executar as ações de lambda


def soma(x, y):
    return x + y


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica



#______soma_______

# print(
#     executa(
#         lambda x, y: x + y,
#         2,3
#     ),
#     executa(soma, 2,3),
#     soma(2,3) # Mesma coisa
# )

#______duplicação_______

# duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(2))

# Mas se lambda for usado de maneira complexa igual essa, o código ficaria ruim
# Por isso é melhor a usar de maneira mais simples, tipo deste jeito =

print(
    executa(
        lambda x, y: x + y, # print(executa(lambda x, y: x + y, 2,3),)
        2,3
    ),
)





print(
    executa(
        lambda *args : sum(args), # Soma todos os números presentes
        1,2,4,5,6,7,8,9 
    ) 
)
