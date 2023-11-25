"""
Codigo que possui a classe para a janela para o usuario entrar com o codigo 
da medicao ele deseja modificar as informacoes
Autor: Luana Watanabe Tonieti
Email: luanawt43@gmail.com
"""

from PyQt6.QtWidgets import *
from PyQt6 import uic
import Menu
import EditOptions
import UtilsDB
import EditDialog

class EditID(QMainWindow):
    """
    Classe para a janela em que o usuario deve inserir o codigo da medicao a ser editada. 
    Carrega a interface criada e define os metodos a serem chamados caso determinados 
    botoes sejam clicados. Recebe o nome e as informacoes obtidas atraves das medicoes
    """
    def __init__(self):
        super().__init__()
        self.Form, self.Window = uic.loadUiType("EditID.ui")
        self.window = self.Window()
        self.form = self.Form()
        self.form.setupUi(self.window)
        self.form.voltarButton.clicked.connect(self.voltar_button_clicked)
        self.form.continuarButton.clicked.connect(self.continuar_button_clicked)

    def voltar_button_clicked(self):
        """
        Metodo que fecha a janela atual e abre a janela do menu
        """
        self.window.close()
        self.menu = Menu.Menu()
        self.menu.window.show()

    def continuar_button_clicked(self):
        """
        Metodo que fecha a janela atual e abre a janela para o usuario prosseguir com 
        a edicao
        """
        self.codigoEdit = self.form.codigoText.text()
        self.window.close()
        if UtilsDB.verificar_existencia(self.codigoEdit):
            self.editOptions = EditOptions.EditOptions(self.codigoEdit)
            self.editOptions.window.show()
        else:
            self.editSucess = EditDialog.EditDialog(False, False)
            self.editSucess.window.show()