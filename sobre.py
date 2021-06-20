# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sobre.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import LSTime


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 421)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("files/LSTime.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 551, 421))
        self.frame.setStyleSheet("background:#2F0C35")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 551, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#fff;\n""background:#9C27B0;")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lblLogotipo = QtWidgets.QLabel(self.frame)
        self.lblLogotipo.setGeometry(QtCore.QRect(30, 70, 161, 161))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.lblLogotipo.setFont(font)
        self.lblLogotipo.setStyleSheet("background:transparent;color:#9C27B0;border-radius:5px;padding:5px;")
        self.lblLogotipo.setText("")
        self.lblLogotipo.setPixmap(QtGui.QPixmap("files/LSTime.ico"))
        self.lblLogotipo.setScaledContents(True)
        self.lblLogotipo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLogotipo.setObjectName("lblLogotipo")
        self.lblTexto = QtWidgets.QLabel(self.frame)
        self.lblTexto.setGeometry(QtCore.QRect(220, 80, 321, 141))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblTexto.setFont(font)
        self.lblTexto.setStyleSheet("color:#fff;background:transparent;padding:0 5px;")
        self.lblTexto.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignTop)
        self.lblTexto.setWordWrap(True)
        self.lblTexto.setObjectName("lblTexto")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 260, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:#fff;")
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setObjectName("label_6")
        self.btnOk = QtWidgets.QPushButton(self.frame)
        # self.btnOk.setGeometry(QtCore.QRect(420, 370, 121, 41))
        # font = QtGui.QFont()
        # font.setFamily("Agency FB")
        # font.setPointSize(25)
        # font.setBold(True)
        # font.setWeight(75)
        # self.btnOk.setFont(font)
        # self.btnOk.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.btnOk.setStyleSheet("QPushButton{border:none;background:#9C27B0;color:#fff;border-radius:17px;padding"
        #                          ":0px 5px;}QPushButton:hover{background:#28A745;color:#fff;}")
        # self.btnOk.setObjectName("btnOk")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(350, 260, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:#fff;")
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(350, 290, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:#fff;")
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(350, 320, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:#fff;")
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(10, 290, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:#fff;")
        self.label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(10, 320, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:#fff;")
        self.label_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_11.setObjectName("label_11")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(0, 250, 550, 1))
        self.line_2.setStyleSheet("background:#fff;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(0, 357, 550, 1))
        self.line_3.setStyleSheet("background:#fff;")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.lblrodape = QtWidgets.QLabel(self.frame)
        self.lblrodape.setGeometry(QtCore.QRect(10, 370, 530, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(14)
        self.lblrodape.setFont(font)
        self.lblrodape.setStyleSheet("background:rgba(156, 39, 176,.3);color:#fff;border-radius:17px;padding:0 20px;")
        self.lblrodape.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.lblrodape.setObjectName("lblrodape")
        self.lblrodape.raise_()
        self.label.raise_()
        self.lblLogotipo.raise_()
        self.lblTexto.raise_()
        self.label_6.raise_()
        # self.btnOk.raise_()
        self.label_8.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.line_2.raise_()
        self.line_3.raise_()

        # self.btnOk.clicked.connect(self.sair)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sobre LSTime"))
        self.label.setText(_translate("Dialog", "LSoft Inc - LSTime"))
        self.lblTexto.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                   "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                                   "type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n "
                                                   "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; "
                                                   "font-size:9pt; font-weight:400; font-style:normal;\">\n "
                                                   "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; "
                                                   "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                   "text-indent:0px;\"><span style=\" font-weight:600;\">LStime</span> "
                                                   "é uma aplicação que possibilita controlar o seu tempo durante "
                                                   "os estudos.</p>\n<p align=\"justify\" style=\" margin-top:12px; "
                                                   "margin-bottom:12px; margin-left:0px; margin-right:0px; "
                                                   "-qt-block-indent:0; text-indent:0px;\">Mantem-te focado e ao mesmo "
                                                   "tempo controlas o seu progresso a medida que vais avançando.</p>\n "
                                                   "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; "
                                                   "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                   "text-indent:0px;\">Adiciona um tempo de pausa e configura um "
                                                   "alarme para não perder as tuas tarefas diárias.</p>\n "
                                                   "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; "
                                                   "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                   "text-indent:0px;\">Visualiza a posição do seu "
                                                   "mouse.</p></body></html>"))
        self.label_6.setText(
            _translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Desenvolvido "
                                 "Por</span>: Lucash Sanjivala</p></body></html>"))
        # self.btnOk.setText(_translate("Dialog", "Ok"))
        # self.btnOk.setShortcut(_translate("Dialog", "Enter"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">"
                                                  "Aplicação</span>: ""LSTime</p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">"
                                                  "Versão</span>: 3.1.5</p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">"
                                                  "Empresa</span>: LSoft Inc</p></body></html>"))
        self.label_10.setText(_translate("Dialog",
                                         "<html><head/><body><p><span style=\" font-weight:600;\">Telefone</span>: "
                                         "923 528 877  |  943 176 740</p></body></html>"))
        self.label_11.setText(_translate("Dialog",
                                         "<html><head/><body><p><span style=\" font-weight:600;\">Email</span>: "
                                         "sanjivala@gmail.com</p></body></html>"))
        self.lblrodape.setText(_translate("Dialog",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                             "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                             "type=\"text/css\">\n ""p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'Agency FB\'; font-size:14pt; "
                                             "font-weight:400; font-style:normal;\">\n"
                                             "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; "
                                             "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                             "text-indent:0px;\"><span style=\" font-weight:600;\">LSoft Inc</span> "
                                             "Copyright &copy; 2020 - Todos os direitos reservados</p></body></html>"))

    # def sair(self):
    #     # sys.exit(self.setupUi(Dialog))
    #     classe = Ui_Dialog()
    #     classe.setupUi(Dialog)
    #     Dialog.close()
    #     print('Método sair foi chamado')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
