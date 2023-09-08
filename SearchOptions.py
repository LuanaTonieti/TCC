from PyQt6.QtWidgets import *
from PyQt6 import uic
import Menu
import UtilsDB

class SearchOptions(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Form, self.Window = uic.loadUiType("SearchOptions.ui")
        self.window = self.Window()
        self.form = self.Form()
        self.form.setupUi(self.window)
        self.form.pesquisarButton.clicked.connect(self.pesquisar_button_clicked)
        self.form.voltarButton.clicked.connect(self.voltar_button_clicked)
        
    def voltar_button_clicked(self):
        self.window.close()
        self.menu = Menu.Menu()
        self.menu.window.show()

    def pesquisar_button_clicked(self):
        self.window.close()
        self.utilsDB = UtilsDB.UtilsDB()
        self.utilsDB.window.show()
        self.projectName = ''
        if self.form.tudoRB.isChecked():
            self.utilsDB.pesquisar(0, '', '', 0, '')
        else:
            if self.form.nomeRB.isChecked():
                self.projectName = self.form.nomeText.text()
            if self.form.idRB.isChecked():
                self.utilsDB.pesquisar(1, 'codigo', '', self.form.idText.text(), self.projectName)
            elif self.form.alturaRB.isChecked():
                self.utilsDB.pesquisar(2, 'altura', self.form.alturaCB.currentText(), self.form.alturaText.text(), self.projectName)
            elif self.form.larguraRB.isChecked():
                self.utilsDB.pesquisar(2, 'largura', self.form.larguraCB.currentText(), self.form.larguraText.text(), self.projectName)
            elif self.form.comprimentoRB.isChecked():
                self.utilsDB.pesquisar(2, 'largura', self.form.comprimentoCB.currentText(), self.form.comprimentoText.text(), self.projectName)
            elif self.form.volumeRB.isChecked():
                self.utilsDB.pesquisar(2, 'altura*largura*comprimento', self.form.volumeCB.currentText(), self.form.volumeText.text(), self.projectName)
            elif self.form.dataRB.isChecked():
                self.utilsDB.pesquisar(2, 'data_imagem', self.form.dataCB.currentText(), self.form.data.date().toPyDate(), self.projectName)
            else:
                self.utilsDB.pesquisar(1, 'nome_projeto', '', self.projectName, '')
