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
        self.tvPalabras.setText(f"{cantidadPalabras}")
        # contar caracteres
        # cantidadCaracteres = len(texto)
        # self.tvCaracteres.setText(f"{cantidadCaracteres}")
        totalCaracteres = 0
        for palabra in textoSeparado:
            totalCaracteres += len(palabra)
        totalCaracteres
        self.tvCaracteres.setText(f"{totalCaracteres}")

app = QtWidgets.QApplication(sys.argv)
ventana = ContadorPalabras()
ventana.show()
sys.exit(app.exec_())