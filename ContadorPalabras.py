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

        if cantidadPalabras >= 20:
            self.tvPalabras.setStyleSheet("color: red;")
            self.label_2.setStyleSheet("color: red;")
        else:
            self.tvPalabras.setStyleSheet("color: white;")
            self.label_2.setStyleSheet("color: white;")

        if totalCaracteres >= 120:
            self.tvCaracteres.setStyleSheet("color: red;")
            self.label_3.setStyleSheet("color: red;")
        else:
            self.tvCaracteres.setStyleSheet("color: white;")
            self.label_3.setStyleSheet("color: white;")

app = QtWidgets.QApplication(sys.argv)
ventana = ContadorPalabras()
ventana.show()
sys.exit(app.exec_())