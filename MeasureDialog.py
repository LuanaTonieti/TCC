from PyQt6.QtWidgets import *
from PyQt6 import uic
import PositionBox
import Menu

class MeasureDialog(QMainWindow):
    def __init__(self, result):
        super().__init__()
        self.Form, self.Window = uic.loadUiType("MeasureDialog.ui")
        self.window = self.Window()
        self.form = self.Form()
        self.form.setupUi(self.window)
        self.set_text_button_label(result)
        self.form.medirButton.clicked.connect(self.medir_button_clicked)
        self.form.menuButton.clicked.connect(self.menu_button_clicked)
        
    def medir_button_clicked(self):
        self.window.close()
        self.positionBox = PositionBox.PositionBox(self.nome)
        self.positionBox.window.show()

    def menu_button_clicked(self):
        self.window.close()
        self.menu = Menu.Menu()
        self.menu.window.show()

    def set_text_button_label(self, result):
        if result:
            self.form.label.setText("Medição feita com sucesso!")
            self.form.medirButton.setText("Nova Medição")
        else:
            self.form.label.setText("Erro na medição.")
            self.form.medirButton.setText("Tentar novamente")