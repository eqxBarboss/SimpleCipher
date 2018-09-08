import sys

from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication, QPushButton,
    QDesktopWidget, QComboBox, QMessageBox)

import RailFence, Grille, Vigenere, CheckData


AlphEng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
AlphRus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'

InputFileName = 'Input.txt'
OutputFileName = 'Output.txt'

    
class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
    
        self.initUI()
        self.onActivated(0)


    def initUI(self):

        keyLabel = QLabel('Key:')
        self.keyEdit = QLineEdit()


        grid = QGridLayout()
        grid.setSpacing(15)


        self.combo = QComboBox(self)
        self.combo.addItems(["Rail Fence", "Grille", "Vigenere"])
        self.combo.activated[int].connect(self.onActivated)


        btnCipher = QPushButton('Cipher')
        btnCipher.clicked.connect(self.cipherClicked)


        btnEncipher = QPushButton('Encipher')
        btnEncipher.clicked.connect(self.encipherClicked)


        grid.addWidget(self.combo, 1, 0, 1, 2)
        grid.addWidget(keyLabel, 2, 0)
        grid.addWidget(self.keyEdit, 2, 1, 1, 1)
        grid.addWidget(btnCipher, 3, 0)
        grid.addWidget(btnEncipher, 3, 1)
        self.setLayout(grid)


        self.resize(400, 100)
        self.center()
        self.setWindowTitle('Simple cipher algorithms. D. Yaskevich')
        self.show()

    
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def onActivated(self, index):

        if index == 0:
            self.CipherProc = RailFence.CipherRailFence
            self.EncipherProc = RailFence.EncipherRailFence
            self.FileMask = AlphEng
            self.CheckKeyFunc = CheckData.CheckDigitsPositiveStr
            self.keyEdit.setEnabled(True)
            self.keyEdit.setPlaceholderText('Decimal key required...')
        elif index == 1:
            self.CipherProc = Grille.CipherGrille
            self.EncipherProc = Grille.EncipherGrille
            self.FileMask = AlphEng
            self.CheckKeyFunc = CheckData.CheckNothing
            self.keyEdit.setEnabled(False)
            self.keyEdit.setPlaceholderText('No key required.')
        elif index == 2:
            self.CipherProc = Vigenere.CipherVigenere
            self.EncipherProc = Vigenere.EncipherVigenere
            self.FileMask = AlphRus
            self.CheckKeyFunc = CheckData.CheckRusStr
            self.keyEdit.setEnabled(True)
            self.keyEdit.setPlaceholderText('Cyrillic key required...')

        self.keyEdit.clear()


    def isPrepared(self):

        if self.CheckKeyFunc(self.keyEdit.text()):
            if CheckData.CheckFile(InputFileName, self.FileMask):
                return True    
            else:
                QMessageBox.warning(self, 'Message', "Input error occurred!" + "\n" + "Please, try again.", QMessageBox.Ok)    
        else:
            QMessageBox.warning(self, 'Message', "Invalid key!" + "\n" + "Please, try again.", QMessageBox.Ok)
        return False


    def cipherClicked(self):

        if self.isPrepared():
            self.CipherProc(InputFileName, OutputFileName, self.keyEdit.text())


    def encipherClicked(self):

        if self.isPrepared():
            self.EncipherProc(InputFileName, OutputFileName, self.keyEdit.text())



if __name__ == '__main__':

    app = QApplication(sys.argv)
    MW = MainWindow()
    sys.exit(app.exec_())
     