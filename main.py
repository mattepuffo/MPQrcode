# https://doc.qt.io/qtforpython/tutorials/basictutorial/uifiles.html

import sys

from PySide6.QtGui import Qt, QScreen
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QCoreApplication

if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

    app = QApplication(sys.argv)

    uiFileName = "main.ui"
    uiFile = QFile(uiFileName)

    loader = QUiLoader()
    window = loader.load(uiFile)
    uiFile.close()

    window.show()
    center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
    geo = window.frameGeometry()
    geo.moveCenter(center)
    window.move(geo.topLeft())

    window.btnCrea.clicked.connect(lambda: print("clicked"))

    sys.exit(app.exec())
