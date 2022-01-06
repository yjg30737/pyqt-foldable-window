from setuptools import setup, find_packages

setup(
    name='pyqt-foldable-window',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_foldable_window.style': ['button.css'],
                  'pyqt_foldable_window.ico': ['close.png', 'conceal.png', 'reveal.png']},
    description='PyQt foldable window',
    url='https://github.com/yjg30737/pyqt-foldable-window.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main'
    ]
)