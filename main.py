import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        qp.setBrush(QColor('Grey'))
        qp.drawRect(0, 0, 800, 800)
        qp.setPen(QColor('Yellow'))
        for i in range(randint(2, 15)):
            a = randint(0, 200)
            qp.drawEllipse(randint(0, 755), randint(0, 755), a, a)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
