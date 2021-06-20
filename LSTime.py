# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LSTime.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
# Feito por: Lucash Sanjivala
# Empresa: LSoft, Inc
# Versão: 1.3.4
# SO: Windows 10
# Copyright 2020 - Todos os direito reservados
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QThread
from mutagenx.mp3 import MP3
from mutagenx.flac import FLAC
from pygame import mixer
import sobre, progressos, usuario
import sqlite3
import time, os, random, winsound, threading


class Ui_MainWindow(QThread, object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 576)
        MainWindow.setMinimumSize(QtCore.QSize(810, 576))
        MainWindow.setMaximumSize(QtCore.QSize(810, 576))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("files/LSTime.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background:#222;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setStyleSheet("background:#9C27B0;")
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.label = QtWidgets.QLabel(self.frame1)
        self.label.setGeometry(QtCore.QRect(211, 0, 581, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#FABB15;\n""background:#222;")
        self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.fmAlarme = QtWidgets.QFrame(self.frame1)
        self.fmAlarme.setGeometry(QtCore.QRect(0, 57, 211, 501))
        self.fmAlarme.setStyleSheet("background:#DE9C00;")
        self.fmAlarme.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fmAlarme.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fmAlarme.setObjectName("fmAlarme")
        self.lcdHora = QtWidgets.QLCDNumber(self.fmAlarme)
        self.lcdHora.setGeometry(QtCore.QRect(10, 20, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        self.lcdHora.setFont(font)
        self.lcdHora.setStyleSheet("color:#fff;")
        self.lcdHora.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdHora.setDigitCount(8)
        self.lcdHora.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdHora.setObjectName("lcdHora")
        self.lcdData = QtWidgets.QLCDNumber(self.fmAlarme)
        self.lcdData.setGeometry(QtCore.QRect(10, 60, 191, 31))
        self.lcdData.setStyleSheet("color:#fff;")
        self.lcdData.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdData.setDigitCount(10)
        self.lcdData.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdData.setObjectName("lcdData")
        self.line_2 = QtWidgets.QFrame(self.fmAlarme)
        self.line_2.setGeometry(QtCore.QRect(10, 100, 191, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.btnAtivar = QtWidgets.QPushButton(self.fmAlarme)
        self.btnAtivar.setGeometry(QtCore.QRect(10, 240, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.btnAtivar.setFont(font)
        self.btnAtivar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAtivar.setStyleSheet("QPushButton{border:none;background:#28A745;color:#fff;}"
                                     "QPushButton:hover{background:#0F4F93;}")
        self.btnAtivar.setObjectName("btnAtivar")
        self.txtHora = QtWidgets.QTimeEdit(self.fmAlarme)
        self.txtHora.setGeometry(QtCore.QRect(100, 240, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.txtHora.setFont(font)
        self.txtHora.setStyleSheet("QTimeEdit{background:#ddd;color:#9C27B0;}QTimeEdit:focus{background:#fff;}")
        self.txtHora.setFrame(False)
        self.txtHora.setAlignment(QtCore.Qt.AlignCenter)
        self.txtHora.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.txtHora.setObjectName("txtHora")
        self.lblAlarme = QtWidgets.QLabel(self.fmAlarme)
        self.lblAlarme.setGeometry(QtCore.QRect(10, 120, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.lblAlarme.setFont(font)
        self.lblAlarme.setStyleSheet("background:#fff;\n""color:#9C27B0")
        self.lblAlarme.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAlarme.setObjectName("lblAlarme")
        self.line_3 = QtWidgets.QFrame(self.fmAlarme)
        self.line_3.setGeometry(QtCore.QRect(10, 350, 190, 3))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.label_9 = QtWidgets.QLabel(self.fmAlarme)
        self.label_9.setGeometry(QtCore.QRect(10, 360, 191, 46))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(25)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background:#fff;\n""color:#9C27B0;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.btnEncerrar = QtWidgets.QPushButton(self.fmAlarme)
        self.btnEncerrar.setGeometry(QtCore.QRect(20, 412, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.btnEncerrar.setFont(font)
        self.btnEncerrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnEncerrar.setStyleSheet("QPushButton{border:none;background:#0F4F93;color:#ddd;border-radius:5px;}"
                                       "QPushButton:hover{\n""background:#28A745;\n""}")
        self.btnEncerrar.setObjectName("btnEncerrar")
        self.btnReiniciar = QtWidgets.QPushButton(self.fmAlarme)
        self.btnReiniciar.setGeometry(QtCore.QRect(110, 412, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.btnReiniciar.setFont(font)
        self.btnReiniciar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnReiniciar.setStyleSheet("QPushButton{border:none;background:#0F4F93;color:#ddd;border-radius:5px;}"
                                        "QPushButton:hover{\n""background:#28A745;\n""}")
        self.btnReiniciar.setObjectName("btnReiniciar")
        self.btnHibernar = QtWidgets.QPushButton(self.fmAlarme)
        self.btnHibernar.setGeometry(QtCore.QRect(20, 452, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.btnHibernar.setFont(font)
        self.btnHibernar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnHibernar.setStyleSheet("QPushButton{border:none;background:#0F4F93;color:#ddd;border-radius:5px;}"
                                       "QPushButton:hover{\n""background:#28A745;\n""}")
        self.btnHibernar.setObjectName("btnHibernar")
        self.btnCancelar = QtWidgets.QPushButton(self.fmAlarme)
        self.btnCancelar.setGeometry(QtCore.QRect(110, 452, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.btnCancelar.setFont(font)
        self.btnCancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancelar.setStyleSheet("QPushButton{border:none;background:#0F4F93;\n""color:#ddd;border-radius:5px;}"
                                       "QPushButton:hover{\n""background:#28A745;\n""}")
        self.btnCancelar.setObjectName("btnCancelar")
        self.label_10 = QtWidgets.QLabel(self.fmAlarme)
        self.label_10.setGeometry(QtCore.QRect(10, 362, 191, 131))
        self.label_10.setStyleSheet("background:#ddd;")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.cbAposAlarme = QtWidgets.QCheckBox(self.fmAlarme)
        self.cbAposAlarme.setGeometry(QtCore.QRect(10, 270, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.cbAposAlarme.setFont(font)
        self.cbAposAlarme.setStyleSheet("color:#fff;\n""background:transparent;")
        self.cbAposAlarme.setObjectName("cbAposAlarme")
        self.cbOpcao = QtWidgets.QComboBox(self.fmAlarme)
        self.cbOpcao.setGeometry(QtCore.QRect(10, 310, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cbOpcao.setFont(font)
        self.cbOpcao.setStyleSheet("background:#fff;\n""color:#9C27B0;")
        self.cbOpcao.setMaxCount(5)
        self.cbOpcao.setFrame(True)
        self.cbOpcao.setObjectName("cbOpcao")
        self.cbOpcao.addItem("")
        self.cbOpcao.addItem("")
        self.cbOpcao.addItem("")
        self.cbOpcao.addItem("")
        self.line_7 = QtWidgets.QFrame(self.fmAlarme)
        self.line_7.setGeometry(QtCore.QRect(10, 13, 190, 3))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.rbMusica = QtWidgets.QRadioButton(self.fmAlarme)
        self.rbMusica.setGeometry(QtCore.QRect(10, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.rbMusica.setFont(font)
        self.rbMusica.setStyleSheet("background:#fff;\n""color:#0F4F93;\n""border-radius:0;\n""padding:0 7px;")
        self.rbMusica.setObjectName("rbMusica")
        self.rbMusica.setChecked(False)
        self.rbPadrao = QtWidgets.QRadioButton(self.fmAlarme)
        self.rbPadrao.setGeometry(QtCore.QRect(100, 160, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.rbPadrao.setFont(font)
        self.rbPadrao.setStyleSheet("background:#fff;\n""color:#0F4F93;\n""border-radius:0;\n""padding:0 7px;")
        self.rbPadrao.setObjectName("rbPadrao")
        self.lblCaminho = QtWidgets.QLabel(self.fmAlarme)
        self.lblCaminho.setGeometry(QtCore.QRect(10, 200, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblCaminho.setFont(font)
        self.lblCaminho.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lblCaminho.setStyleSheet(
            "background:rgba(221,221,221,.2);color:#fff;border-radius:5px;padding:0 2px;border:2px solid #fff;")
        self.lblCaminho.setObjectName("lblCaminho")
        self.lblCaminho.raise_()
        self.label_10.raise_()
        self.lcdHora.raise_()
        self.lcdData.raise_()
        self.line_2.raise_()
        self.btnAtivar.raise_()
        self.txtHora.raise_()
        self.lblAlarme.raise_()
        self.line_3.raise_()
        self.label_9.raise_()
        self.btnEncerrar.raise_()
        self.btnReiniciar.raise_()
        self.btnHibernar.raise_()
        self.btnCancelar.raise_()
        self.cbAposAlarme.raise_()
        self.cbOpcao.raise_()
        self.line_7.raise_()
        self.rbMusica.raise_()
        self.rbPadrao.raise_()
        self.label_22 = QtWidgets.QLabel(self.frame1)
        self.label_22.setGeometry(QtCore.QRect(574, 143, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet(
            "background:transparent;color:#fff;border-radius:10px;border-bottom:2px solid #fff;")
        self.label_22.setText("")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_3 = QtWidgets.QLabel(self.frame1)
        self.label_3.setGeometry(QtCore.QRect(574, 80, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(29)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-bottom:2px solid #fff;\n""color:#9C27B0;background:#fff;padding:3px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lblLogotipo = QtWidgets.QLabel(self.frame1)
        self.lblLogotipo.setGeometry(QtCore.QRect(0, 0, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setBold(False)
        font.setWeight(50)
        self.lblLogotipo.setFont(font)
        self.lblLogotipo.setStyleSheet("background:#222;\n""color:#fff;\n""padding:0 25px;")
        self.lblLogotipo.setText("")
        self.lblLogotipo.setPixmap(QtGui.QPixmap("files/Logotipo.png"))
        self.lblLogotipo.setScaledContents(True)
        self.lblLogotipo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLogotipo.setObjectName("lblLogotipo")
        self.txtTempoEstudo = QtWidgets.QSpinBox(self.frame1)
        self.txtTempoEstudo.setGeometry(QtCore.QRect(215, 142, 88, 57))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.txtTempoEstudo.setFont(font)
        self.txtTempoEstudo.setStyleSheet("QSpinBox{padding:0 3px;background:#ddd;color:#9C27B0;}"
                                          "QSpinBox:focus{background:#fff;\n""color:#0F4F93;\n""}")
        self.txtTempoEstudo.setFrame(False)
        self.txtTempoEstudo.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.txtTempoEstudo.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.txtTempoEstudo.setMinimum(0)
        self.txtTempoEstudo.setMaximum(600)
        self.txtTempoEstudo.setProperty("value", 0)
        self.txtTempoEstudo.setObjectName("txtTempoEstudo")
        self.btnIniciar = QtWidgets.QPushButton(self.frame1)
        self.btnIniciar.setGeometry(QtCore.QRect(360, 143, 91, 55))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(29)
        font.setBold(False)
        font.setWeight(50)
        self.btnIniciar.setFont(font)
        self.btnIniciar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnIniciar.setStyleSheet("QPushButton{background:#28A745;border:none;color:#fff;}"
                                      "QPushButton:hover{\n""background:#0F4F93;\n""color:#fff;\n""}")
        self.btnIniciar.setObjectName("btnIniciar")
        self.label_5 = QtWidgets.QLabel(self.frame1)
        self.label_5.setGeometry(QtCore.QRect(220, 80, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(29)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background:#fff;\n""color:#9C27B0;\n""padding:0 3px;")
        self.label_5.setObjectName("label_5")
        self.lblTempoEstudo = QtWidgets.QLabel(self.frame1)
        self.lblTempoEstudo.setGeometry(QtCore.QRect(220, 143, 231, 61))
        self.lblTempoEstudo.setStyleSheet("border-bottom:2px solid #fff;")
        self.lblTempoEstudo.setText("")
        self.lblTempoEstudo.setObjectName("lblTempoEstudo")
        self.label_2 = QtWidgets.QLabel(self.frame1)
        self.label_2.setGeometry(QtCore.QRect(299, 143, 61, 55))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(35)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n""background:#ddd;\n""color:#9C27B0;\n""}")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lblSegundos = QtWidgets.QLabel(self.frame1)
        self.lblSegundos.setGeometry(QtCore.QRect(466, 80, 91, 121))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(70)
        font.setBold(True)
        font.setWeight(75)
        self.lblSegundos.setFont(font)
        self.lblSegundos.setStyleSheet("color:000;\n""background:transparent;")
        self.lblSegundos.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSegundos.setObjectName("lblSegundos")
        self.lblHoraRestante = QtWidgets.QLabel(self.frame1)
        self.lblHoraRestante.setGeometry(QtCore.QRect(625, 208, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.lblHoraRestante.setFont(font)
        self.lblHoraRestante.setStyleSheet("color:#d2d3d4;\n""padding:0px 10px;border-bottom:2px solid #ddd;")
        self.lblHoraRestante.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lblHoraRestante.setObjectName("lblHoraRestante")
        self.label_7 = QtWidgets.QLabel(self.frame1)
        self.label_7.setGeometry(QtCore.QRect(690, 208, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:#d2d3d4;background:transparent;border-bottom:2px solid #ddd;padding:0 5px;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.btnFinalizar = QtWidgets.QPushButton(self.frame1)
        self.btnFinalizar.setGeometry(QtCore.QRect(220, 208, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(35)
        self.btnFinalizar.setFont(font)
        self.btnFinalizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnFinalizar.setStyleSheet("QPushButton{background:#0F4F93;color:#fff;border:none;}"
                                        "QPushButton:hover{background:transparent;border:2px solid #fff;"
                                        "color:#fff;border-radius:5px;\n""}")
        self.btnFinalizar.setObjectName("btnFinalizar")
        self.line = QtWidgets.QFrame(self.frame1)
        self.line.setGeometry(QtCore.QRect(220, 259, 561, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btnSobre = QtWidgets.QPushButton(self.frame1)
        self.btnSobre.setGeometry(QtCore.QRect(570, 512, 211, 39))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.btnSobre.setFont(font)
        self.btnSobre.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.btnSobre.setStyleSheet("QPushButton{border:none;background:#2F0C35;color:#fff;padding:0px 5px;}"
                                    "QPushButton:hover{background:#28A745;color:#fff;border:2px solid #fff;"
                                    "border-radius:5px;\n""}")
        self.btnSobre.setObjectName("btnSobre")
        self.label_8 = QtWidgets.QLabel(self.frame1)
        self.label_8.setGeometry(QtCore.QRect(570, 280, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(30)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:#9C27B0;\n""background:#fff;")
        self.label_8.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.frame1)
        self.label_11.setGeometry(QtCore.QRect(570, 330, 211, 121))
        self.label_11.setStyleSheet("background:#ddd;")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.lblTempoTotal = QtWidgets.QLabel(self.frame1)
        self.lblTempoTotal.setGeometry(QtCore.QRect(580, 340, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblTempoTotal.setFont(font)
        self.lblTempoTotal.setStyleSheet("color:#fff;\n""background:#9C27B0;\n""border:none;")
        self.lblTempoTotal.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTempoTotal.setObjectName("lblTempoTotal")
        self.btnRestaurar = QtWidgets.QPushButton(self.frame1)
        self.btnRestaurar.setGeometry(QtCore.QRect(660, 340, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.btnRestaurar.setFont(font)
        self.btnRestaurar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRestaurar.setStyleSheet("QPushButton{background:#0F4F93;border:none;color:#fff;}QPushButton:hover{"
                                        "background:#ddd;\n""color:#9C27B0;\n""border:3px solid #9C27B0;\n""}")
        self.btnRestaurar.setObjectName("btnRestaurar")
        self.label_13 = QtWidgets.QLabel(self.frame1)
        self.label_13.setGeometry(QtCore.QRect(630, 340, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:#fff;\n""background:#9C27B0;")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.lblSetas = QtWidgets.QLabel(self.frame1)
        self.lblSetas.setGeometry(QtCore.QRect(466, 200, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.lblSetas.setFont(font)
        self.lblSetas.setStyleSheet("background:transparent;\n""color:#ffff00")
        self.lblSetas.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSetas.setObjectName("lblSetas")
        self.btnProgressos = QtWidgets.QPushButton(self.frame1)
        self.btnProgressos.setGeometry(QtCore.QRect(570, 455, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(25)
        self.btnProgressos.setFont(font)
        self.btnProgressos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnProgressos.setStyleSheet("QPushButton{background:#0F4F93;border:none;color:#fff;}QPushButton:hover{"
                                         "background:transparent;color:#fff;border:2px solid #fff;border-radius:5px;}")
        self.btnProgressos.setObjectName("btnProgressos")
        self.btnGravar = QtWidgets.QPushButton(self.frame1)
        self.btnGravar.setGeometry(QtCore.QRect(580, 400, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(23)
        self.btnGravar.setFont(font)
        self.btnGravar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGravar.setStyleSheet("QPushButton{background:#0F4F93;border:none;color:#fff;}QPushButton:hover{"
                                     "background:#9C27B0;\n""color:#fff;\n""}")
        self.btnGravar.setObjectName("btnGravar")
        self.label_14 = QtWidgets.QLabel(self.frame1)
        self.label_14.setGeometry(QtCore.QRect(220, 273, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(28)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background:#fff;\n""color:#0F4F93")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame1)
        self.label_15.setGeometry(QtCore.QRect(220, 323, 331, 71))
        self.label_15.setStyleSheet("background:#ddd;")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame1)
        self.label_16.setGeometry(QtCore.QRect(287, 334, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(30)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("QLabel{background:#fff;color:#0F4F93;}")
        self.label_16.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.btnPausar = QtWidgets.QPushButton(self.frame1)
        self.btnPausar.setGeometry(QtCore.QRect(230, 334, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(23)
        self.btnPausar.setFont(font)
        self.btnPausar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPausar.setStyleSheet("QPushButton{background:#28A745;border:none;color:#fff;}"
                                     "QPushButton:hover{background:#0F4F93;color:#fff;}")
        self.btnPausar.setObjectName("btnPausar")
        self.line_5 = QtWidgets.QFrame(self.frame1)
        self.line_5.setGeometry(QtCore.QRect(220, 400, 331, 3))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.lblTempoRestante = QtWidgets.QLabel(self.frame1)
        self.lblTempoRestante.setGeometry(QtCore.QRect(590, 140, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.lblTempoRestante.setFont(font)
        self.lblTempoRestante.setStyleSheet("color:#fff;\n""background:transparent;")
        self.lblTempoRestante.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTempoRestante.setObjectName("lblTempoRestante")
        self.label_21 = QtWidgets.QLabel(self.frame1)
        self.label_21.setGeometry(QtCore.QRect(700, 140, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(40)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color:#fff;\n""background:transparent;")
        self.label_21.setObjectName("label_21")
        self.label_4 = QtWidgets.QLabel(self.frame1)
        self.label_4.setGeometry(QtCore.QRect(23, 6, 59, 59))
        self.label_4.setStyleSheet("background:transparent;")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("files/LSTime.ico"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(self.frame1)
        self.frame.setGeometry(QtCore.QRect(220, 410, 341, 140))
        self.frame.setStyleSheet("background:#ddd;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.label_17.setStyleSheet("background:#fff;")
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("files/player/logo.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.btnPrev = QtWidgets.QPushButton(self.frame)
        self.btnPrev.setGeometry(QtCore.QRect(56, 35, 30, 30))
        self.btnPrev.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPrev.setStyleSheet("border:none;\n""background:#fff;\n""border-radius:15px;")
        self.btnPrev.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("files/player/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPrev.setIcon(icon1)
        self.btnPrev.setIconSize(QtCore.QSize(35, 35))
        self.btnPrev.setObjectName("btnPrev")
        self.btnPause = QtWidgets.QPushButton(self.frame)
        self.btnPause.setGeometry(QtCore.QRect(164, 35, 30, 30))
        self.btnPause.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPause.setStyleSheet("border:none;\n""background:#fff;\n""border-radius:15px;")
        self.btnPause.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("files/player/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPause.setIcon(icon2)
        self.btnPause.setIconSize(QtCore.QSize(35, 35))
        self.btnPause.setObjectName("btnPause")
        self.btnNext = QtWidgets.QPushButton(self.frame)
        self.btnNext.setGeometry(QtCore.QRect(200, 35, 30, 30))
        self.btnNext.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNext.setStyleSheet("border:none;\n""background:#fff;\n""border-radius:15px;")
        self.btnNext.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("files/player/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNext.setIcon(icon3)
        self.btnNext.setIconSize(QtCore.QSize(35, 35))
        self.btnNext.setObjectName("btnNext")
        self.btnMuted = QtWidgets.QPushButton(self.frame)
        self.btnMuted.setGeometry(QtCore.QRect(264, 106, 30, 30))
        self.btnMuted.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMuted.setStyleSheet("border:none;\n""background:#fff;\n""border-radius:15px;")
        self.btnMuted.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("files/player/volume.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMuted.setIcon(icon4)
        self.btnMuted.setIconSize(QtCore.QSize(20, 20))
        self.btnMuted.setObjectName("btnMuted")
        self.btnRandom = QtWidgets.QPushButton(self.frame)
        self.btnRandom.setGeometry(QtCore.QRect(300, 106, 30, 30))
        self.btnRandom.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRandom.setStyleSheet("border:none;\n""background:#fff;\n""border-radius:15px;")
        self.btnRandom.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("files/player/randomB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRandom.setIcon(icon5)
        self.btnRandom.setIconSize(QtCore.QSize(20, 20))
        self.btnRandom.setObjectName("btnRandom")
        self.lblReproducao = QtWidgets.QLabel(self.frame)
        self.lblReproducao.setGeometry(QtCore.QRect(10, 74, 241, 24))
        self.lblReproducao.setStyleSheet("background:#fff;\n""color:#000;")
        self.lblReproducao.setIndent(5)
        self.lblReproducao.setObjectName("lblReproducao")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(10, 70, 320, 3))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.lblTempo = QtWidgets.QLabel(self.frame)
        self.lblTempo.setGeometry(QtCore.QRect(260, 74, 71, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblTempo.setFont(font)
        self.lblTempo.setStyleSheet("background:#ddd;\n""color:#000;")
        self.lblTempo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTempo.setObjectName("lblTempo")
        self.btnStop = QtWidgets.QPushButton(self.frame)
        self.btnStop.setGeometry(QtCore.QRect(92, 35, 30, 30))
        self.btnStop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnStop.setStyleSheet("border:none;\n""background:#fff;\n""border-radius:15px;")
        self.btnStop.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("files/player/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStop.setIcon(icon6)
        self.btnStop.setIconSize(QtCore.QSize(35, 35))
        self.btnStop.setObjectName("btnStop")
        self.hsVolume = QtWidgets.QSlider(self.frame)
        self.hsVolume.setGeometry(QtCore.QRect(170, 110, 81, 22))
        self.hsVolume.setOrientation(QtCore.Qt.Horizontal)
        # self.hsVolume.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.hsVolume.setObjectName("hsVolume")
        self.cbFicheiros = QtWidgets.QComboBox(self.frame)
        self.cbFicheiros.setGeometry(QtCore.QRect(10, 110, 151, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbFicheiros.setFont(font)
        self.cbFicheiros.setStyleSheet("background:#fff;\n""color:#333;")
        self.cbFicheiros.setObjectName("cbFicheiros")
        self.btnAddMusica = QtWidgets.QPushButton(self.frame)
        self.btnAddMusica.setGeometry(QtCore.QRect(250, 35, 81, 31))
        self.btnAddMusica.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAddMusica.setStyleSheet("border:none;\n""background:#0F4F93;")
        self.btnAddMusica.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("files/player/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAddMusica.setIcon(icon7)
        self.btnAddMusica.setIconSize(QtCore.QSize(30, 30))
        self.btnAddMusica.setObjectName("btnAddMusica")
        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setGeometry(QtCore.QRect(235, 37, 3, 26))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.btnPlay = QtWidgets.QPushButton(self.frame)
        self.btnPlay.setGeometry(QtCore.QRect(128, 35, 30, 30))
        self.btnPlay.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPlay.setStyleSheet("border:none;\n""background:#fff;\n""border-radius:15px;")
        self.btnPlay.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("files/player/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPlay.setIcon(icon8)
        self.btnPlay.setIconSize(QtCore.QSize(35, 35))
        self.btnPlay.setObjectName("btnPlay")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(30, 0, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background:#fff;\n""color:#0F4F93")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.line_9 = QtWidgets.QFrame(self.frame)
        self.line_9.setGeometry(QtCore.QRect(10, 101, 320, 3))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.frame)
        self.line_10.setGeometry(QtCore.QRect(48, 36, 3, 28))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.btnDelete = QtWidgets.QPushButton(self.frame)
        self.btnDelete.setGeometry(QtCore.QRect(10, 35, 31, 31))
        self.btnDelete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDelete.setStyleSheet("border:none;\n""background:#fff;\n""border-radius:15px;")
        self.btnDelete.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("files/player/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDelete.setIcon(icon9)
        self.btnDelete.setIconSize(QtCore.QSize(35, 35))
        self.btnDelete.setObjectName("btnDelete")
        self.label_6 = QtWidgets.QLabel(self.frame1)
        self.label_6.setGeometry(QtCore.QRect(360, 324, 171, 71))
        self.label_6.setStyleSheet("background:transparent;")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("files/Logotipo.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.btnPrev.raise_()
        self.btnPause.raise_()
        self.btnNext.raise_()
        self.btnMuted.raise_()
        self.btnRandom.raise_()
        self.lblReproducao.raise_()
        self.line_4.raise_()
        self.lblTempo.raise_()
        self.btnStop.raise_()
        self.hsVolume.raise_()
        self.cbFicheiros.raise_()
        self.btnAddMusica.raise_()
        self.line_6.raise_()
        self.btnPlay.raise_()
        self.label_18.raise_()
        self.line_9.raise_()
        self.label_17.raise_()
        self.line_10.raise_()
        self.btnDelete.raise_()
        self.line_5.raise_()
        self.frame.raise_()
        self.label_15.raise_()
        self.label.raise_()
        self.fmAlarme.raise_()
        self.label_22.raise_()
        self.label_3.raise_()
        self.lblLogotipo.raise_()
        self.label_5.raise_()
        self.lblTempoEstudo.raise_()
        self.btnIniciar.raise_()
        self.txtTempoEstudo.raise_()
        self.label_2.raise_()
        self.lblSegundos.raise_()
        self.lblHoraRestante.raise_()
        self.label_7.raise_()
        self.btnFinalizar.raise_()
        self.line.raise_()
        self.btnSobre.raise_()
        self.label_8.raise_()
        self.label_11.raise_()
        self.lblTempoTotal.raise_()
        self.btnRestaurar.raise_()
        self.label_13.raise_()
        self.lblSetas.raise_()
        self.btnProgressos.raise_()
        self.btnGravar.raise_()
        self.label_14.raise_()
        self.label_16.raise_()
        self.btnPausar.raise_()
        self.lblTempoRestante.raise_()
        self.label_21.raise_()
        self.label_4.raise_()
        self.label_6.raise_()
        self.horizontalLayout.addWidget(self.frame1)
        MainWindow.setCentralWidget(self.centralwidget)

        # Configuração do método para hora e data
        self.formatoHora = ''
        self.alarme = Alarme
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.hora_data)
        self.timer.start(1000)

        # Inicialização das variáveis extras
        self.minutos = 0
        self.tempo = 0
        self.t_total = 0
        self.iniciado = False
        self.lblSetas.setVisible(False)
        self.btnFinalizar.setEnabled(False)

        self.btnPausar.setEnabled(False)
        self.pausado = False

        # Inicialização do pygame
        mixer.init()
        self.base_dados = 'progressos.db'

        self.conexao()

        # Alarme
        self.alarme = Alarme(self.lblAlarme, self.rbMusica, self.rbPadrao, self.lblCaminho, self.txtHora,
                             self.cbAposAlarme, self.cbOpcao, self.formatoHora, self.btnAtivar)

        self.btnAtivar.clicked.connect(self.alarme.verifica)
        self.rbMusica.clicked.connect(self.alarme.add_Musica)

        # Reprodutor
        self.reprodutor = Reprodutor(self.cbFicheiros, self.lblReproducao, self.hsVolume, self.btnRandom, self.btnMuted,
                                     self.lblTempo)
        self.reprodutor.start()

        self.hsVolume.setValue(50)

        self.btnAddMusica.clicked.connect(self.reprodutor.add_files)
        self.btnPlay.clicked.connect(self.reprodutor.play_music)
        self.btnNext.clicked.connect(self.reprodutor.next_music)
        self.btnPrev.clicked.connect(self.reprodutor.prev_music)
        self.btnStop.clicked.connect(self.reprodutor.stop_music)
        self.btnPause.clicked.connect(self.reprodutor.pause_music)
        self.btnDelete.clicked.connect(self.reprodutor.limpar_musicas)
        self.btnRandom.clicked.connect(self.reprodutor.music_random)
        self.btnMuted.clicked.connect(self.reprodutor.music_muted)
        self.hsVolume.valueChanged.connect(self.reprodutor.music_volume)
        self.cbFicheiros.currentIndexChanged.connect(self.reprodutor.select_music)

        # Ação aos botões do contador de tempo
        self.btnIniciar.clicked.connect(self.verificao)
        self.btnPausar.clicked.connect(self.pause)
        self.btnSobre.clicked.connect(self.sobre)
        self.btnFinalizar.clicked.connect(self.finalizar_execucao)
        self.btnRestaurar.clicked.connect(self.reiniciar_t_total)
        self.btnGravar.clicked.connect(self.gravar_progressos)
        self.btnProgressos.clicked.connect(self.ver_progressos)

        # Ação dos botões de configuração do sistema
        self.btnEncerrar.clicked.connect(self.shutdown)
        self.btnReiniciar.clicked.connect(self.reiniciar)
        self.btnHibernar.clicked.connect(self.hibernar)

        self.btnCancelar.clicked.connect(self.usuario)

        self.retranslateUi(MainWindow)
        self.cbOpcao.setCurrentIndex(0)
        self.cbFicheiros.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LSTime"))
        self.label.setText(_translate("MainWindow", "Gestão do Tempo"))
        self.btnAtivar.setToolTip(_translate("MainWindow", "Ativar Alarme"))
        self.btnAtivar.setText(_translate("MainWindow", "Ativar"))
        self.txtHora.setToolTip(_translate("MainWindow", "Adicionar tempo do Alarme"))
        self.lblAlarme.setText(_translate("MainWindow", "Adicionar Alarme"))
        self.label_9.setText(_translate("MainWindow", "Computador"))
        self.btnEncerrar.setToolTip(_translate("MainWindow", "Desligar o Computador"))
        self.btnEncerrar.setText(_translate("MainWindow", "Encerrar"))
        self.btnReiniciar.setToolTip(_translate("MainWindow", "Reiniciar o Computador"))
        self.btnReiniciar.setText(_translate("MainWindow", "Reiniciar"))
        self.btnHibernar.setToolTip(_translate("MainWindow", "Hibernar Computador"))
        self.btnHibernar.setText(_translate("MainWindow", "Hibernar"))
        self.btnCancelar.setText(_translate("MainWindow", "Usuário"))
        self.cbAposAlarme.setToolTip(_translate("MainWindow", "O que fazer depois que o alarme for concluido"))
        self.cbAposAlarme.setText(_translate("MainWindow", "Após o Alarme:"))
        self.cbOpcao.setCurrentText(_translate("MainWindow", "Fechar Aplicação"))
        self.cbOpcao.setItemText(0, _translate("MainWindow", "Fechar Aplicação"))
        self.cbOpcao.setItemText(1, _translate("MainWindow", "Encerrar PC"))
        self.cbOpcao.setItemText(2, _translate("MainWindow", "Reiniciar PC"))
        self.cbOpcao.setItemText(3, _translate("MainWindow", "Hibernar PC"))
        self.rbMusica.setToolTip(_translate("MainWindow", "Usar música como toque de alarme"))
        self.rbMusica.setText(_translate("MainWindow", "Música"))
        self.rbPadrao.setToolTip(_translate("MainWindow", "Usar um toque predefinido"))
        self.rbPadrao.setText(_translate("MainWindow", "Padrão"))
        self.lblCaminho.setToolTip(_translate("MainWindow", "Caminho do ficheiro de música"))
        self.lblCaminho.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", "Tempo Restante"))
        self.txtTempoEstudo.setToolTip(_translate("MainWindow", "Adicionar tempo de Estudo em Minutos"))
        self.btnIniciar.setToolTip(_translate("MainWindow", "Contagem do tempo"))
        self.btnIniciar.setText(_translate("MainWindow", "Iniciar"))
        self.label_5.setText(_translate("MainWindow", "Tempo de Estudo"))
        self.label_2.setText(_translate("MainWindow", "Min"))
        self.lblSegundos.setText(_translate("MainWindow", ""))
        self.lblHoraRestante.setText(_translate("MainWindow", "00:00"))
        self.label_7.setText(_translate("MainWindow", "H"))
        self.btnFinalizar.setToolTip(_translate("MainWindow", "Finalizar tempo de Estudo"))
        self.btnFinalizar.setText(_translate("MainWindow", "Finalizar"))
        self.btnSobre.setToolTip(_translate("MainWindow", "Informações sobre a Aplicação"))
        self.btnSobre.setText(_translate("MainWindow", "Sobre"))
        self.label_8.setText(_translate("MainWindow", "Tempo Total"))
        self.lblTempoTotal.setToolTip(_translate("MainWindow", "Tempo total de estudo"))
        self.lblTempoTotal.setText(_translate("MainWindow", "0"))
        self.btnRestaurar.setToolTip(_translate("MainWindow", "Apagar tempo e recomeçar"))
        self.btnRestaurar.setText(_translate("MainWindow", "Reiniciar"))
        self.label_13.setText(_translate("MainWindow", "M"))
        self.lblSetas.setText(_translate("MainWindow", "<<<"))
        self.btnProgressos.setToolTip(_translate("MainWindow", "Visualizar progressos feitos"))
        self.btnProgressos.setText(_translate("MainWindow", "Ver Progressos"))
        self.btnGravar.setToolTip(_translate("MainWindow", "Gravar o tempo atual"))
        self.btnGravar.setText(_translate("MainWindow", "Gravar Progresso"))
        self.label_14.setText(_translate("MainWindow", "Fazer uma Pausa"))
        self.label_16.setText(_translate("MainWindow", "Min"))
        self.btnPausar.setToolTip(_translate("MainWindow", "Iniciar Intervalo"))
        self.btnPausar.setText(_translate("MainWindow", "Pausar"))
        self.btnRandom.setToolTip(_translate("MainWindow", "Aleatório"))
        self.btnMuted.setToolTip(_translate("MainWindow", "Sem Som"))
        self.hsVolume.setToolTip(_translate("MainWindow", "Aumentar ou diminur volume"))
        self.btnDelete.setToolTip(_translate("MainWindow", "Apagar músicas do reprodutor"))
        self.btnPrev.setToolTip(_translate("MainWindow", "Previous"))
        self.btnNext.setToolTip(_translate("MainWindow", "Next"))
        self.btnStop.setToolTip(_translate("MainWindow", "Stop"))
        self.btnPlay.setToolTip(_translate("MainWindow", "Play"))
        self.btnPause.setToolTip(_translate("MainWindow", "Pause"))
        self.btnAddMusica.setToolTip(_translate("MainWindow", "Adicionar músicas no reprodutor"))
        self.lblTempoRestante.setText(_translate("MainWindow", "0"))
        self.label_21.setText(_translate("MainWindow", "Min"))
        self.lblReproducao.setText(_translate("MainWindow", ""))
        self.lblTempo.setText(_translate("MainWindow", "--:--"))
        self.cbFicheiros.setCurrentText(_translate("MainWindow", ""))
        self.cbFicheiros.setItemText(0, _translate("MainWindow", ""))
        self.label_18.setText(_translate("MainWindow", "LSPlayer"))

    # Criação dos métodos para configuração do sistema
    def shutdown(self):
        shutdown = QMessageBox.question(None, 'Encerrar PC',
                                        'Esta opção vai Encerrar o Computador\n\n\tDeseja Continuar?',
                                        QMessageBox.Ok | QMessageBox.No)
        if shutdown == QMessageBox.Ok:
            os.popen('shutdown /p').read()
        else:
            pass

    def reiniciar(self):
        restart = QMessageBox.question(None, 'Reiniciar PC',
                                       'Esta opção vai Encerrar totalmente e reiniciar o computador\n\n\tDeseja '
                                       'Continuar?', QMessageBox.Ok | QMessageBox.No)
        if restart == QMessageBox.Ok:
            os.popen('shutdown -r').read()
        else:
            pass

    def hibernar(self):
        hibernar = QMessageBox.question(None, 'PC to hibernate',
                                        'Esta opção vai Hiberna o computador\n\n\tDeseja Continuar?',
                                        QMessageBox.Ok | QMessageBox.No)
        if hibernar == QMessageBox.Ok:
            os.popen('shutdown -h /f').read()
        else:
            pass

    def usuario(self):
        dialog = QtWidgets.QDialog()
        janela = usuario.Ui_Dialog()
        janela.setupUi(dialog)
        dialog.exec_()

    # Métodos para data e hora
    def hora_data(self):
        hora = QtCore.QTime.currentTime()
        formatoHora = hora.toString('hh:mm:ss')
        self.lcdHora.display(formatoHora)
        data = QtCore.QDate.currentDate()
        formatoData = data.toString('dd/MM/yyyy')
        self.lcdData.display(formatoData)

    def sobre(self):
        dialog = QtWidgets.QDialog()
        janela = sobre.Ui_Dialog()
        janela.setupUi(dialog)
        dialog.exec_()

    def informacao_cadastro(self, titulo, informacao):
        mensagem = QtWidgets.QMessageBox()
        mensagem.setIcon(QtWidgets.QMessageBox.Information)
        icone = QtGui.QIcon()
        icone.addPixmap(QtGui.QPixmap('files/LSTime.ico'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mensagem.setWindowIcon(icone)
        mensagem.setWindowTitle(titulo)
        mensagem.setText(informacao)
        mensagem.exec_()

    def erro_gravacao(self, titulo, mensagem):
        erro = QtWidgets.QMessageBox()
        erro.setIcon(QtWidgets.QMessageBox.Critical)
        icone = QtGui.QIcon()
        icone.addPixmap(QtGui.QPixmap('files/LSTime.ico'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        erro.setWindowIcon(icone)
        erro.setWindowTitle(titulo)
        erro.setText(mensagem)
        erro.exec_()

    # Criação dos métodos para conexão e cadastro dos progressos feitos
    def conexao(self):
        connect = sqlite3.connect(self.base_dados)
        cursor = connect.cursor()
        try:
            cursor.execute("create table if not exists progressos ("
                           "id integer primary key autoincrement,"
                           "minutos text,"
                           "dataCadastro text)")
            connect.commit()
            connect.close()
        except BaseException as error:
            print(error)

    def gravar_progressos(self):
        data = QtCore.QDate.currentDate()
        formatoData = str(data.toString('dd / MM / yyyy'))
        tempo_total = str(self.lblTempoTotal.text())

        if len(tempo_total) < 2 or tempo_total == '0':
            self.erro_gravacao('Tempo total em falta', '\nNão existe tempo total para ser gravado!\n')
        else:
            conexao = sqlite3.connect(self.base_dados)
            cursor = conexao.cursor()
            try:
                execucao = cursor.execute("insert into progressos(id, minutos, dataCadastro) values(null,?,?)", (tempo_total, formatoData))
                conexao.commit()
                conexao.close()
                self.informacao_cadastro('Sucesso', '\nTempo gravado com sucesso...\n')
                self.lblTempoTotal.setText('0')
            except BaseException as falha:
                print(falha)

    def ver_progressos(self):
        dialog = QtWidgets.QDialog()
        janela = progressos.Ui_Dialog()
        janela.setupUi(dialog)
        dialog.exec_()

    def execucao(self):
        self.btnIniciar.setText('Parar')
        self.btnGravar.setEnabled(False)
        self.btnRestaurar.setEnabled(False)
        self.txtTempoEstudo.setEnabled(False)
        self.btnPausar.setEnabled(True)
        self.lblSetas.setVisible(False)
        self.btnFinalizar.setEnabled(False)

    def fim_Execucao(self):
        self.btnIniciar.setText('Iniciar')
        self.btnIniciar.setEnabled(True)
        self.btnGravar.setEnabled(True)
        self.btnRestaurar.setEnabled(True)
        self.txtTempoEstudo.setEnabled(True)
        self.btnFinalizar.setEnabled(False)
        self.btnPausar.setEnabled(False)
        self.lblSetas.setVisible(False)
        self.lblSegundos.setText("")
        self.lblTempoRestante.setText('0')
        self.lblHoraRestante.setText('0:0')
        # self.iniciado = False

    # Função para finalizar a execução da thread
    def finalizar_execucao(self):
        self.tempo_total()
        self.iniciado = False
        self.parar_Thread()

    def som(self):
        ficheiro = 'files/contador.wav'
        mixer.music.load(ficheiro)
        print('Ficheiro:', ficheiro)
        while self.minutos == 0:
            mixer.music.play()
            time.sleep(2)

    # Instrução que converte minutos em horas restantes
    def conversor(self):
        if self.minutos == 0:
            hora = 0
            minutos = 0
        else:
            hora = self.minutos // 60
            minutos = self.minutos % 60
        formato = '{}:{}'.format(hora, minutos)
        self.lblHoraRestante.setText(formato)

    def run(self):
        segundos = 60
        self.minutos = int(self.txtTempoEstudo.text())
        if self.minutos < 10:
            winsound.PlaySound('SystemExit', winsound.SND_ALIAS)
        else:
            self.lblTempoRestante.setText(str(self.minutos))
            self.tempo = self.minutos
            self.conversor()
            self.execucao()
            while self.minutos > 0:
                if self.pausado == True:
                    pass
                else:
                    segundos -= 1
                    self.lblSegundos.setText(str(segundos))
                    self.iniciado = True
                    if segundos == 0:
                        segundos = 60
                        self.minutos -= 1
                        self.lblTempoRestante.setText(str(self.minutos))
                        self.conversor()
                        if self.minutos == 0:
                            self.conversor()
                            self.lblSetas.setVisible(True)
                            self.btnIniciar.setEnabled(False)
                            self.btnFinalizar.setEnabled(True)
                            self.som()
                            break
                time.sleep(1)
            # self.fim_Execucao()

    def iniciarThread(self):
        self.start()

    def parar_Thread(self):
        self.tempo = 0
        self.pausado = True
        self.pause()
        self.fim_Execucao()
        self.terminate()

    def verificao(self):
        if self.iniciado == False:
            self.iniciarThread()
        else:
            self.parar_Thread()
            self.iniciado = False

    def tempo_total(self):
        self.t_total += int(self.tempo)
        self.lblTempoTotal.setText(str(self.t_total))

    # Reinicializar o tempo total
    def reiniciar_t_total(self):
        tempo = self.lblTempoTotal.text()
        if tempo == '0' or tempo == 0:
            print('Tempo vazio')
        else:
            reinicio = QMessageBox.question(None, 'Apagar Progresso',
                                            'Está ação irá apagar todo progresso feito até agora\n\n\tDeseja continuar?', QMessageBox.Ok | QMessageBox.No)
            if reinicio == QMessageBox.Ok:
                self.t_total = 0
                self.lblTempoTotal.setText(str(self.t_total))
            else:
                pass

    # Configuração do botão Pause
    def pause(self):
        if self.pausado == False:
            self.btnPausar.setText('Continuar')
            self.btnPausar.setStyleSheet('QPushButton{background:#f00;border:none;color:#fff;}'
                                         'QPushButton:hover{background:#0F4F93;color:#fff;}')
            self.btnPausar.setToolTip('Continuar o Contador')
            self.pausado = True
        else:
            self.btnPausar.setText('Pausar')
            self.btnPausar.setStyleSheet('QPushButton{background:#28A745;border:none;color:#fff;}'
                                         'QPushButton:hover{background:#0F4F93;color:#fff;}')
            self.btnPausar.setToolTip('Pausar o Contador')
            self.pausado = False

    def pause_false(self):
        self.btnPausar.setText('Pausar')
        self.btnPausar.setStyleSheet('QPushButton{background:#28A745;border:none;color:#fff;}'
                                     'QPushButton:hover{background:#0F4F93;color:#fff;}')
        self.btnPausar.setToolTip('Pausar o Contador')

    def musica_Padrao(self):
        if self.rbMusica.checkStateSet():
            pass


class Alarme(Ui_MainWindow, threading.Thread):
    def __init__(self, lblAlarme, rbMusica, rbPadrao, lblCaminho, txtHora, cbAposAlarme, cbOpcao, formatoHora,
                 btnAtivar):
        super(Alarme, self).__init__()

        self.lblAlarme = lblAlarme
        self.rbMusica = rbMusica
        self.rbPadrao = rbPadrao
        self.lblCaminho = lblCaminho
        self.txtHora = txtHora
        self.cbAposAlarme = cbAposAlarme
        self.cbOpcao = cbOpcao
        self.formatoHora = formatoHora
        self.btnAtivar = btnAtivar
        self.caminho = ''
        self.init = False

    def add_Musica(self):
        if self.lblCaminho.text() == '':
            self.caminho, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Adicionar Música', 'C:\\Users\\User\\Music',
                                                                    filter='Músicas (*.mp3 *.wma *.wav *.ogg *.flac *.m4a)')
            caminho_total = str(self.caminho)
            caminho_absoluto = os.path.basename(caminho_total)
            if self.caminho != '' and len(self.caminho) > 1:
                self.lblCaminho.setText(str(caminho_total))
                self.lblCaminho.setToolTip(str(self.caminho))
            else:
                self.rbPadrao.setChecked(True)
        else:
            self.rbMusica.setChecked(True)

    def musica_alarme(self):
        if self.caminho != '':
            mixer.music.load(self.caminho)
            mixer.music.play(1)
        else:
            pass

    def padrao_alarme(self):
        file = 'files/alarme.wav'
        mixer.music.load(file)
        while self.init == True:
            mixer.music.play()
            time.sleep(1.2)

    def inicio_alarme(self):
        self.rbMusica.setEnabled(False)
        self.rbPadrao.setEnabled(False)
        self.txtHora.setEnabled(False)

    def fim_alarme(self):
        self.rbMusica.setEnabled(True)
        self.rbMusica.setChecked(False)
        self.rbPadrao.setEnabled(True)
        self.rbPadrao.setChecked(True)
        self.txtHora.setEnabled(True)
        self.caminho = ''
        self.cbAposAlarme.setChecked(False)
        self.lblCaminho.setText('')
        self.lblCaminho.setToolTip('')

    def alerta(self):
        info = QtWidgets.QMessageBox()
        info.setIcon(QtWidgets.QMessageBox.Warning)
        icone = QtGui.QIcon()
        icone.addPixmap(QtGui.QPixmap('files/LSTime.ico'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        info.setWindowIcon(icone)
        info.setText('Adiciona uma Música como toque de alarme')
        info.setWindowTitle('Erro - Música não adicionada')
        info.setDefaultButton(QtWidgets.QMessageBox.Ok)
        info.exec_()

    def alarme_ativo(self):
        if self.init == True:
            self.lblAlarme.setText('Alarme Ativo')
            font = QtGui.QFont()
            font.setFamily("Agency FB")
            font.setPointSize(20)
            font.setBold(True)
            self.lblAlarme.setFont(font)
            self.lblAlarme.setStyleSheet('background:#f00;color:#fff')
        else:
            self.lblAlarme.setText('Adicionar Alarme')
            font = QtGui.QFont()
            font.setFamily("Agency FB")
            font.setPointSize(20)
            font.setBold(False)
            self.lblAlarme.setFont(font)
            self.lblAlarme.setStyleSheet('background:#fff;color:#9C27B0')

    def run(self):
        global valor
        valor = 0
        self.init = True
        tempo = str(self.txtHora.text())
        self.btnAtivar.setText('Parar')
        self.alarme_ativo()
        self.inicio_alarme()
        while True:
            hora = QtCore.QTime.currentTime()
            formHora = hora.toString('hh:mm:ss')
            if formHora[0:5] == tempo:
                if self.rbMusica.isChecked() == True:
                    self.opcoes()
                    self.musica_alarme()
                    while valor <= 300:
                        print(valor, ' ', end="")
                        valor += 1
                        time.sleep(1)
                else:
                    self.opcoes()
                    self.padrao_alarme()
            else:
                pass
            time.sleep(1)

    def verifica(self):
        if self.init == False:
            if self.rbMusica.isChecked() == False and self.rbPadrao.isChecked() == False:
                self.alerta()
            elif self.rbMusica.isChecked() == True and self.lblCaminho.text() == '':
                self.alerta()
            elif self.rbPadrao.isChecked() == True:
                self.start()
            else:
                self.start()
        else:
            self.parar_Alarme()

    def parar_Alarme(self):
        self.btnAtivar.setText('Ativar')
        self.init = False
        valor = 0
        if mixer.music.get_busy() == True:
            mixer.music.stop()
        self.fim_alarme()
        self.alarme_ativo()
        self.terminate()

    def opcoes(self):
        index = self.cbOpcao.currentIndex()
        print(index)

        if self.cbAposAlarme.isChecked() == False:
            pass
        else:
            if index == 0:
                print('Fechar Aplicação')
                quit(0)
            elif index == 1:
                print('Desligar')
                os.popen('shutdown /p').read()
            elif index == 2:
                print('Reiniciar')
                os.popen('shutdown -r').read()
            elif index == 3:
                print('Hiberna')
                os.popen('shutdown -h /f').read()
                self.parar_Alarme()
            else:
                print('Fim da condição')


class Reprodutor(Ui_MainWindow, threading.Thread):
    def __init__(self, cbFicheiros, lblReproducao, hsVolume, btnRandom, btnMuted, lblTempo):
        super(Reprodutor, self).__init__()

        self.cbFicheiros = cbFicheiros
        self.lblReproducao = lblReproducao
        self.hsVolume = hsVolume
        self.btnRandom = btnRandom
        self.btnMuted = btnMuted
        self.lblTempo = lblTempo

        self.lista_musicas = []
        self.index = 0
        self.paused = False
        self.random = False
        self.muted = False
        self.duracao = 0
        self.stop = False

    def add_files(self):
        ficheiros, _ = QtWidgets.QFileDialog.getOpenFileNames(None, 'Adicionar Músicas', 'C:\\Users\\User\\Music',
                                                              filter='Músicas (*.mp3 *.wav *.flac)')
        if ficheiros != '' or not (ficheiros.__contains__('.wma')):
            for musica in ficheiros:
                ficheiro_absoluto = os.path.basename(musica)
                self.lista_musicas.append(musica)
                self.cbFicheiros.addItem(ficheiro_absoluto)
        else:
            pass

    def play_music(self):
        if len(self.lista_musicas) < 1:
            pass
        else:
            try:
                if self.paused == True:
                    mixer.music.unpause()
                else:
                    mixer.music.load(self.lista_musicas[self.index])
                    mixer.music.play()
                    self.m_duracao()
                self.information()
                self.paused = False
                self.stop = False
            except BaseException as be:
                print(be)
                print('Erro de Formato')

    def m_duracao(self):
        # duracao = 0
        if str(self.lista_musicas[self.index]).endswith(".wav"):
            tempo = mixer.Sound(self.lista_musicas[self.index])
            self.duracao = int(tempo.get_length())

        elif str(self.lista_musicas[self.index]).endswith(".mp3"):
            audio = MP3(self.lista_musicas[self.index])
            self.duracao = int(audio.info.length)

        elif str(self.lista_musicas[self.index]).endswith(".flac"):
            audio = FLAC(self.lista_musicas[self.index])
            self.duracao = int(audio.info.length)
        else:
            pass

        minutos, segundos = divmod(self.duracao, 60)
        tempo_duracao = '%.f:%.f' % (minutos, segundos)
        self.lblTempo.setText(tempo_duracao)

    def next_music(self):
        if self.random == True:
            try:
                aleatorio = random.randint(0, len(self.lista_musicas) - 1)
                self.index = aleatorio
                self.play_music()
            except ValueError:
                pass
            except Exception as e:
                print(e)
        else:
            if len(self.lista_musicas) == 0:
                pass
            elif len(self.lista_musicas) == 1:
                self.paused = False
                self.play_music()
            elif self.index == len(self.lista_musicas) - 1:
                self.index = 0
                self.paused = False
                self.play_music()
            else:
                self.paused = False
                self.index += 1
                self.play_music()

    def prev_music(self):
        ultima_musica = self.index * (-1)
        if self.random == True:
            try:
                aleatorio = random.randint(0, len(self.lista_musicas) - 1)
                self.index = aleatorio
                self.play_music()
            except ValueError:
                pass
            except Exception as e:
                print(e)
        else:
            if len(self.lista_musicas) == 0:
                pass
            elif len(self.lista_musicas) == 1:
                self.paused = False
                self.play_music()
            else:
                if ultima_musica == len(self.lista_musicas) - 1:
                    self.paused = False
                    self.index = 0
                    self.play_music()
                else:
                    self.paused = False
                    self.index -= 1
                    self.play_music()

    def stop_music(self):
        if len(self.lista_musicas) > 0:
            mixer.music.stop()
            self.lblReproducao.setText("STOPED...")
            self.paused = False
            self.stop = True
        else:
            self.index = 0

    def pause_music(self):
        if len(self.lista_musicas) > 0 and self.stop == False:
            mixer.music.pause()
            self.lblReproducao.setText("PAUSED...")
            self.paused = True
        elif len(self.lista_musicas) > 0 and self.stop == True:
            print('Stop True')
            self.paused = False
        else:
            self.index = 0

    def music_random(self):
        if self.random == False:
            self.random = True
            icon5 = QtGui.QIcon()
            icon5.addPixmap(QtGui.QPixmap("files/player/random.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btnRandom.setIcon(icon5)
        else:
            self.random = False
            icon5 = QtGui.QIcon()
            icon5.addPixmap(QtGui.QPixmap("files/player/randomB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btnRandom.setIcon(icon5)

    def music_muted(self):
        if self.muted == False:
            mixer.music.set_volume(0)
            self.hsVolume.setValue(0)
            self.muted = True
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap("files/player/mute.png"))
            self.btnMuted.setIcon(icon6)
        else:
            mixer.music.set_volume(.5)
            self.hsVolume.setValue(50)
            self.muted = False
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap("files/player/volume.png"))
            self.btnMuted.setIcon(icon6)

    def music_volume(self, valor):
        volume = int(valor) / 100
        mixer.music.set_volume(volume)
        if volume == 0:
            self.muted = True
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap("files/player/mute.png"))
            self.btnMuted.setIcon(icon6)
        else:
            self.muted = False
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap("files/player/volume.png"))
            self.btnMuted.setIcon(icon6)

    def select_music(self):
        if len(self.lista_musicas) > 0:
            self.index = self.cbFicheiros.currentIndex()
            self.play_music()
        else:
            pass

    def information(self):
        self.lblReproducao.setText(os.path.basename(self.lista_musicas[self.index]))
        self.lblReproducao.setToolTip(os.path.basename(self.lista_musicas[self.index]))

    def limpar_musicas(self):
        self.stop_music()
        self.lista_musicas.clear()
        self.cbFicheiros.clear()
        self.lblReproducao.setText("")
        self.cbFicheiros.setCurrentText("")
        self.cbFicheiros.setCurrentIndex(0)
        self.lblTempo.setText('')
        self.lblReproducao.setToolTip('')

    def run(self):
        while True:
            if len(self.lista_musicas) == 0:
                pass
            elif len(self.lista_musicas) == 1:
                self.next_music()
                while self.duracao > 0:
                    if self.paused == True:
                        pass
                    elif self.paused == False:
                        self.duracao -= 1
                    # print('Duração:', self.duracao)
                    time.sleep(.99)
            else:
                while self.index <= len(self.lista_musicas):
                    self.next_music()
                    while self.duracao > 0:
                        if self.paused == True:
                            pass
                        elif self.paused == False:
                            self.duracao -= 1
                        # print('Duração:', self.duracao)
                        time.sleep(1)
                    # print('Índex:', self.index)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
