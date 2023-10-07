"""
Codigo que possui a classe para a janela para mostrar os resultados da medicao
Autor: Luana Watanabe Tonieti
Email: luanawt43@gmail.com
"""

from PyQt6.QtWidgets import *
from PyQt6 import uic
import MeasureDialog
import UtilsDB
import base64

class MeasureInfo(QMainWindow):
    """
    Classe para a janela de apresentacao dos resultados da medicao feita. Carrega a 
    interface criada e define os metodos a serem chamados caso determinados botoes 
    sejam clicados. Recebe o nome e as informacoes obtidas atraves das medicoes
    """
    def __init__(self, nome, altura, largura, comprimento, imagem, data):
        """
        :param nome: recebe uma string
        :param altura: recebe um float
        :param largura: recebe um float
        :param comprimento: recebe um float
        :param imagem: recebe uma string
        :param data: recebe uma data
        """
        super().__init__()
        self.Form, self.Window = uic.loadUiType("MeasureInfo.ui")
        self.window = self.Window()
        self.form = self.Form()
        self.form.setupUi(self.window)
        self.nome = nome
        self.altura = altura
        self.largura = largura
        self.comprimento = comprimento
        self.imagem = imagem
        self.data = data
        self.form.finalizarButton.clicked.connect(self.finalizar_button_clicked)
        self.show_info(self.altura, self.largura, self.comprimento, self.imagem, self.data)

    def show_info(self, altura, largura, comprimento, imagem, data):
        """
        Metodo que coloca as informacoes obtidas na interface para que o
        usuario possa ver o resultado
        """
        self.form.alturaText.setText("{:.2f}".format(altura))
        self.form.larguraText.setText("{:.2f}".format(largura))
        self.form.comprimentoText.setText("{:.2f}".format(comprimento))
        self.form.volumeText.setText("{:.2f}".format(altura*largura*comprimento))
        format_string = '%Y-%m-%d'
        data_string = data.strftime(format_string)
        self.form.image.setStyleSheet("background-image : url(" + str(imagem) + ")")
        self.form.dataText.setText(data_string)
        
    def finalizar_button_clicked(self):
        """
        Metodo que salva as informacoes no banco de dados e fecha a janela 
        atual, abrindo uma janela informando se esta operacao foi feita com
        sucesso ou nao
        """
        self.imagem = open(self.imagem,'rb').read()
        self.imagem = base64.b64encode(self.imagem)
        result = UtilsDB.inserir(self.nome, self.altura, self.largura, self.comprimento, self.imagem, self.data)
        self.window.close()
        self.measureDialog = MeasureDialog.MeasureDialog(result)
        self.measureDialog.window.show()
