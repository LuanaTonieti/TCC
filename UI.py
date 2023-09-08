from PyQt6.QtWidgets import *
import sys
import Menu

app=QApplication(sys.argv)
menu = Menu.Menu()
menu.window.show()
app.exec()