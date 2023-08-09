# Trabalhando com classes e herança no PySide6
import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QMainWindow,
    QPushButton,
    QWidget,
)


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # Sempre utilize o super primeiro.

        self.central_widget = QWidget()

        self.setCentralWidget(self.central_widget)
        self.setWindowTitle("Minha janela bonita")

        # Botão
        self.botao1 = self.make_button("Texto do botão")
        self.botao1.clicked.connect(self.second_market_action)  # type: ignore

        self.botao2 = self.make_button("Botão 2")

        self.botao3 = self.make_button("Terceiro")

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.botao1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.botao2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.botao3, 3, 1, 1, 2)

        # statusBar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Mostrar mensagem na barra")

        # menuBar
        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu("Primeiro menu")
        self.primeira_acao = self.primeiro_menu.addAction("Primeira ação")
        self.primeira_acao.triggered.connect(  # type:ignore
            self.muda_mensagem_da_status_bar
        )

        self.segunda_action = self.primeiro_menu.addAction("Segunda ação")
        self.segunda_action.setCheckable(True)
        self.segunda_action.toggled.connect(  # type:ignore
            self.second_market_action
        )
        self.segunda_action.hovered.connect(  # type:ignore
            self.second_market_action
        )

    @Slot()
    def muda_mensagem_da_status_bar(self):
        self.status_bar.showMessage("O meu slot foi executado")

    @Slot()
    def second_market_action(self):
        print("Está marcado?", self.segunda_action.isChecked())

    def make_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet("font-size: 80px;")
        return btn

        # Por conta da função ter sido atrelado numa classe, e também por conta
        # do status_bar ter um self, não precisa usar o outro argumento.
        # apenas usar self no local.


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()
