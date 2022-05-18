from setuptools import setup, find_packages

setup(
    name='pyqt-foldable-window',
    version='0.3.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_foldable_window.style': ['button.css'],
                  'pyqt_foldable_window.ico': ['fold.svg', 'unfold.svg']},
    description='PyQt foldable window',
    url='https://github.com/yjg30737/pyqt-foldable-window.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqt-svg-button>=0.0.1',
        'pyqt-resource-helper>=0.0.1',
        'pyqt-custom-titlebar-window>=0.0.1'
    ]
)