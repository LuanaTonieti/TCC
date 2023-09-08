from PyQt6.QtWidgets import *
from PyQt6 import uic
import InsertName
import SearchOptions
import EditID

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Form, self.Window = uic.loadUiType("Menu.ui")
        self.window = self.Window()
        self.form = self.Form()
        self.form.setupUi(self.window)
        self.form.medirButton.clicked.connect(self.medir_button_clicked)
        self.form.procurarButton.clicked.connect(self.procurar_button_clicked)
        self.form.editarButton.clicked.connect(self.editar_button_clicked)

    def medir_button_clicked(self):
        self.window.close()
        self.insertName = InsertName.InsertName()
        self.insertName.window.show()
    
    def procurar_button_clicked(self):
        self.window.close()
        self.insertName = SearchOptions.SearchOptions()
        self.insertName.window.show()

    def editar_button_clicked(self):
        self.window.close()
        self.editID = EditID.EditID()
        self.editID.window.show()