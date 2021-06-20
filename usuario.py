# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usuario.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import LSTime


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 421)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("files/LSTime.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 391, 421))
        self.frame.setStyleSheet("background: #9C27B0;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 391, 421))
        self.label.setStyleSheet("background: #9C27B0;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("files/login/fundo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(60, 280, 35, 35))
        self.label_3.setStyleSheet("background:transparent;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("files/login/user.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(0, 380, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background:rgba(0,0,0,.6);color:#fff;font: 14pt \"Agency FB\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.btnOk = QtWidgets.QPushButton(self.frame)
        self.btnOk.setGeometry(QtCore.QRect(130, 331, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnOk.setFont(font)
        self.btnOk.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnOk.setToolTipDuration(-2)
        self.btnOk.setStyleSheet(
            "QPushButton {background:rgba(0,0,0,.5);color:#fff;border:2px solid #ddd;border-radius:20px;"
            "padding-bottom:0px;}QPushButton:hover {background:#ddd;border:2px solid #C87D2B;color:#333;}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("files/login/gravar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOk.setIcon(icon1)
        self.btnOk.setIconSize(QtCore.QSize(32, 32))
        self.btnOk.setObjectName("btnOk")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 380, 391, 2))
        self.line.setStyleSheet("background:#FF9800;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.txtUsuario = QtWidgets.QLineEdit(self.frame)
        self.txtUsuario.setGeometry(QtCore.QRect(55, 280, 301, 40))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.txtUsuario.setFont(font)
        self.txtUsuario.setToolTipDuration(-2)
        self.txtUsuario.setStyleSheet(
            "QLineEdit {background:rgba(255,255,255,.6);padding:0 46px;border-radius:15px;border-bottom:1px solid "
            "#ffffff;}QLineEdit:hover {background:#fff;color:#333;border-bottom:1px solid #9C27B0;}QLineEdit:Focus{"
            "background:#fff;color:#333;border-bottom:1px solid #FF9800;}")
        self.txtUsuario.setMaxLength(15)
        self.txtUsuario.setObjectName("txtUsuario")
        self.btnFoto = QtWidgets.QPushButton(self.frame)
        self.btnFoto.setGeometry(QtCore.QRect(288, 218, 50, 50))
        self.btnFoto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnFoto.setStyleSheet("border:2px solid #FF9800;border-radius:25px;background:transparent;color:#fff;")
        self.btnFoto.setText("")
        self.btnFoto.setObjectName("btnFoto")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(290, 220, 46, 46))
        self.label_5.setStyleSheet("background:#fff;padding:5px;border-radius:20px;")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("files/login/camera.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 391, 381))
        self.label_2.setStyleSheet("background:rgba(222, 156, 0,.6);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.lblFoto = QtWidgets.QLabel(self.frame)
        self.lblFoto.setGeometry(QtCore.QRect(80, 10, 241, 241))
        self.lblFoto.setStyleSheet("background:transparent;border:5px solid #fff;border-radius:5px;")
        self.lblFoto.setText("")
        self.lblFoto.setPixmap(QtGui.QPixmap("files/login/user.png"))
        self.lblFoto.setScaledContents(True)
        self.lblFoto.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFoto.setObjectName("lblFoto")
        self.label.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.txtUsuario.raise_()
        self.btnOk.raise_()
        self.line.raise_()
        self.label_3.raise_()
        self.lblFoto.raise_()
        self.label_5.raise_()
        self.btnFoto.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Variáveis extras
        self.ficheiro = ''
        self.imagem = 'files/login/login.png'
        self.usuario = ''
        self.lista = []

        self.leitor()
        self.btnFoto.clicked.connect(self.foto)
        self.btnOk.clicked.connect(self.nome)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Usuário"))
        self.label_4.setText(_translate("Dialog", "LSOFT INC - COPYRIGHT (C) - TODOS DIREITOS RESERVADOS"))
        self.btnOk.setToolTip(_translate("Dialog", "OK"))
        self.btnOk.setText(_translate("Dialog", "OK"))
        self.txtUsuario.setToolTip(_translate("Dialog", "Nome de perfil"))
        self.txtUsuario.setPlaceholderText(_translate("Dialog", "Nome de Usuário"))
        self.btnFoto.setToolTip(_translate("Dialog", "Alterar foto"))

    def msg_erro(self, titulo, texto):
        mensagem = QtWidgets.QMessageBox()
        mensagem.setIcon(QtWidgets.QMessageBox.Critical)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('files/LSTime.ico'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mensagem.setWindowIcon(icon)
        mensagem.setWindowTitle(titulo)
        mensagem.setText(texto)
        mensagem.exec_()

    def msg_success(self):
        mensagem = QtWidgets.QMessageBox()
        mensagem.setIcon(QtWidgets.QMessageBox.Information)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('files/LSTime.ico'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mensagem.setWindowIcon(icon)
        mensagem.setWindowTitle('Sucesso...')
        mensagem.setText('Dados atualizados com sucesso...')
        mensagem.exec_()

    def leitor(self):
        file = open('user.txt', 'r')
        for item in file:
            if item.isspace():
                continue
            else:
                self.lista.append(item)
        if self.lista == '' or len(self.lista) <= 1:
            self.usuario = 'Usuário'
            self.ficheiro = self.imagem
        else:
            self.usuario = self.lista[0]
            self.ficheiro = self.lista[1]
        self.txtUsuario.setText(self.usuario)
        pixmap = QtGui.QPixmap(self.ficheiro)
        pixmap = pixmap.scaled(self.lblFoto.width(), self.lblFoto.height(), QtCore.Qt.KeepAspectRatio)
        self.lblFoto.setPixmap(pixmap)
        self.lblFoto.setAlignment(QtCore.Qt.AlignCenter)
        file.close()

    def foto(self):
        self.ficheiro, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Select Foto', '',
                                                                 'Fotos(*.jpg *.png *.jpeg *.bmp)')

        if self.ficheiro:
            pixmap = QtGui.QPixmap(self.ficheiro)
            pixmap = pixmap.scaled(self.lblFoto.width(), self.lblFoto.height(), QtCore.Qt.KeepAspectRatio)
            self.lblFoto.setPixmap(pixmap)
            self.lblFoto.setAlignment(QtCore.Qt.AlignCenter)
        else:
            pass

    def nome(self):
        file = open('user.txt', 'w')
        self.usuario = str(self.txtUsuario.text().upper())
        if self.usuario == '' or len(self.usuario) <= 1:
            self.msg_erro('Nome de Usuário', 'Insere um nome de Usuário válido!')
            self.txtUsuario.clear()
            self.txtUsuario.setFocus()
            self.txtUsuario.setPlaceholderText('Nome de Usuário')
        elif self.usuario.isspace():
            self.msg_erro('Nome de Usuário', 'Nome de usuário não pode ser espaço em branco!')
            self.txtUsuario.clear()
            self.txtUsuario.setFocus()
            self.txtUsuario.setPlaceholderText('Nome de Usuário')
        elif self.usuario.isnumeric():
            self.msg_erro('Nome de Usuário', 'Nome de usuário deve conter letras!')
            self.txtUsuario.clear()
            self.txtUsuario.setFocus()
            self.txtUsuario.setPlaceholderText('Nome de Usuário')
        elif self.usuario.__contains__(' '):
            self.msg_erro('Nome de usuário', 'Nome de usuário não pode conter espaços em branco!')
            self.txtUsuario.clear()
            self.txtUsuario.setFocus()
            self.txtUsuario.setPlaceholderText('Nome de Usuário')
        else:
            if self.ficheiro == '':
                self.ficheiro = self.imagem
            file.truncate()
            file.write(self.usuario + '\n')
            file.write(self.ficheiro)
            if file:
                self.msg_success()
            file.close()
            self.hidden()

    def hidden(self):
        print('Fechando a janela')


if __name__ == "__main__":
    import sys

    open('user.txt', 'a')
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
