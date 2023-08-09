# Ambientes virtuais em Python (venv)
# Um ambiente virtual carrega toda a sua instalação
# do Python para uma pasta no caminho escolhido.
# O ambiente virtual seria como um ctrl c
# e poderá salvar coisas que você usou no passado
# para depois no futuro dar ctrv v e por exemplo
# fazer uma manutenção em tal,
# além de poder amarzenar arquivos neste ambiente
# para não pesar muito sua máquina.
# Ao ativar um ambiente virtual, a instalação do
# ambiente virtual será usada.
# venv é o módulo que vamos usar para
# criar ambientes virtuais.
# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env

# requirementes.txt é a pasta em que pode instalar seu ambiente virtual de volta.
# E o usar livremente, lá mais para frente.


# Criação__________________________________________________________________________________

# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env
#
# Como criar ambientes virtuais
# Abra a pasta do seu projeto no terminal
# e digite:
# python -m venv venv


# Abra a pasta do seu projeto no terminal
# e digite:
# python -m venv venv

# Ativação__________________________________________________________________________________

# Ativando e desativando meu ambiente virtual
# Windows: .\venv\Scripts\activate
# Linux e Mac: source venv/bin/activate
# Desativar: deactivate

# Quando o venv estiver desativado o python ira usar o do sistema, instalando
# as coisas global.
# Mas quando o venv estiver ativado, o instalador utilizara a pasta do venv.

# "python.terminal.activateEnvironment": true / Será usado para ativar
# automaticamente ou
# Não, seu sistema virtual, a cada vez que você começa um novo terminal.


# pip(instalar)_______________________________________________________________________________

# pip - instalando pacotes e bibliotecas
# Instalar última versão:
# pip install nome_pacote
# Instalar versão precisa
# (tem outras formas também não mencionadas)
# pip install nome_pacote==0.0.0
# Desinstalar pacote
# pip uninstall nome_pacote
# Congelar (ver pacotes)
# pip freeze
# pip index version - mostra as versões disponíveis
# para usar coloque pip install nome_pacote==versão_que_quer_instalar
# https://pypi.org

# Requirement.txt_______________________________________________________________________________
# Criando e usando um requirements.txt
# pip freeze > requirements.txt
# Instalando tudo do requirements.txt
# pip install -r requirements.txt
