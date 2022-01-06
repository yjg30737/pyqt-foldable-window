from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QMenuBar, QAction, QPushButton, QHBoxLayout, QWidget, qApp
from pyqt_resource_helper import PyQtResourceHelper


class FoldableWindowMenuBar(QMenuBar):
    fold = pyqtSignal()
    unfold = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.__parent = parent
        self.__offset = 0
        self.__moving = False
        self.__initUi()

    def __initUi(self):
        fileMenu = self.addMenu('File')
        newAction = QAction('abc', self)
        fileMenu.addAction(newAction)

        self.__arrowBtn = QPushButton()
        self.__arrowBtn.setCheckable(True)
        self.__arrowBtn.toggled.connect(self.__toggled)
        PyQtResourceHelper.setStyleSheet([self.__arrowBtn], ['style/button.css'])
        PyQtResourceHelper.setIcon([self.__arrowBtn], ['ico/fold.png'])

        self.__closeBtn = QPushButton()
        self.__closeBtn.clicked.connect(qApp.exit)

        PyQtResourceHelper.setStyleSheet([self.__closeBtn], ['style/button.css'])
        PyQtResourceHelper.setIcon([self.__closeBtn], ['ico/close.png'])

        lay = QHBoxLayout()
        lay.setAlignment(Qt.AlignRight)
        lay.addWidget(self.__arrowBtn)
        lay.addWidget(self.__closeBtn)
        lay.setContentsMargins(2, 2, 2, 2)

        cornerWidget = QWidget()
        cornerWidget.setLayout(lay)

        self.setCornerWidget(cornerWidget)
        self.setMouseTracking(True)

    def __toggled(self, f):
        if f:
            self.__fold()
            PyQtResourceHelper.setIcon([self.__arrowBtn], ['ico/unfold.png'])
        else:
            self.__unfold()
            PyQtResourceHelper.setIcon([self.__arrowBtn], ['ico/fold.png'])

    def __fold(self):
        self.fold.emit()

    def __unfold(self):
        self.unfold.emit()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            p = e.pos()
            if self.actionAt(p):
                pass
            else:
                self.__offset = p
                self.__moving = True
        return super().mousePressEvent(e)

    def mouseMoveEvent(self, e):
        cur = self.cursor()
        cur.setShape(Qt.ArrowCursor)
        self.setCursor(cur)
        if self.__moving:
            self.__parent.move(e.globalPos() - self.__offset)
        return super().mouseMoveEvent(e)

    def mouseReleaseEvent(self, e):
        self.__moving = False
        return super().mouseReleaseEvent(e)

    # Maximize/normalize when user double-clicks the menu bar
    s = ''' 
    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.LeftButton:
            p = e.pos()
            if self.actionAt(p):
                pass
            else:
                if self.__parent.isMaximized():
                    self.__parent.showNormal()
                else:
                    self.__parent.showMaximized()
        return super().mouseDoubleClickEvent(e)
    '''