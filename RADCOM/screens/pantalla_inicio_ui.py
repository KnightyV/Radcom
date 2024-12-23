from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(1275, 725)
        Form.setMinimumSize(QtCore.QSize(1275, 725))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        Form.setAutoFillBackground(False)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(500, 570, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"        background: #FFFFFF; \n"
"         border-radius: 30px; \n"
"}")
        self.pushButton.setObjectName("pushButton")
        
        # Password input
        self.Contrasena = QtWidgets.QLineEdit(Form)
        self.Contrasena.setGeometry(QtCore.QRect(450, 480, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Montserratl")
        font.setPointSize(-1)
        self.Contrasena.setFont(font)
        self.Contrasena.setStyleSheet("QLineEdit {\n"
"    background: transparent;    /* Quitar el fondo */\n"
"    border: 1px solid #FFFFFF;               /* Quitar el borde */\n"
"    color: #FFFFFF;             /* Cambiar el color del texto (ejemplo: blanco) */\n"
"    font-family: \"Montserratl\";       /* Cambiar el tipo de letra */\n"
"    font-size: 25px;            /* Cambiar el tamaño de la fuente */\n"
"}")
        self.Contrasena.setInputMask("")
        self.Contrasena.setText("")
        self.Contrasena.setAlignment(QtCore.Qt.AlignCenter)
        self.Contrasena.setObjectName("Contrasena")
        self.Contrasena.setEchoMode(QtWidgets.QLineEdit.Password)  # Set echo mode to Password

        # Username input
        self.Usuario = QtWidgets.QLineEdit(Form)
        self.Usuario.setGeometry(QtCore.QRect(450, 410, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Montserratl")
        font.setPointSize(-1)
        self.Usuario.setFont(font)
        self.Usuario.setStyleSheet("QLineEdit {\n"
"    background: transparent;    /* Quitar el fondo */\n"
"    border: 1px solid #FFFFFF;               /* Quitar el borde */\n"
"    color: #FFFFFF;             /* Cambiar el color del texto (ejemplo: blanco) */\n"
"    font-family: \"Montserratl\";       /* Cambiar el tipo de letra */\n"
"    font-size: 25px;            /* Cambiar el tamaño de la fuente */\n"
"}")
        self.Usuario.setInputMask("")
        self.Usuario.setText("")
        self.Usuario.setAlignment(QtCore.Qt.AlignCenter)
        self.Usuario.setObjectName("Usuario")
        
        # Read-only input
        self.Usuario_2 = QtWidgets.QLineEdit(Form)
        self.Usuario_2.setGeometry(QtCore.QRect(360, 370, 561, 291))
        font = QtGui.QFont()
        font.setFamily("Montserratl")
        font.setPointSize(-1)
        self.Usuario_2.setFont(font)
        self.Usuario_2.setStyleSheet("QLineEdit {\n"
"    background: transparent;    /* Quitar el fondo */\n"
"    border: 1px solid #FFFFFF;               /* Quitar el borde */\n"
"    border-radius: 20px;\n"
"    color: #FFFFFF;             /* Cambiar el color del texto (ejemplo: blanco) */\n"
"    font-family: \"Montserratl\";       /* Cambiar el tipo de letra */\n"
"    font-size: 10px;            /* Cambiar el tamaño de la fuente */\n"
"}")
        self.Usuario_2.setInputMask("")
        self.Usuario_2.setText("")
        self.Usuario_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Usuario_2.setObjectName("Usuario_2")

        # Make "Usuario_2" QLineEdit read-only and non-focusable
        self.Usuario_2.setReadOnly(True)
        self.Usuario_2.setFocusPolicy(QtCore.Qt.NoFocus)

        # Logo
        self.LOGO = QtWidgets.QLabel(Form)
        self.LOGO.setGeometry(QtCore.QRect(490, 50, 291, 271))
        self.LOGO.setText("")
        self.LOGO.setPixmap(QtGui.QPixmap("assets/Logo_P.png"))
        self.LOGO.setScaledContents(True)
        self.LOGO.setObjectName("LOGO")
        
        # Raise widgets for proper stacking
        self.Usuario_2.raise_()
        self.pushButton.raise_()
        self.Contrasena.raise_()
        self.Usuario.raise_()
        self.LOGO.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "INICIAR SESION"))
        self.Contrasena.setPlaceholderText(_translate("Form", "CONTRASEÑA"))
        self.Usuario.setPlaceholderText(_translate("Form", "USUARIO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
