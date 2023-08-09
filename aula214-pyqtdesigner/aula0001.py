"""
Caso dê errado em abrir o "designer.exe/designer.app" apenas vá nesse site:
https://build-system.fman.io/qt-designer-download
E baixe para o seu sistema.

Após baixar, irá escolher o que irá querer
criar, no caso, foi escolhido para criar uma
"MainWindow".

A área, object inspector é uma representação
do que está em sua janela.

A janela está assim  com uma QMainWindow

QMainWindow -> centralWidget -> menubar - statusbar

Se clicar neles, pode ver várias coisas que pode fazer.

No lado esquerdo da tela, possui os widgets, os butões e os layouts.


Para escolher um objeto, apenas pegue ele, arraste até a tela, e ele vai ser
adicionado na janela, lá você pode ajustar ele.

Uma maneira de ajustar o tamanho é, clicar no botão direito depois clicar
em "layout" depois, escolha se quer ajustar em layout horizontal ou vertical
e pronto.
Caso for alterar/configurar algum objeto no property editor, é recomendado
pesquisar no "filter".

Pode pesquisar, align, font, e por aí vai.

Também pode mudar o nome dos objetos em "objectName".

Se formos selecionar mais um layout, por exemplo a própria grid, depois
formos escolher aonde ela vai ficar. É possível ver um risco em azul na tela,
significando aonde ele ficará.
E novamente dito, pode ser alterado o nome da mesma.

Após a janela estar pronta, pelo menos uma parte, pode ir no form, e clicar em
"preview" para ver como a mesma irá ficar.

Para salvar clique no ícone de baixo do form, o terceiro na esquerda superior.
se fazer isto:
pyside6-uic .\aula214-pyqtdesigner\ui\window.ui -o 
.\aula214-pyqtdesigner\src\window.py

Será criado um arquivo python a partir do ui que foi utilizado.

Toda hora que isso for feito, será necessário a recompilação.
"""