"""
Codigo que possui a classe para a janela que informa o usuario se a edicao foi
feita com sucesso ou nao
Autor: Luana Watanabe Tonieti
Email: luanawt43@gmail.com
"""

from PyQt6.QtWidgets import *
from PyQt6 import uic
import EditID
import Menu

class EditDialog(QMainWindow):
    """
    Classe para a janela de apresentacao dos resultados da edicao feita. Carrega a 
    interface criada e define os metodos a serem chamados caso determinados botoes 
    sejam clicados. Recebe o nome e as informacoes obtidas atraves das medicoes
    """
    def __init__(self, result):
        """
        :param result: recebe uma bool
        """
        super().__init__()
        self.Form, self.Window = uic.loadUiType("EditDialog.ui")
        self.window = self.Window()
        self.form = self.Form()
        self.form.setupUi(self.window)
        self.set_text_button_label(result)
        self.form.editarButton.clicked.connect(self.editar_button_clicked)
        self.form.menuButton.clicked.connect(self.menu_button_clicked)
        
    def editar_button_clicked(self):
        """
        Metodo que fecha a janela atual e abre a janela para entrar com o codigo da
        medicao que sera editada
        """
        self.window.close()
        self.editID = EditID.EditID()
        self.editID.window.show()

    def menu_button_clicked(self):
        """
        Metodo que fecha a janela atual e abre a janela do menu
        """
        self.window.close()
        self.menu = Menu.Menu()
        self.menu.window.show()

    def set_text_button_label(self, result):
        """
        Metodo que escreve no label se a edicao foi feita com sucesso ou nao
        :param result: recebe uma bool
        """
        if result:
            self.form.label.setText("Edição feita com sucesso!")
            self.form.editarButton.setText("Nova Edição")
        else:
            self.form.label.setText("Erro na edição.")
            self.form.editarButton.setText("Tentar Novamente")