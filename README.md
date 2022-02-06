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
from PyQt5.QtWidgets import QApplication, QTextEdit
from pyqt_foldable_window import FoldableWindow


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = FoldableWindow()
    window.layout().addWidget(QTextEdit()) # QTextEdit is center widget in this example.
    window.show()
    app.exec_()
```

Result

Unfolded state

![image](https://user-images.githubusercontent.com/55078043/148364015-c8b7ae03-4004-4940-a8d3-655e32e0bbd5.png)

Folded state

![image](https://user-images.githubusercontent.com/55078043/148364439-3ffeaad8-5a6f-4e80-bd03-8bd498255b03.png)

## Note

I didn't add any features to let user set their customized menu bar. Maybe i will add that feature in any ways.
