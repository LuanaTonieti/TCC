from PyQt6.QtWidgets import *
from PyQt6 import uic
import Menu
import EditOptions

class EditID(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Form, self.Window = uic.loadUiType("EditID.ui")
        self.window = self.Window()
        self.form = self.Form()
        self.form.setupUi(self.window)
        self.form.voltarButton.clicked.connect(self.voltar_button_clicked)
        self.form.continuarButton.clicked.connect(self.continuar_button_clicked)

    def voltar_button_clicked(self):
        self.window.close()
        self.menu = Menu.Menu()
        self.menu.window.show()

    def continuar_button_clicked(self):
        self.codigoEdit = self.form.codigoText.text()
        self.window.close()
        self.editOptions = EditOptions.EditOptions(self.codigoEdit)
        self.editOptions.window.show()