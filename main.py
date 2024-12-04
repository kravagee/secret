import sys

from PyQt6 import uic
from PyQt6.QtCore import QPointF, Qt, QRectF
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtWidgets import QWidget, QApplication
from random import randint


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.cur_figure = 'круг'
        self.center = (0, 0)
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_figure(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_figure(self, qp):
        rad = randint(20, 100)
        color = QColor(255, 255, 0)
        qp.setBrush(color)
        if self.cur_figure == 'круг':
            qp.drawEllipse(QPointF(randint(0, 1000), randint(0, 1000)), rad, rad)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec())