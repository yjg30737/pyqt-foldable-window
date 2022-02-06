from setuptools import setup, find_packages

setup(
    name='pyqt-foldable-window',
    version='0.2.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_foldable_window.style': ['button.css'],
                  'pyqt_foldable_window.ico': ['fold.png', 'unfold.png']},
    description='PyQt foldable window',
    url='https://github.com/yjg30737/pyqt-foldable-window.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main',
        'pyqt-custom-titlebar-window @ git+https://git@github.com/yjg30737/pyqt-custom-titlebar-window.git@main'
    ]
)