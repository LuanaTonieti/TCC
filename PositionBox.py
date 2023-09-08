from PyQt6.QtWidgets import *
from PyQt6 import uic
import InsertName
import MeasureInfo
from datetime import date

class PositionBox(QMainWindow):
    def __init__(self, nome):
        super().__init__()
        self.Form, self.Window = uic.loadUiType("PositionBox.ui")
        self.window = self.Window()
        self.form = self.Form()
        self.form.setupUi(self.window)
        self.form.voltarButton.clicked.connect(self.voltar_button_clicked)
        self.form.medirButton.clicked.connect(self.medir_button_clicked)
        self.nome = nome

    def voltar_button_clicked(self):
        self.window.close()
        self.insertName = InsertName.InsertName()
        self.insertName.window.show()

    def medir_button_clicked(self):
        # abrir webcam e pegar a imagem, pegar os dados obtidos pelos sensores
        print("Medindo...")
        data = date.today()
        imagem = 'dog.png'
        altura = 57.4
        largura = 87.1
        comprimento = 441.92
        self.window.close()
        self.measureInfo = MeasureInfo.MeasureInfo(self.nome, altura, largura, comprimento, imagem, data)
        self.measureInfo.window.show()