from PyQt6.QtWidgets import *
from PyQt6 import uic
import EditID
import UtilsDB
import EditDialog
from datetime import date

class EditOptions(QMainWindow):
    def __init__(self, codigo):
        super().__init__()
        self.Form, self.Window = uic.loadUiType("EditOptions.ui")
        self.window = self.Window()
        self.form = self.Form()
        self.form.setupUi(self.window)
        self.form.voltarButton.clicked.connect(self.voltar_button_clicked)
        self.form.editarButton.clicked.connect(self.editar_button_clicked)
        self.codigo = codigo

    def voltar_button_clicked(self):
        self.window.close()
        self.editID = EditID.EditID()
        self.editID.window.show()

    def editar_button_clicked(self):
        self.window.close()
        query = ''
        result = False
        if self.form.excluirRB.isChecked():
            UtilsDB.deletar(self.codigo)
        else:
            if self.form.nomeRB.isChecked():
                query += f", nome_projeto = '{self.form.nomeText.text()}'"
            if self.form.alturaRB.isChecked():
                query += f", altura = {self.form.alturaText.text()}"
            if self.form.larguraRB.isChecked():
                query += f", largura = {self.form.larguraText.text()}"
            if self.form.comprimentoRB.isChecked():
                query += f", comprimento = {self.form.comprimentoText.text()}"
            if self.form.dataRB.isChecked():
                # print(f", data_imagem = '{self.form.data.date().toPyDate().strftime('%Y-%m-%d')}'")
                query += f", data_imagem = '{self.form.data.date().toPyDate().strftime('%Y-%m-%d')}'"
            if query:
                result = UtilsDB.atualizar(query[1:], self.codigo)
        self.editSucess = EditDialog.EditDialog(result)
        self.editSucess.window.show()