# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (button1)
#               -> Widget 2 (button2)
#               -> Widget 3 (button3)
#   -> show
# -> exec

import sys

from PySide6.QtCore import Slot  # É recomendado usar nas funções que são slot.
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QMainWindow,
    QPushButton,
    QWidget,
)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle("Janela do bungas")
button1 = QPushButton("Texto do botão")
button1.setStyleSheet("font-size: 80px;")


button2 = QPushButton("Botão 2")
button2.setStyleSheet("font-size: 40px;")

button3 = QPushButton("Botão 3")
button3.setStyleSheet("font-size: 40px;")

layout = QGridLayout()
central_widget.setLayout(layout)
layout.addWidget(button1, 1, 1, 1, 1)
layout.addWidget(button2, 1, 2, 1, 1)
layout.addWidget(button3, 3, 1, 1, 2)


@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage("O meu slot foi executado.")

    return inner()


@Slot()
def other_slot(checked):  # arg __1, marcado ou não.
    print("Está marcado?", checked)


@Slot()
def third_slot(action):
    def inner_function():
        other_slot(action.isChecked())

    return inner_function


# Adiando execução da função, criando outra função, levando o escopo, dessa
# função para outro local. Mesma coisa feita com o lambda, a diferença, é que
# agora está sendo criado um estudo numa função.


# StatusBar
status_bar = window.statusBar()
status_bar.showMessage("Mostrar mensagem na barra")

# MenuBar
menu = window.menuBar()
first_menu = menu.addMenu("Primeiro menu")
first_action = first_menu.addAction("Primeira ação")
first_action.triggered.connect(slot_example(status_bar))

second_action = first_menu.addAction("Segunda ação")
second_action.setCheckable(True)
# Deixa a ação duma maneira que ela será de marcar ou desmarcar.
second_action.toggled.connect(other_slot)
second_action.hovered.connect(third_slot(second_action))
# Signal, é como dito antes, um sinal, por exemplo, toggled e trigged, sinais
# De que algo foi feito, e poderão executar coisas na tela.
# O slot, é a ação feita, após o signal ser emitido, fazendo uma conexão
# a partir do connect, e no caso, o que seria conectado é o slot, uma ação
# que será feita.

# Esse não recebe lambda, pois o outro slot, já é automático receber ele,
# sendo chamado o checked automaticamente.
# Então, após alguma coisa acontecer com a second_action, se ela for marcada
# algo irá acontecer.


# Agora, por conta do hovered, ele está falando se tal ação foi marcada ou não.

# Em resumo um signal será passada para você queira você ou não, dentro da
# por isso é recomendado ir na doc, ver com qual signal quer conectar.

button1.clicked.connect(third_slot(second_action))
window.show()
app.exec()
