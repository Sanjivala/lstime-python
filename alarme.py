# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alarme.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(331, 291)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("files/LSTime.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 331, 291))
        self.frame.setStyleSheet("background:#DE9C00;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.rbPredefinido = QtWidgets.QRadioButton(self.frame)
        self.rbPredefinido.setGeometry(QtCore.QRect(180, 80, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.rbPredefinido.setFont(font)
        self.rbPredefinido.setStyleSheet("background:#fff;color:#0F4F93;border-radius:5px;padding:0 7px;")
        self.rbPredefinido.setChecked(False)
        self.rbPredefinido.setObjectName("rbPredefinido")
        self.rbMusica = QtWidgets.QRadioButton(self.frame)
        self.rbMusica.setGeometry(QtCore.QRect(20, 80, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.rbMusica.setFont(font)
        self.rbMusica.setStyleSheet("background:#fff;color:#0F4F93;border-radius:5px;padding:0 7px;")
        self.rbMusica.setChecked(True)
        self.rbMusica.setObjectName("rbMusica")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 311, 271))
        self.label_2.setStyleSheet("background:#DE9C00;border:3px solid #fff;border-radius:5px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background:#fff;\n""color:#0F4F93;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.btnOk = QtWidgets.QPushButton(self.frame)
        self.btnOk.setGeometry(QtCore.QRect(60, 230, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.btnOk.setFont(font)
        self.btnOk.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnOk.setStyleSheet("QPushButton{background:#28A745;color:#fff;border:none;border-radius:5px;""}\n"
                                 "QPushButton:hover{background:#0F4F93;border:2px solid #fff;color:#fff;}")
        self.btnOk.setObjectName("btnOk")
        self.btnCancelar = QtWidgets.QPushButton(self.frame)
        self.btnCancelar.setGeometry(QtCore.QRect(170, 230, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.btnCancelar.setFont(font)
        self.btnCancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancelar.setStyleSheet("QPushButton{background:#9C27B0;color:#fff;border:none;border-radius:5px;}\n"
                                       "QPushButton:hover{background:#0F4F93;border:2px solid #fff;color:#fff;}")
        self.btnCancelar.setObjectName("btnCancelar")
        self.lblCaminho = QtWidgets.QLabel(self.frame)
        self.lblCaminho.setGeometry(QtCore.QRect(20, 180, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lblCaminho.setFont(font)
        self.lblCaminho.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lblCaminho.setStyleSheet(
            "background:rgba(221,221,221,.2);color:#fff;border-radius:5px;padding:0 2px;border:2px solid #fff;")
        self.lblCaminho.setObjectName("lblCaminho")
        self.btnAdicionar = QtWidgets.QPushButton(self.frame)
        self.btnAdicionar.setGeometry(QtCore.QRect(20, 130, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.btnAdicionar.setFont(font)
        self.btnAdicionar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAdicionar.setStyleSheet("QPushButton{background:#0F4F93;color:#fff;border:none;border-radius:5px;}"
                                        "QPushButton:hover{background:#9C27B0;border:2px solid #fff;color:#fff;}")
        self.btnAdicionar.setObjectName("btnAdicionar")
        self.btnAdicionar2 = QtWidgets.QPushButton(self.frame)
        self.btnAdicionar2.setGeometry(QtCore.QRect(268, 182, 41, 27))
        self.btnAdicionar2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAdicionar2.setStyleSheet("QPushButton{background:#0F4F93;color:#fff;border:none;border-radius:3px;}"
                                         "QPushButton:hover{background:#9C27B0;}")
        self.btnAdicionar2.setObjectName("btnAdicionar2")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(266, 182, 3, 29))
        self.line.setStyleSheet("color:#fff;\n""background:#fff;")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.label_2.raise_()
        self.rbPredefinido.raise_()
        self.rbMusica.raise_()
        self.label_3.raise_()
        self.btnOk.raise_()
        self.btnCancelar.raise_()
        self.lblCaminho.raise_()
        self.btnAdicionar.raise_()
        self.btnAdicionar2.raise_()
        self.line.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Alarme"))
        self.rbPredefinido.setToolTip(_translate("Dialog", "Usar um toque predefinido"))
        self.rbPredefinido.setText(_translate("Dialog", "Predefinido"))
        self.rbMusica.setToolTip(_translate("Dialog", "Usar m??sica como toque de alarme"))
        self.rbMusica.setText(_translate("Dialog", "M??sica"))
        self.label_3.setText(_translate("Dialog", "Tipo de Toque"))
        self.btnOk.setToolTip(_translate("Dialog", "Gravar alarme atual"))
        self.btnOk.setText(_translate("Dialog", "Ok"))
        self.btnCancelar.setToolTip(_translate("Dialog", "Cancelar alarme atual"))
        self.btnCancelar.setText(_translate("Dialog", "Cancelar"))
        self.lblCaminho.setToolTip(_translate("Dialog", "Caminho do ficheiro de m??sica"))
        self.lblCaminho.setText(_translate("Dialog", "Jos?? Lucash Celestino Sanjivala"))
        self.btnAdicionar.setToolTip(_translate("Dialog", "Adicionar ficheiro como toque de alarme"))
        self.btnAdicionar.setText(_translate("Dialog", "Adicionar"))
        self.btnAdicionar2.setToolTip(_translate("Dialog", "Adicionar ficheiro como toque de alarme"))
        self.btnAdicionar2.setText(_translate("Dialog", "..."))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
