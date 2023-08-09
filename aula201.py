# (Parte 1) Básico do protocolo HTTP (HyperText Transfer Protocol)
# HTTP (HyperText Transfer Protocol) é um protocolo usado enviar e receber
# dados na Internet. Ele funciona no modo cliente/servidor, onde o cliente
# (seu navegador, por exemplo) faz uma requisição ao servidor
# (site, por exemplo), que responde com os dados adequados.
#
# A mensagem de requisição do cliente deve incluir dados como:
# - O método HTTP
#     - leitura (safe) - GET, HEAD (cabeçalhos), OPTIONS (métodos suportados)
#     - escrita - POST, PUT (substitui), PATCH (atualiza), DELETE
# - O endereço do recurso a ser acessado (/users/)
# - Os cabeçalhos HTTP (Content-Type, Authorization)
# - O Corpo da mensagem (caso necessário, de acordo com o método HTTP)
#
# A mensagem de resposta do servidor deve incluir dados como:
# - código de status HTTP (200 success, 404 Not found, 301 Moved Permanently)
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# - Os cabeçalhos HTTP (Content-Type, Accept)
# - O corpo da mensagem (Pode estar em vazio em alguns casos)

"""
Isso é um web scrapping "raspagem de dados" como diz, serve para puxar os
dados de algum site, para o python, puxar dados de sites na internet.
a raspagem não é díficil, só que você precisa ter um "soft skill", soft skill,
é algo que está ligado com que você está aprendendo, e precisa saber disso
para falar sobre outra coisa. Um exemplo de soft skill, é ter que aprender
html e css para fazer a raspagem de dados.
Outra coisa que precisa saber, é como chegar neste site, aí que entra
prótocolo http, é um prótocolo utilizado para enviar e receber dados.
Geralmente usado para fazer alguma requisição.
Criar um pedido para um determinado servidor, e essa é a parte do cliente,
que vai solicitar isto.

Exemplo usamos o método "GET" no google, para ler o site.

Logo tem que saber o método que vamos usar.

A diferença do método PUT e do PATCH, é que o PUT, substitui TODO o arquivo.
Já o método PATCH, atualiza apenas um elemento do arquivo.
E o método POST, cria algo no arquivo.

E também tem o DELETE para apagar alguma coisa. Na maioria dos casos você manda
um body, para os dados da requisição, do que você quer fazer, isso no método de
escrita no caso.

Os recursos, é o endereço, quando passamos no final, por exemplo "(/users/)"
estamos acessando a parte do usuário, mas se passarmos só "/" estamos acessando
a raiz do site.

https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status Esse site, mostra os
códigos de status de respostas da troca.

Em resumo, seu computador é o cliente, o conteúdo que você está tentando
acessar é o servidor, ocorrerá uma troca de mensagens e dados entre os dois.

Para ver os status code, vá em uma pág, vá no inspecionar, e encima do
inpecionar vá em "network".

Clique em um dos números do status, e poderá ver o content type, e tudo mais.
"""
