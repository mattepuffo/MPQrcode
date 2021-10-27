# https://doc.qt.io/qtforpython/tutorials/basictutorial/uifiles.html

import sys

from PySide6.QtGui import Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice, QCoreApplication

if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

    app = QApplication(sys.argv)

    uiFileName = "main.ui"
    uiFile = QFile(uiFileName)
    if not uiFile.open(QIODevice.ReadOnly):
        print(f"Cannot open {uiFileName}: {uiFile.errorString()}")
        sys.exit(-1)

    loader = QUiLoader()
    window = loader.load(uiFile)
    uiFile.close()

    if not window:
        print(loader.errorString())
        sys.exit(-1)

    window.show()
    sys.exit(app.exec())
