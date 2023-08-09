# if / elif      / else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair" ? ')



if entrada == 'sair':
    print('Você saiu do sistema.')
elif entrada == 'entrar':
    print('Você entrou no sistema.')
else:
    print('Você não digitou nenhum comando aceito.')
    print('Tente digitar "entrar" ou "sair"')
