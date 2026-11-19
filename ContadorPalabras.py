import sys
from PyQt5 import QtWidgets, uic

class ContadorPalabras(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('contadorpalabras.ui', self)
        self.btnContar.clicked.connect(self.contarPalabras)

    def contarPalabras(self):
        print("se preciono el texto")
        # recuperar texto
        texto = self.edtCaracteres.text()
        # separar palabras
        textoSeparado = texto.split()
        print(textoSeparado)
        # contar las palabras
        cantidadPalabras = len(textoSeparado)
        print ("cantidad de palabras: ", cantidadPalabras)

app = QtWidgets.QApplication(sys.argv)
ventana = ContadorPalabras()
ventana.show()
sys.exit(app.exec_())