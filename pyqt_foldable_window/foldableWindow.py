from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from pyqt_custom_titlebar_window.customTitlebarWindow import CustomTitlebarWindow
from pyqt_resource_helper import PyQtResourceHelper


class FoldableWindow(CustomTitlebarWindow):
    def __init__(self, main_window: QMainWindow):
        super().__init__(main_window)
        self.__initUi(main_window)

    def __initUi(self, main_window):
        self.__addFoldableFeature(main_window)

    def __addFoldableFeature(self, main_window: QMainWindow):
        self.__menuBar = main_window.menuBar()

        lay = QHBoxLayout()
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)

        cornerWidget = QWidget()
        cornerWidget.setLayout(lay)

        existingCornerWidget = self.__menuBar.cornerWidget(Qt.TopRightCorner)
        if existingCornerWidget:
            lay.insertWidget(0, existingCornerWidget)

        self.__arrowBtn = QPushButton()
        self.__arrowBtn.setCheckable(True)
        self.__arrowBtn.toggled.connect(self.__toggled)
        PyQtResourceHelper.setStyleSheet([self.__arrowBtn], ['style/button.css'])
        PyQtResourceHelper.setIcon([self.__arrowBtn], ['ico/fold.png'])

        lay.addWidget(self.__arrowBtn)
        cornerWidget.setLayout(lay)
        self.__menuBar.setCornerWidget(cornerWidget)

        self.__foldUnfoldAnimation = QPropertyAnimation(self, b"height")
        self.__foldUnfoldAnimation.valueChanged.connect(self.setFixedHeight)
        self.__foldUnfoldAnimation.setStartValue(self.height())
        self.__foldUnfoldAnimation.setDuration(200)
        self.__foldUnfoldAnimation.setEndValue(self.__menuBar.sizeHint().height() + self._margin + 2)

    def __toggled(self, f):
        if f:
            self.__fold()
            PyQtResourceHelper.setIcon([self.__arrowBtn], ['ico/unfold.png'])
        else:
            self.__unfold()
            PyQtResourceHelper.setIcon([self.__arrowBtn], ['ico/fold.png'])

    def __fold(self):
        self.__foldUnfoldAnimation.setDirection(QAbstractAnimation.Forward)
        self.__foldUnfoldAnimation.start()
        self.__menuBar.raise_()

    def __unfold(self):
        self.__foldUnfoldAnimation.setDirection(QAbstractAnimation.Backward)
        self.__foldUnfoldAnimation.start()
        self.__menuBar.raise_()