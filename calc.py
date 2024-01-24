from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import ui_shaxxxov
import sys

class App(QMainWindow, ui_shaxxxov.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui_shaxxxov.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.calculate)
        self.ui.lineEdit_2.returnPressed.connect(self.calculate)

    def calculate(self):
        try:
            summ = int(self.ui.lineEdit.text())
            days = int(self.ui.lineEdit_2.text())
        except:
            QMessageBox.about(self, 'Ошибка!', 'Введены не числа!')
            return

        try:
            for k in range(days):
                summ += (summ/100)**2
        except:
            QMessageBox.about(self, 'Долг достиг ПРЕДЕЛА', 'Финальный долг должника: ' + '{:e}'.format(int(summ)))
            return

        QMessageBox.about(self, 'Калькуляция проведена!', f'Должник в рабстве на сумму: {int(summ)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()