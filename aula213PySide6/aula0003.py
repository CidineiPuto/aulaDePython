# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets

import sys

from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget

app = QApplication(sys.argv)

botao = QPushButton("Texto do botão")
botao.setStyleSheet("font-size: 80px;")


botao2 = QPushButton("Botão 2")
botao2.setStyleSheet("font-size: 40px;")

botao3 = QPushButton("Botão 3")
botao3.setStyleSheet("font-size: 40px;")

central_widget = QWidget()  # Ele não recebe um outro widget, mas sim um layout
# Layout ele recebe outros widget e os posiciona na pág como quiser.
# Exemplo o "QVBoxLayout" em que todo widget que colocar dentro desse layout,
# será colocado de cima pra baixo.
# Mas caro queira um horizontal, só usar QHBoxLayout
# E também, possui o QGridLayout, só que ele recebe outras coisas.
# Pois pode passar qual coluna, e linha.
layout = QGridLayout()
central_widget.setLayout(layout)
layout.addWidget(botao, 1, 1, 1, 1)  # Esse botão é da linha 1, coluna 1
layout.addWidget(botao2, 1, 2, 1, 1)  # row, col, row span, col span
layout.addWidget(botao3, 3, 1, 1, 2)

"""
Porém, se você colocar no QGrid, um "addWidget" Que vai adicionar mais uma
coluna, essa coluna será adicionada na pág, então, caso queira que um
ocupe 2 colunas, existe algo chamado "row span" e "col span"

layout.addWidget(botao2, 3, 1, 1, 1) linha 3, coluna 1, row span 1, col span 1
se o row, ou o col span, for mais de um, ele irá ocupar a quantidade de linha
ou coluna colocada lá.

"""

central_widget.show()  # Entra na hierarquia e mostra a sua janela

app.exec()  # O loop da aplicação
"""
É necessário de algo chamado "central widget" quando você tem uma janela,
em que nela pode configurar um único widget que tem nessa janela ali.
Joga um layout dentro desse widget, e esse layout recebe vários widget.
"""
