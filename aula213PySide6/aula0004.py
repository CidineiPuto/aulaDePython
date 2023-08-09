# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec

import sys

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
botao1 = QPushButton("Texto do botão")
botao1.setStyleSheet("font-size: 80px;")


botao2 = QPushButton("Botão 2")
botao2.setStyleSheet("font-size: 40px;")

botao3 = QPushButton("Botão 3")
botao3.setStyleSheet("font-size: 40px;")

layout = QGridLayout()
central_widget.setLayout(layout)
layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)


def slot_example(status_bar):
    status_bar.showMessage("O meu slot foi executado.")


# StatusBar
status_bar = window.statusBar()
status_bar.showMessage("Mostrar mensagem na barra")

# MenuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu("Primeiro menu")
primeira_acao = primeiro_menu.addAction("Primeira ação")
primeira_acao.triggered.connect(
    lambda: slot_example(status_bar),
)
"""
Uma nova função, no caso a lambda, está sendo criada, e dentro dessa função
quando ela for chamada, e a ação for executada, será executada esta outra
função, passando a status_bar lá para dentro, adiando a execução da função.
"""
# Quando a ação é executada, tal sinal é chamado de triggered. Então agora,
# quando tal ação for executada, será mostrado 123 no terminal, por conta da
# ação dentro dela, que é o slot_example.


# Isso tudo só é possível devido a "window."

window.show()
app.exec()


"""
A "Window" já deixa um menu pronto, e uma status bar também.
Tal status bar, é a que está acima, sendo chamada de "status_bar" podendo
fazer o que quiser com ela.
"""
