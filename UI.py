"""
Codigo principal. Inicializa bre a janela de menu para que o usuario possa escolher
o que deseja fazer
Autor: Luana Watanabe Tonieti
Email: luanawt43@gmail.com
"""

from PyQt6.QtWidgets import *
import sys
import Menu

app=QApplication(sys.argv)
menu = Menu.Menu()
menu.window.show()
app.exec()