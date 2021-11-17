import sys
from pathlib import Path
from shutil import copyfile
from PySide6.QtCore import QFile, QCoreApplication
from PySide6.QtGui import Qt, QScreen
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog

from create_qrcode import CreateQrcode

class MainWindow(QWidget):
    tmpImg = ''

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
        self.window.btnCrea.clicked.connect(lambda: self.createQr(self.window.txtTesto.text().strip()))
        self.window.btnSalva.clicked.connect(lambda: self.saveFileDialog())

    def createQr(self, testo):
        cqr = CreateQrcode()
        self.tmpImg = cqr.create(testo, "file.png")
        self.window.lblImage.setStyleSheet(
            "background-image : url('" + self.tmpImg + "');background-position: center;background-repeat: no-repeat;")
        self.window.btnSalva.setEnabled(True)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Salva", str(Path.home()), "PNG (*.png)", options=options)

        if fileName:
            copyfile(self.tmpImg, fileName + '.png')

if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())
