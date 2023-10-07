"""
Codigo que possui a classe para a janela que informa o usuario caso a pesquisa
feita nao tenha resultados
Autor: Luana Watanabe Tonieti
Email: luanawt43@gmail.com
"""

from PyQt6.QtWidgets import *
from PyQt6 import uic
import SearchOptions
import Menu

class SearchNotFind(QMainWindow):
    """
    Classe para a janela de pesquisa nao encontrada. Carrega a interface criada e define os
    metodos a serem chamados caso determinados botoes sejam clicados
    """
    def __init__(self):
        super().__init__()
        self.Form, self.Window = uic.loadUiType("SearchNotFind.ui")
        self.window = self.Window()
        self.form = self.Form()
        self.form.setupUi(self.window)
        self.form.pesquisarButton.clicked.connect(self.pesquisar_button_clicked)
        self.form.menuButton.clicked.connect(self.menu_button_clicked)
        
    def pesquisar_button_clicked(self):
        """
        Metodo que fecha a janela atual e abre a janela para fazer pesquisas no db
        """
        self.window.close()
        self.searchOptions = SearchOptions.SearchOptions()
        self.searchOptions.window.show()

    def menu_button_clicked(self):
        """
        Metodo que fecha a janela atual e abre a janela do menu
        """
        self.window.close()
        self.menu = Menu.Menu()
        self.menu.window.show()