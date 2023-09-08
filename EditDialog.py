from PyQt6.QtWidgets import *
from PyQt6 import uic
import EditID
import Menu

class EditDialog(QMainWindow):
    def __init__(self, result):
        super().__init__()
        self.Form, self.Window = uic.loadUiType("EditDialog.ui")
        self.window = self.Window()
        self.form = self.Form()
        self.form.setupUi(self.window)
        self.set_text_button_label(result)
        self.form.editarButton.clicked.connect(self.editar_button_clicked)
        self.form.menuButton.clicked.connect(self.menu_button_clicked)
        
    def editar_button_clicked(self):
        self.window.close()
        self.editID = EditID.EditID()
        self.editID.window.show()

    def menu_button_clicked(self):
        self.window.close()
        self.menu = Menu.Menu()
        self.menu.window.show()

    def set_text_button_label(self, result):
        if result:
            self.form.label.setText("Edição feita com sucesso!")
            self.form.editarButton.setText("Nova Edição")
        else:
            self.form.label.setText("Erro na edição.")
            self.form.editarButton.setText("Tentar novamente")