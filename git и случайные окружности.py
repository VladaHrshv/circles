# В задаче ничего не было сказано про то,
# должны ли круги исчезать с формы, так что я представляю такой вариант
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randint
from Ui import Ui_Form


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.active)
        self.flag = 0

    def active(self):
        self.flag = 1
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.flag:
            self.drawCircle(event, qp)
        qp.end()

    def drawCircle(self, event, qp):
        SIZE = WIDTH, HEIGHT = self.width(), self.height()
        qp.setPen(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
        qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
        r = randint(1, WIDTH // 2)
        x, y = (randint(r, WIDTH - r)), (randint(r, HEIGHT - r))
        qp.drawEllipse(x, y, r, r)
        self.flag = 0


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())