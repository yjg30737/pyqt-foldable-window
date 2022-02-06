# pyqt-foldable-window
PyQt foldable window

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-foldable-window.git --upgrade```

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-resource-helper.git">pyqt-resource-helper</a>
* <a href="https://github.com/yjg30737/pyqt-custom-titlebar-window.git">pyqt-custom-titlebar-window</a>

## Feature
* Being able to fold, unfold window by toggle button on the menu bar
* Being able to move the window with dragging menu bar
* Being able to close (obviously)

## Example
```python
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu
from pyqt_foldable_window import FoldableWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        fileMenu = QMenu('File', self)
        self.menuBar().addMenu(fileMenu)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = FoldableWindow(MainWindow())
    # if you want to add min/max/close button to the top right, add line below. 
    # that is pyqt-custom-titlebar-window(parent class of this)'s feature.
    # window.setMinMaxCloseButton()
    window.show()
    app.exec_()
```

Result

Unfolded state

![image](https://user-images.githubusercontent.com/55078043/152663899-93b65dbd-5763-448a-a421-58681be3f3b7.png)

Folded state

![image](https://user-images.githubusercontent.com/55078043/152663909-8a7766b7-3efc-4398-bbc8-73094be9aa87.png)

## Note
```FoldableWindow```'s argument should be only ```QMainWindow``` kind of class that ```QMenuBar``` exists. If that is not exist, error will occur.

If you use ```setMinMaxCloseButton```, showing maximize/normal feature and ```FoldableWindow```'s fold/unfold feature will be not synchronized well. It is not like causing error, just pet peeve of mine.
