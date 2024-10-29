import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget, QWidget, QVBoxLayout

from screens.inicio_sesion import PantallaInicioSesion
from screens.pantalla_inicio import PantallaInicio
from screens.pantalla_principal_admin import PantallaPrincipalAdmin
from screens.pantalla_principal_facturador import PantallaPrincipalFacturador
from screens.pantalla_principal_cobrador import PantallaPrincipalCobrador
from screens.pantalla_cobro_admin import PantallaCobroAdmin
from screens.pantalla_cobro_facturador import PantallaCobroFacturador
from screens.pantalla_cobro_cobrador import PantallaCobroCobrador
from screens.pantalla_adeudo_admin import PantallaAdeudoAdmin
from screens.pantalla_adeudo_facturador import PantallaAdeudoFacturador
from screens.pantalla_adeudo_cobrador import PantallaAdeudoCobrador
from screens.pantalla_factura_pendiente_admin import PantallaFacturaPendienteAdmin
from screens.pantalla_factura_nueva_admin import PantallaFacturaNuevaAdmin
from screens.pantalla_factura_facturador import PantallaFacturaFacturador
from screens.pantalla_historial_cliente import PantallaHistorialCliente
from screens.pantalla_historial_comunidad import PantallaHistorialComunidad
from screens.pantalla_historial_municipio import PantallaHistorialMunicipio
from screens.pantalla_historial_antena import PantallaHistorialAntena
from screens.pantalla_historial_global import PantallaHistorialGlobal
from screens.pantalla_modificar import PantallaModificar
from screens.pantalla_crearS_cliente import PantallaCrearSCliente
from screens.pantalla_crearS_comunidad import PantallaCrearSComunidad
from screens.pantalla_crearS_municipio import PantallaCrearSMunicipio
from screens.pantalla_crearS_antena import PantallaCrearSAntena

class MainWindow(QWidget):  # Cambia BaseScreen a QWidget
    def __init__(self):
        super().__init__()  # Quita el título de la llamada
        self.setGeometry(100, 100, 1320, 800)  # Tamaño de la ventana principal

        # Crear QStackedWidget para manejar las pantallas
        self.stacked_widget = QStackedWidget()

        # Crear las pantallas
        #self.pantalla_inicio = PantallaInicioSesion(self)
        self.pantalla_inicio = PantallaInicio(self)
        self.pantalla_principal_admin = PantallaPrincipalAdmin(self)
        self.pantalla_principal_facturador = PantallaPrincipalFacturador(self)
        self.pantalla_principal_cobrador = PantallaPrincipalCobrador(self)
        self.pantalla_cobro_admin = PantallaCobroAdmin(self)
        self.pantalla_cobro_facturador = PantallaCobroFacturador(self)
        self.pantalla_cobro_cobrador = PantallaCobroCobrador(self)
        self.pantalla_adeudo_admin = PantallaAdeudoAdmin(self)
        self.pantalla_adeudo_facturador = PantallaAdeudoFacturador(self)
        self.pantalla_adeudo_cobrador = PantallaAdeudoCobrador(self)
        self.pantalla_factura_pendiente_admin = PantallaFacturaPendienteAdmin(self)
        self.pantalla_factura_nueva_admin = PantallaFacturaNuevaAdmin(self)
        self.pantalla_factura_facturador = PantallaFacturaFacturador(self)
        self.pantalla_hitorial_cliente = PantallaHistorialCliente(self)
        self.pantalla_historial_comunidad = PantallaHistorialComunidad(self)
        self.pantalla_historial_municipio = PantallaHistorialMunicipio(self)
        self.pantalla_historial_antena = PantallaHistorialAntena(self)
        self.pantalla_historial_global = PantallaHistorialGlobal(self)
        self.pantalla_modificar = PantallaModificar(self)
        self.pantalla_crearS_cliente = PantallaCrearSCliente(self)
        self.pantalla_crearS_comunidad = PantallaCrearSComunidad(self)
        self.pantalla_crearS_municipio = PantallaCrearSMunicipio(self)
        self.pantalla_crearS_antena = PantallaCrearSAntena(self)

        # Añadir las pantallas al QStackedWidget
        #self.stacked_widget.addWidget(self.pantalla_inicio)
        self.stacked_widget.addWidget(self.pantalla_inicio)
        self.stacked_widget.addWidget(self.pantalla_principal_admin)
        self.stacked_widget.addWidget(self.pantalla_principal_facturador)
        self.stacked_widget.addWidget(self.pantalla_principal_cobrador)
        self.stacked_widget.addWidget(self.pantalla_cobro_admin)
        self.stacked_widget.addWidget(self.pantalla_cobro_facturador)
        self.stacked_widget.addWidget(self.pantalla_cobro_cobrador)
        self.stacked_widget.addWidget(self.pantalla_adeudo_admin)
        self.stacked_widget.addWidget(self.pantalla_adeudo_facturador)
        self.stacked_widget.addWidget(self.pantalla_adeudo_cobrador)
        self.stacked_widget.addWidget(self.pantalla_factura_pendiente_admin)
        self.stacked_widget.addWidget(self.pantalla_factura_nueva_admin)
        self.stacked_widget.addWidget(self.pantalla_factura_facturador)
        self.stacked_widget.addWidget(self.pantalla_hitorial_cliente)
        self.stacked_widget.addWidget(self.pantalla_historial_comunidad)
        self.stacked_widget.addWidget(self.pantalla_historial_municipio)
        self.stacked_widget.addWidget(self.pantalla_historial_antena)
        self.stacked_widget.addWidget(self.pantalla_historial_global)
        self.stacked_widget.addWidget(self.pantalla_modificar)
        self.stacked_widget.addWidget(self.pantalla_crearS_cliente)
        self.stacked_widget.addWidget(self.pantalla_crearS_comunidad)
        self.stacked_widget.addWidget(self.pantalla_crearS_municipio)
        self.stacked_widget.addWidget(self.pantalla_crearS_antena)



        # Añadir el QStackedWidget al layout principal
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.stacked_widget)

        # Establecer la pantalla de inicio
        self.stacked_widget.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("QWidget { background-color: #37373d; }")  # Cambia el color a tu preferencia

    main_window = MainWindow()

    # Set fixed size to prevent maximizing beyond 1275x725
    main_window.setMinimumSize(1275, 725)
    main_window.setMaximumSize(1275, 725)

    main_window.show()  # Esto es crucial para que la ventana se muestre
    sys.exit(app.exec_())
