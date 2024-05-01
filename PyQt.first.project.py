from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QToolBar
from PyQt6.QtGui import QPainter, QPen, QPainterPath, QColor, QAction
from PyQt6.QtCore import Qt


class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.path = QPainterPath()
        self.brushColor = Qt.GlobalColor.black  

    def mousePressEvent(self, event):
        self.path.moveTo(event.position())

    def mouseMoveEvent(self, event):
        self.path.lineTo(event.position())
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(self.brushColor, 3, Qt.PenStyle.SolidLine))
        painter.drawPath(self.path)

    def setBrushColor(self, color):
        self.brushColor = color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas()
        self.setCentralWidget(self.canvas)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PyQt6 Drawing App")
        self.resize(400, 300)
        toolbar = QToolBar("Toolbar")
        self.addToolBar(toolbar)

        black_action = QAction('Black', self)
        black_action.triggered.connect(lambda: self.canvas.setBrushColor(Qt.GlobalColor.black))
        toolbar.addAction(black_action)

        red_action = QAction('Red', self)
        red_action.triggered.connect(lambda: self.canvas.setBrushColor(Qt.GlobalColor.red))
        toolbar.addAction(red_action)

        # Add more colors as needed
        green_action = QAction('Green', self)
        green_action.triggered.connect(lambda: self.canvas.setBrushColor(Qt.GlobalColor.green))
        toolbar.addAction(green_action)

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
