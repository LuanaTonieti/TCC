"""
Codigo que possui a classe para a janela que informa o usuario para posicionar
a caixa a ser medida
Autor: Luana Watanabe Tonieti
Email: luanawt43@gmail.com
"""

from PyQt6.QtWidgets import *
from PyQt6 import uic
import InsertName
import MeasureInfo
from datetime import date

class PositionBox(QMainWindow):
    """
    Classe para a janela para pedir para o usuario posicionar a caixa para que a medicao
    possa ser feita. Carrega a interface criada e define os metodos a serem chamados
    caso determinados botoes sejam clicados
    """
    def __init__(self, nome):
        """
        :param nome: recebe uma string
        """
        super().__init__()
        self.Form, self.Window = uic.loadUiType("PositionBox.ui")
        self.window = self.Window()
        self.form = self.Form()
        self.form.setupUi(self.window)
        self.form.voltarButton.clicked.connect(self.voltar_button_clicked)
        self.form.medirButton.clicked.connect(self.medir_button_clicked)
        self.nome = nome

    def voltar_button_clicked(self):
        """
        Metodo que fecha a janela atual e abre a janela para inserir o nome do
        projeto caso o usuario clique para voltar
        """
        self.window.close()
        self.insertName = InsertName.InsertName()
        self.insertName.window.show()

    def medir_button_clicked(self):
        """
        Metodo que ira pegar as informacoes obtida pela camera e pelo ultrassonico
        e ira fechar a janela atual, abrindo a janela que mostra as informacoes para 
        o usuario
        """
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