# https://doc.qt.io/qtforpython/tutorials/basictutorial/uifiles.html

import sys
from pathlib import Path

from PySide6.QtGui import Qt, QScreen
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6.QtCore import QFile, QCoreApplication
from create_qrcode import CreateQrcode

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.uiFileName = "main.ui"
        self.uiFile = QFile(self.uiFileName)

        self.loader = QUiLoader()
        self.window = self.loader.load(self.uiFile)
        self.uiFile.close()

        self.window.show()
        self.center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        self.geo = self.window.frameGeometry()
        self.geo.moveCenter(self.center)
        self.window.move(self.geo.topLeft())

        self.window.txtTesto.setFocus()
        self.window.btnCrea.clicked.connect(lambda: self.saveFileDialog(self.window.txtTesto.text().strip()))

    def saveFileDialog(self, testo):
        if testo:
            cqr = CreateQrcode()
            cqr.create('ciao')

            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getSaveFileName(self, "Salva", str(Path.home()),
                                                      "All Files (*);;Text Files (*.txt)", options=options)
            if fileName:
                print(fileName)

if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())
