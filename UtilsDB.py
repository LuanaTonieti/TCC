from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtGui import QPixmap
import MySQLdb
import Menu
import base64
import SearchOptions
import SearchNotFind

class UtilsDB(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Form, self.Window = uic.loadUiType("ShowSearch.ui")
        self.window = self.Window()
        self.form = self.Form()
        self.form.setupUi(self.window)
        self.form.voltarButton.clicked.connect(self.voltar_button_clicked)
        self.form.pesquisarButton.clicked.connect(self.pesquisar_button_clicked)
    
    def voltar_button_clicked(self):
        self.window.close()
        self.menu = Menu.Menu()
        self.menu.window.show()

    def pesquisar_button_clicked(self):
        self.window.close()
        self.searchOptions = SearchOptions.SearchOptions()
        self.searchOptions.window.show()

    def pesquisar(self, opcao, campo, operacao, valor, projectName):

        operations = {
            "Maior que": ">",
            "Menor que": "<",
            "Igual a": "=",
            "Depois de": ">",
            "Antes de": "<",
            "Na data de": "="
        }

        if not projectName:
            searchProject = ''
        else:
            searchProject = f"AND nome_projeto = '{projectName}'"

        conn = conectar()
        cursor = conn.cursor()
        if opcao == 0: 
            cursor.execute('SELECT * FROM medidas')
        elif opcao == 1: 
            cursor.execute(f"SELECT * FROM medidas WHERE {campo} = '{valor}' {searchProject}")
        elif opcao == 2: 
            cursor.execute(f"SELECT * FROM medidas WHERE {campo} {operations[operacao]} '{valor}' {searchProject}")
        
        medidas = cursor.fetchall()

        if len(medidas) == 0:
            self.window.close()
            self.searchNotFind = SearchNotFind.SearchNotFind()
            self.searchNotFind.window.show()
        else:
            row_len = []
            for i in medidas:
                row_len.append(len(i))
            col_num = max(row_len)
            self.form.tableWidget.setRowCount(0)	
            self.form.tableWidget.setColumnCount(int(col_num)+1)
            self.form.tableWidget.setHorizontalHeaderLabels(('Código', 'Nome', 'Altura [cm]', 'Largura [cm]', 'Comprimento [cm]', 'Volume [cm3]', 'Imagem', 'Data'))
                
            for row, row_data in enumerate(medidas):
                self.form.tableWidget.insertRow(row)
                row_data = list(row_data)
                volume = 1
                row_data.insert(5, volume)
                for col, col_data in enumerate(row_data):
                    if col >= 2 and col <= 4:
                        volume *= col_data
                        if col == 4:
                            row_data[5] = "{:.2f}".format(volume)
                    if col == 7:
                        col_data = col_data.strftime('%d-%m-%Y')
                    if col == 6:
                        pix = QPixmap()
                        self.label = QLabel()
                        if pix.loadFromData(base64.b64decode(col_data)):
                            self.label.setPixmap(pix)
                            self.label.setScaledContents(True)
                            self.form.tableWidget.setCellWidget(row, col, self.label)
                    else:
                        self.form.tableWidget.setItem(row, col, QTableWidgetItem(str(col_data)))
        desconectar(conn)


def conectar(): # Faz a conexao com o db. Retorna True se foi feita com sucesso e False se deu erro
    result = True
    try:
        conn = MySQLdb.connect(
            db = 'TCC',
            host = 'localhost',
            user = 'luana',
            passwd = 'luana'
        )
        return conn
    except MySQLdb.Error as e:
        result = False 
    return result


def desconectar(conn): # Desconecta do db
    if conn:
        conn.close()


def inserir(nome, altura, largura, comprimento, imagem, data): # Insere os dados no db
    conn = conectar()
    cursor = conn.cursor()
    args = (nome, altura, largura, comprimento, imagem, data)
    query = 'INSERT INTO medidas (nome_projeto, altura, largura, comprimento, imagem, data_imagem) VALUES(%s, %s, %s, %s, %s, %s)'
    cursor.execute(query,args)
    conn.commit()
    result = False
    if cursor.rowcount == 1: # sucesso
        result = True
    desconectar(conn)
    return result


def atualizar(query, codigo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"UPDATE medidas SET {query} WHERE codigo={codigo}")
    conn.commit()
    result = False
    if cursor.rowcount == 1: # verifica de atualizou com sucesso
        result = True
    desconectar(conn)
    return result


def deletar(codigo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM medidas WHERE codigo={codigo}")
    conn.commit()
    result = False
    if cursor.rowcount == 1: # sucesso
        result = True
    desconectar(conn)
    return result