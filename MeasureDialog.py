"""
Codigo que possui a classe para informar o sucesso ou erro da medicao feita
Autor: Luana Watanabe Tonieti
Email: luanawt43@gmail.com
"""

from PyQt6.QtWidgets import *
from PyQt6 import uic
import PositionBox
import Menu

class MeasureDialog(QMainWindow):
    """
    Classe para a janela para informar o usuario se a medicao foi feita com sucesso
    ou se houve algum erro. Carrega a interface criada e define os metodos a serem 
    chamados caso determinados botoes sejam clicados
    """
    def __init__(self, result, nome):
        super().__init__()
        self.Form, self.Window = uic.loadUiType("MeasureDialog.ui")
        self.window = self.Window()
        self.form = self.Form()
        self.form.setupUi(self.window)
        self.set_text_button_label(result)
        self.form.medirButton.clicked.connect(self.medir_button_clicked)
        self.form.menuButton.clicked.connect(self.menu_button_clicked)
        self.nome = nome
        
    def medir_button_clicked(self):
        """
        Metodo que fecha a janela atual e abre a janela para que o usuario
        faca a medicao novamente
        """
        self.window.close()
        self.positionBox = PositionBox.PositionBox(self.nome)
        self.positionBox.window.show()

    def menu_button_clicked(self):
        """
        Metodo que fecha a janela atual e abre a janela do Menu caso o 
        usuario clique no botao menu
        """
        self.window.close()
        self.menu = Menu.Menu()
        self.menu.window.show()

    def set_text_button_label(self, result):
        """
        Metodo que recebe o resultado e mostra ao usuario se a medicao foi 
        feita e salva no db com sucesso ou nao
        :param result: recebe uma bool
        """
        if result:
            self.form.label.setText("Medição feita com sucesso!")
            self.form.medirButton.setText("Nova Medição")
        else:
            self.form.label.setText("Erro na medição.")
            self.form.medirButton.setText("Tentar novamente")