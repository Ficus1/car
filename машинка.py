import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)
        self.image = QLabel(self)
        self.pixmap = QPixmap('cat.jpg')
        self.a = 0

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Квадратик')

    def mouseMoveEvent(self, event):
        self.x, self.y = event.x(), event.y()
        if self.x > 230 or self.y > 230:
            if self.x > 230:
                self.x = 230
            if self.y > 230:
                self.y = 230
        self.image.move(self.x + 10, self.y + 10)
        self.image.resize(self.x - (self.x - 60), self.y - (self.y - 60))
        self.image.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.x, self.y = self.cursor().pos().x() - 300, self.cursor().pos().y() - 300
            if self.a == 0:
                self.a = 1
                self.pixmap = QPixmap('smile.jpg')
            else:
                self.a = 0
                self.pixmap = QPixmap('cat.jpg')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())