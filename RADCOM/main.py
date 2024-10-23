import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from screens.inicio_sesion import PantallaInicioSesion
from screens.pantalla_principal_admin import PantallaPrincipalAdmin
from screens.pantalla_principal_facturador import PantallaPrincipalFacturador
from screens.pantalla_principal_cobrador import PantallaPrincipalCobrador
from screens.base_screen import BaseScreen  # Asegúrate de que BaseScreen esté importado

class MainWindow(BaseScreen):  # Hereda de BaseScreen para utilizar la barra personalizada
    def __init__(self):
        super().__init__(title="RADCOM")  # Pasamos el título a BaseScreen
        self.setGeometry(100, 100, 1320, 800)  # Tamaño de la ventana principal

        # Crear QStackedWidget para manejar las pantallas
        self.stacked_widget = QStackedWidget()

        # Crear las pantallas
        #self.pantalla_inicio = PantallaInicioSesion(self)
        #self.pantalla_principal_admin = PantallaPrincipalAdmin(self)
        #self.pantalla_principal_facturador = PantallaPrincipalFacturador(self)
        self.pantalla_principal_cobrador = PantallaPrincipalCobrador(self)

        # Añadir las pantallas al QStackedWidget
        #self.stacked_widget.addWidget(self.pantalla_inicio)
        #self.stacked_widget.addWidget(self.pantalla_principal_admin)
        #self.stacked_widget.addWidget(self.pantalla_principal_facturador)
        self.stacked_widget.addWidget(self.pantalla_principal_cobrador)

        # Añadir el QStackedWidget al layout de contenido en BaseScreen
        self.layout().insertWidget(1, self.stacked_widget)

        # Establecer la pantalla de inicio
        self.stacked_widget.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()  # Esto es crucial para que la ventana se muestre
    sys.exit(app.exec_())
