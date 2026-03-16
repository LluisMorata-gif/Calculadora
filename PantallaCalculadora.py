import self
from PySide6 import QtWidgets

from pantalla import Ui_Calculadora


class PantallaCalculadora(QtWidgets.QMainWindow, Ui_Calculadora):
    """Clase básica de la interfaz generada por QtDesigner"""

    def __init__(self, parent=None):

        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def opera(self):
        # Metodo que se LLamará al hacer clic en el botón de operar
        pass

    def verifica(self):
        # Metodo que se llamará al hacer clic en el botón de operan
        pass

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = PantallaCalculadora()
    window.show()
    sys.exit(app.exec_())
