import sys
import random
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPainter, QColor


class CircleDrawer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)

        self.circles = []
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(10, 100)
        self.circles.append(diameter)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))
        x_offset = 50
        for diameter in self.circles:
            painter.drawEllipse(x_offset, 50, diameter, diameter)
            x_offset += diameter + 10


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec_())
