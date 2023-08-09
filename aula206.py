# Usando subprocess para executar e comandos externos
# subprocess é um módulo do Python para executar
# processos e comandos externos no seu programa.
# O método mais simples para atingir o objetivo é usando subprocess.run().
# Argumentos principais de subprocess.run():
# - stdout, stdin e stderr -> Redirecionam saída, entrada e erros
# - capture_output -> captura a saída e erro para uso posterior
# - text -> Se True, entradas e saídas serão tratadas como texto
# e automaticamente codificadas ou decodificadas com o conjunto
# de caracteres padrão da plataforma (geralmente UTF-8).
# - shell -> Se True, terá acesso ao shell do sistema. Ao usar
# shell (True), recomendo enviar o comando e os argumentos juntos.
# - executable -> pode ser usado para especificar o caminho
# do executável que iniciará o subprocesso.
# Retorno:
# stdout, stderr, returncode e args
# Importante: a codificação de caracteres do Windows pode ser
# diferente. Tente usar cp1252, cp852, cp850 (ou outros). Linux e
# mac, use utf_8.
# Comando de exemplo:
# Windows: ping 127.0.0.1
# Linux/Mac: ping 127.0.0.1 -c 4

"""
Ping é mandar um sinal para o aparelho da rede, para qualquer ip que você
quiser, podendo ser até um site, você manda um sinal, e ele manda uma resposta
"Eu entendi e recebi o sinal" isso serve para sabermos se aquele site, ou outro
computador, ou celular, qualquer  coisa que tiver um ip e você mandar um ping
para essa coisa isso serve para saber se essa coisa está online.

Ping é basicamente ping bong.
Se digitar esse "ping" na sua máquina, ou o "8.8.8.8" que é o ping do google,
ele irá mostrar os pacotes recebidos, perdas e etc. Também mostrará um tempo
de resposta.
"""
import subprocess
import sys

# sys.platform: linux, linux2, darwin, win32.


cmd = ["ping", "127.0.0.1", "-c", "4"]
encoding = "utf_8"
system = sys.platform

if system == "win32":
    cmd = ["ping", "127.0.0.1"]
    encoding = "cp852"

proc = subprocess.run(
    cmd,
    capture_output=True,
    text=True,
    encoding=encoding,  # Esse é a codificação que este windows está usando.
)

print()

# print(proc.args)  # lista passada no cmd.

# print(proc.stderr) # Quando não dá erro irá vir um (b'') vazio.

print(proc.stdout)

# print(proc.returncode) # Quando vier como "0" é por que deu certo.

"""
Se for passado um:

print(proc.stdout.decode("cp852"))

Ele vai decodificar o processo do stdout (saída) e nos mostrar. Porém,
se o "text=True" logo não precisa utilizar esse decodificador.
"""
