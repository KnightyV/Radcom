import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from screens.inicio_sesion import PantallaInicioSesion
from screens.pantalla_principal_admin import PantallaPrincipalAdmin
from screens.base_screen import BaseScreen  # Asegúrate de que BaseScreen esté importado

class MainWindow(BaseScreen):  # Hereda de BaseScreen para utilizar la barra personalizada
    def __init__(self):
        super().__init__(title="RADCOM")  # Pasamos el título a BaseScreen
        self.setGeometry(100, 100, 1320, 760)  # Tamaño de la ventana principal

        # Crear QStackedWidget para manejar las pantallas
        self.stacked_widget = QStackedWidget()

        # Crear las pantallas
        self.pantalla_inicio = PantallaInicioSesion(self)
        self.pantalla_principal_admin = PantallaPrincipalAdmin(self)

        # Añadir las pantallas al QStackedWidget

        #NO OLVIDES QUITAR LOS SIGUIENTES COMENTARIOS
        
        #self.stacked_widget.addWidget(self.pantalla_inicio)
        self.stacked_widget.addWidget(self.pantalla_principal_admin)

        # Añadir el QStackedWidget al layout principal de BaseScreen
        self.layout().insertWidget(1, self.stacked_widget)  # Insertar debajo de la barra de título
        self.stacked_widget.setCurrentIndex(0)  # Mostrar la pantalla de inicio de sesión

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
