# pyqt-foldable-window
PyQt foldable window

== 2022/05/15 ==

This is for tutorial/example.

I will add this feature to <a href="https://github.com/yjg30737/pyqt-custom-titlebar-window.git">pyqt-custom-titlebar-window</a>.

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-foldable-window.git --upgrade```

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-svg-icon-pushbutton.git">pyqt-svg-icon-pushbutton</a>
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
    window.show()
    app.exec_()
```

Result

Note: Preview below is very first version. Current version(0.3.0) icons are svg, so they are not blurry anymore.

Unfolded state

![image](https://user-images.githubusercontent.com/55078043/152663899-93b65dbd-5763-448a-a421-58681be3f3b7.png)

Folded state

![image](https://user-images.githubusercontent.com/55078043/152663909-8a7766b7-3efc-4398-bbc8-73094be9aa87.png)

## Note
```FoldableWindow```'s argument should be only ```QMainWindow``` kind of class that ```QMenuBar``` exists. If that is not exist, error will occur.

## See Also
* <a href="https://github.com/yjg30737/pyqt-foldable-item-list-widget.git">pyqt-foldable-item-list-widget</a>
