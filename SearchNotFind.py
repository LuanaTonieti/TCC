from PyQt6.QtWidgets import *
from PyQt6 import uic
import SearchOptions
import Menu

class SearchNotFind(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Form, self.Window = uic.loadUiType("SearchNotFind.ui")
        self.window = self.Window()
        self.form = self.Form()
        self.form.setupUi(self.window)
        self.form.pesquisarButton.clicked.connect(self.pesquisar_button_clicked)
        self.form.menuButton.clicked.connect(self.menu_button_clicked)
        
    def pesquisar_button_clicked(self):
        self.window.close()
        self.searchOptions = SearchOptions.SearchOptions()
        self.searchOptions.window.show()

    def menu_button_clicked(self):
        self.window.close()
        self.menu = Menu.Menu()
        self.menu.window.show()