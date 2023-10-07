"""
Codigo que possui a classe para a janela de opcoes de busca
Autor: Luana Watanabe Tonieti
Email: luanawt43@gmail.com
"""

from PyQt6.QtWidgets import *
from PyQt6 import uic
import Menu
import UtilsDB
import SearchNotFind

class SearchOptions(QMainWindow):
    """
    Classe para a janela de opcoes de busca. Carrega a interface criada e define os
    metodos a serem chamados caso determinados botoes sejam clicados
    """
    def __init__(self):
        super().__init__()
        self.Form, self.Window = uic.loadUiType("SearchOptions.ui")
        self.window = self.Window()
        self.form = self.Form()
        self.form.setupUi(self.window)
        self.form.pesquisarButton.clicked.connect(self.pesquisar_button_clicked)
        self.form.voltarButton.clicked.connect(self.voltar_button_clicked)
        
    def voltar_button_clicked(self):
        """
        Metodo que fecha a janela atual e abre a janela do Menu caso o 
        usuario clique para voltar
        """
        self.window.close()
        self.menu = Menu.Menu()
        self.menu.window.show()

    def pesquisar_button_clicked(self):
        """
        Metodo responsavel por montar a query de acordo com o que o usuario
        colocou na GUI. No final, fecha a janela atual e abre a janela
        mostrando o resultado da pesquisa
        """
        self.utilsDB = UtilsDB.UtilsDB()
        self.query = ''

        operations = {
            "Maior que": ">",
            "Menor que": "<",
            "Igual a": "=",
            "Depois de": ">",
            "Antes de": "<",
            "Na data de": "="
        }

        if self.form.tudoRB.isChecked():
            self.window.close()
            self.utilsDB.window.show()
            self.utilsDB.pesquisar(self.query, 0)
        else:
            if self.form.nomeRB.isChecked() and len(self.form.nomeText.text()) != 0 :
                self.query += f" AND nome_projeto = '{self.form.nomeText.text()}'"
            if self.form.idRB.isChecked() and len(self.form.idText.text()) != 0:
                self.query += f" AND codigo = {self.form.idText.text()}"
            if self.form.alturaRB.isChecked() and len(self.form.alturaText.text()) != 0:
                self.query += f" AND altura {operations[self.form.alturaCB.currentText()]} {self.form.alturaText.text()}"
            if self.form.larguraRB.isChecked() and len(self.form.larguraText.text()) != 0:
                self.query += f" AND largura {operations[self.form.larguraCB.currentText()]} {self.form.larguraText.text()}"
            if self.form.comprimentoRB.isChecked() and len(self.form.comprimentoText.text()) != 0:
                self.query += f" AND comprimento {operations[self.form.comprimentoCB.currentText()]} {self.form.comprimentoText.text()}"
            if self.form.volumeRB.isChecked() and len(self.form.volumeText.text()) != 0:
                self.query += f" AND altura*largura*comprimento {operations[self.form.volumeCB.currentText()]} {self.form.volumeText.text()}"
            if self.form.dataRB.isChecked():
                self.query += f" AND data_imagem {operations[self.form.dataCB.currentText()]} '{self.form.data.date().toPyDate()}'"
            if len(self.query) != 0:
                self.window.close()
                self.utilsDB.window.show()
                self.utilsDB.pesquisar(self.query[4:], 1)
            else:
                self.window.close()
                self.searchNotFind = SearchNotFind.SearchNotFind()
                self.searchNotFind.window.show()
