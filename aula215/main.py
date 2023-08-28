import sys
import time

from PySide6.QtCore import QObject, QThread, Signal
from PySide6.QtWidgets import QApplication, QWidget
from ui_worker import Ui_Form


class Worker1(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def doWork(self):
        value = "0"
        self.started.emit(value)
        for i in range(1, 5 + 1):
            value = str(i)
            self.progressed.emit(str(value))
            time.sleep(1)
        self.finished.emit(value)


class MyWidget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.button1.clicked.connect(self.hardWork1)
        self.button2.clicked.connect(self.hardWork2)

    def runWorker1(self, worker: Worker1):
        self._thread = QThread()
        thread = self._thread
        worker.moveToThread(thread)

        # Mover o worker para a thread
        worker.moveToThread(thread)

        # Run
        thread.started.connect(worker.doWork)
        worker.finished.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.worker1Starded)
        worker.progressed.connect(self.worker1progressed)
        worker.finished.connect(self.worker1finished)

        return thread.start()

    def worker1Starded(self, value):
        self.button1.setDisabled(True)
        self.label1.setText(value)
        print("Worker iniciado")

    def worker1progressed(self, value):
        self.label1.setText(value)
        print("Em progresso")

    def worker1finished(self, value):
        self.label1.setText(value)
        self.button1.setDisabled(False)
        print("Worker finalizado")

    def runWorker2(self, worker: Worker1):
        self._thread2 = QThread()
        thread2 = self._thread2
        worker.moveToThread(thread2)

        # Mover o worker para a thread
        worker.moveToThread(thread2)

        # Run
        thread2.started.connect(worker.doWork)
        worker.finished.connect(thread2.quit)

        thread2.finished.connect(thread2.deleteLater)
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.worker2Starded)
        worker.progressed.connect(self.worker2progressed)
        worker.finished.connect(self.worker2finished)

        return thread2.start()

    def worker2Starded(self, value):
        self.button2.setDisabled(True)
        self.label2.setText(value)
        print("Worker 2 iniciado")

    def worker2progressed(self, value):
        self.label2.setText(value)
        print("2 em progresso")

    def worker2finished(self, value):
        self.label2.setText(value)
        self.button2.setDisabled(False)
        print("Worker 2 finalizado")

    def hardWork1(self):
        self._worker = Worker1()
        self.runWorker1(self._worker)

    def hardWork2(self):
        self._worker2 = Worker1()
        self.runWorker2(self._worker2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
