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
        self.__menuBar.fold.connect(self.__fold)
        self.__menuBar.unfold.connect(self.__unfold)

        lay.insertWidget(0, self.__menuBar)
        lay_margin = self.__n_margin // 4
        lay.setContentsMargins(lay_margin, lay_margin, lay_margin, lay_margin)
        lay.setSpacing(0)

        self.__foldUnfoldAnimation = QPropertyAnimation(self, b"height")
        self.__foldUnfoldAnimation.valueChanged.connect(self.setFixedHeight)
        self.__foldUnfoldAnimation.setStartValue(self.height())
        self.__foldUnfoldAnimation.setDuration(200)
        self.__foldUnfoldAnimation.setEndValue(self.__menuBar.sizeHint().height() + self.__n_margin // 2 - 1)

    def __fold(self):
        self.__foldUnfoldAnimation.setDirection(QAbstractAnimation.Forward)
        self.__foldUnfoldAnimation.start()
        self.__menuBar.raise_()

    def __unfold(self):
        self.__foldUnfoldAnimation.setDirection(QAbstractAnimation.Backward)
        self.__foldUnfoldAnimation.start()
        self.__menuBar.raise_()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = FoldableWindow()
    window.layout().addWidget(QTextEdit())
    window.show()
    app.exec_()