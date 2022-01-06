from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from pyqt_foldable_window.foldableWindowMenuBar import FoldableWindowMenuBar


class FoldableWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__n_margin = 10
        self.__initUi()

    def __initUi(self):
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.__cursor = QCursor()

        self.setMouseTracking(True)

        self.setFixedSize(200, 200)

        lay = QVBoxLayout()
        lay.setAlignment(Qt.AlignTop)
        self.setLayout(lay)

        menubar = FoldableWindowMenuBar(self)
        self.setMenuBar(menubar)

    def setMenuBar(self, menubar: QMenuBar):
        lay = self.layout()
        self.__menuBar = menubar
        self.__menuBar.setMinimumHeight(self.__menuBar.sizeHint().height())
        self.__menuBar.shrink.connect(self.__shrink)
        self.__menuBar.expand.connect(self.__expand)

        lay.insertWidget(0, self.__menuBar)
        lay_margin = self.__n_margin // 4
        lay.setContentsMargins(lay_margin, lay_margin, lay_margin, lay_margin)
        lay.setSpacing(0)

        self.__shrinkExpandAnimation = QPropertyAnimation(self, b"height")
        self.__shrinkExpandAnimation.valueChanged.connect(self.setFixedHeight)
        self.__shrinkExpandAnimation.setStartValue(self.height())
        self.__shrinkExpandAnimation.setDuration(200)
        self.__shrinkExpandAnimation.setEndValue(self.__menuBar.sizeHint().height() + self.__n_margin // 2 - 1)

    def __shrink(self):
        self.__shrinkExpandAnimation.setDirection(QAbstractAnimation.Forward)
        self.__shrinkExpandAnimation.start()
        self.__menuBar.raise_()

    def __expand(self):
        self.__shrinkExpandAnimation.setDirection(QAbstractAnimation.Backward)
        self.__shrinkExpandAnimation.start()
        self.__menuBar.raise_()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = FoldableWindow()
    window.layout().addWidget(QTextEdit())
    window.show()
    app.exec_()