"""
Codigo que possui a classe para a janela na qual o usuario deve informar o nome do projeto
ao qual a medicao que sera feita pertence
Autor: Luana Watanabe Tonieti
Email: luanawt43@gmail.com
"""

from PyQt6.QtWidgets import *
from PyQt6 import uic
import PositionBox
import Menu

class InsertName(QMainWindow):
    """
    Classe para a janela do nome do projeto. Carrega a interface criada e define os
    metodos a serem chamados caso determinados botoes sejam clicados
    """
    def __init__(self):
        super().__init__()
        self.Form, self.Window = uic.loadUiType("InsertName.ui")
        self.window = self.Window()
        self.form = self.Form()
        self.form.setupUi(self.window)
        self.form.prontoButton.clicked.connect(self.pronto_button_clicked)
        self.form.voltarButton.clicked.connect(self.voltar_button_clicked)
        
    def pronto_button_clicked(self):
        """
        Metodo que fecha a janela atual e abre a janela para o usuario continuar
        com a medicao
        """
        self.projectName = self.form.projectName.toPlainText()
        self.window.close()
        self.positionBox = PositionBox.PositionBox(self.projectName)
        self.positionBox.window.show()

    def voltar_button_clicked(self):
        """
        Metodo que fecha a janela atual e abre a janela de menu
        """
        self.window.close()
        self.menu = Menu.Menu()
        self.menu.window.show()