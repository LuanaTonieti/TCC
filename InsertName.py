from PyQt6.QtWidgets import *
from PyQt6 import uic
import PositionBox
import Menu

class InsertName(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Form, self.Window = uic.loadUiType("InsertName.ui")
        self.window = self.Window()
        self.form = self.Form()
        self.form.setupUi(self.window)
        self.form.prontoButton.clicked.connect(self.pronto_button_clicked)
        self.form.voltarButton.clicked.connect(self.voltar_button_clicked)
        
    def pronto_button_clicked(self):
        self.projectName = self.form.projectName.toPlainText()
        self.window.close()
        self.positionBox = PositionBox.PositionBox(self.projectName)
        self.positionBox.window.show()

    def voltar_button_clicked(self):
        self.window.close()
        self.menu = Menu.Menu()
        self.menu.window.show()