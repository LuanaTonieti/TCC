from PyQt6.QtWidgets import *
from PyQt6 import uic
import MeasureDialog
import UtilsDB
import base64

class MeasureInfo(QMainWindow):
    def __init__(self, nome, altura, largura, comprimento, imagem, data):
        super().__init__()
        self.Form, self.Window = uic.loadUiType("MeasureInfo.ui")
        self.window = self.Window()
        self.form = self.Form()
        self.form.setupUi(self.window)
        self.form.finalizarButton.clicked.connect(self.finalizar_button_clicked)
        self.nome = nome
        self.altura = altura
        self.largura = largura
        self.comprimento = comprimento
        self.imagem = imagem
        self.data = data
        self.show_info(self.altura, self.largura, self.comprimento, self.imagem, self.data)

    def show_info(self, altura, largura, comprimento, imagem, data):
        self.form.alturaText.setText("{:.2f}".format(altura))
        self.form.larguraText.setText("{:.2f}".format(largura))
        self.form.comprimentoText.setText("{:.2f}".format(comprimento))
        self.form.volumeText.setText("{:.2f}".format(altura*largura*comprimento))
        format_string = '%Y-%m-%d'
        data_string = data.strftime(format_string)
        self.form.image.setStyleSheet("background-image : url(" + str(imagem) + ")")
        self.form.dataText.setText(data_string)
        
    def finalizar_button_clicked(self):
        self.imagem = open(self.imagem,'rb').read()
        self.imagem = base64.b64encode(self.imagem)
        result = UtilsDB.inserir(self.nome, self.altura, self.largura, self.comprimento, self.imagem, self.data)
        self.window.close()
        self.measureDialog = MeasureDialog.MeasureDialog(result)
        self.measureDialog.window.show()
