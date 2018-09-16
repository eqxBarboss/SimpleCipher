import sys

from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication, QPushButton,
    QDesktopWidget, QComboBox, QMessageBox)

import RailFence, Grille, Vigenere, CheckData, Kasiski


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


        btnCipher = QPushButton('Encipher')
        btnCipher.clicked.connect(self.EncipherClicked)


        btnEncipher = QPushButton('Decipher')
        btnEncipher.clicked.connect(self.DecipherClicked)


        btnKasiski = QPushButton('Kasiski test')
        btnKasiski.clicked.connect(self.KasiskiClicked)


        grid.addWidget(self.combo, 1, 0, 1, 10)
        grid.addWidget(keyLabel, 2, 0, 1, 1)
        grid.addWidget(self.keyEdit, 2, 1, 1, 9)
        grid.addWidget(btnCipher, 4, 0, 1, 5)
        grid.addWidget(btnEncipher, 4, 5, 1, 5)
        grid.addWidget(btnKasiski, 3, 0, 1, 10)
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
            self.EncipherProc = RailFence.EncipherRailFence
            self.DecipherProc = RailFence.DecipherRailFence
            self.FileMask = AlphEng
            self.CheckKeyFunc = CheckData.CheckDigitsPositiveStr
            self.keyEdit.setEnabled(True)
            self.keyEdit.setPlaceholderText('Decimal key required...')
        elif index == 1:
            self.EncipherProc = Grille.EncipherGrille
            self.DecipherProc = Grille.DecipherGrille
            self.FileMask = AlphEng
            self.CheckKeyFunc = CheckData.CheckNothing
            self.keyEdit.setEnabled(False)
            self.keyEdit.setPlaceholderText('No key required.')
        elif index == 2:
            self.EncipherProc = Vigenere.EncipherVigenere
            self.DecipherProc = Vigenere.DecipherVigenere
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

   
    def EncipherClicked(self):

        if self.isPrepared():
            self.EncipherProc(InputFileName, OutputFileName, self.keyEdit.text())


    def DecipherClicked(self):

        if self.isPrepared():
            self.DecipherProc(InputFileName, OutputFileName, self.keyEdit.text())


    def KasiskiClicked(self):
        if CheckData.CheckFile(InputFileName, AlphRus):
            Kasiski.KasiskiTest(InputFileName, OutputFileName)    
        else:
            QMessageBox.warning(self, 'Message', "Input error occurred!" + "\n" + "Please, try again.", QMessageBox.Ok)      



if __name__ == '__main__':

    app = QApplication(sys.argv)
    MW = MainWindow()
    sys.exit(app.exec_())
     