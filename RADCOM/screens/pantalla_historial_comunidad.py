from PyQt5.QtWidgets import QWidget, QApplication
from screens.pantalla_historial_comunidad_ui import Ui_Form  # Importa la clase generada por Qt Designer
import sys

class PantallaHistorialComunidad(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Instancia de la clase generada por Qt Designer
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # Configura la UI

        # Aquí puedes agregar más funcionalidades o conectores si es necesario
        self.setup_connections()

    def setup_connections(self):
        # Aquí puedes conectar señales a slots, por ejemplo:
        # self.ui.someButton.clicked.connect(self.some_function)
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PantallaHistorialComunidad()  # Cambiar a la clase correcta
    window.show()
    sys.exit(app.exec_())
