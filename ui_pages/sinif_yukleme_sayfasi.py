# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_pages\sinif_yukleme_sayfasi.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SinifYukleForm(object):
    def setupUi(self, SinifYukleForm):
        SinifYukleForm.setObjectName("SinifYukleForm")
        SinifYukleForm.resize(376, 714)
        self.gridLayout = QtWidgets.QGridLayout(SinifYukleForm)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(SinifYukleForm)
        self.frame.setStyleSheet("QFrame{\n"
"background: #354152;\n"
"}\n"
"\n"
"QLineEdit{\n"
" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    min-width: 6em;\n"
"    font-size:20px;\n"
"    padding-left:15px;\n"
"    height:42px;\n"
"    border-radius:15px;\n"
"    border-color: #303030;\n"
"    background: transparent;\n"
"    color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"border-radius: 15px;\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.466409, x2:0.188, y2:0.482727, stop:0.823864 rgba(82, 185, 143, 255), stop:1 rgba(115, 185, 153, 255));\n"
"padding: 8px 16px;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"QPushButton#btn_login:pressed{\n"
"color: black;\n"
"background: #008bd1\n"
"}\n"
"QCommandLinkButton{\n"
"font-size: 16px;\n"
"background: #4c5d75;\n"
"}\n"
"QCommandLinkButton:pressed{\n"
"    background-color: rgb(92, 186, 138);\n"
"}\n"
"\n"
"\n"
"QCheckBox{\n"
"font-size:24px;\n"
"color:white;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator{\n"
"    height:25px;\n"
"    width:25px;\n"
"\n"
"}\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    min-width: 6em;\n"
"    font-size:20px;\n"
"    padding-left:15px;\n"
"    height:42px;\n"
"    border-radius:15px;\n"
"    border-color: #303030;\n"
"    background: transparent;\n"
"    color:white;\n"
"\n"
"}\n"
"\n"
"QComboBox:on {\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border-bottom-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    background: #354152;\n"
"    border: 1px solid gray;\n"
"    color:white;\n"
"\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-color: white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, -20, 351, 731))
        self.frame_2.setStyleSheet("QFrame{\n"
"background: #354152;\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size:24px;\n"
"    color:white;\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"border-radius:10px;\n"
"padding-left: 15px;\n"
"font-size:16px;\n"
"\n"
"}\n"
"QPushButton{\n"
"height:32px;\n"
"border-radius: 15px;\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.466409, x2:0.188, y2:0.482727, stop:0.823864 rgba(82, 185, 143, 255), stop:1 rgba(115, 185, 153, 255));\n"
"padding: 8px 16px;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"QPushButton:pressed{\n"
"color: black;\n"
"background: #008bd1\n"
"}\n"
"\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    min-width: 6em;\n"
"    font-size:16px;\n"
"    padding-left:15px;\n"
"\n"
"}\n"
"\n"
"QComboBox:on {\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border-bottom-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    background: white;\n"
"    border: 1px solid gray;\n"
"    box-shadow: transparent;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-color: transparent;\n"
"}\n"
"\n"
"\n"
"\n"
"QSpinBox{\n"
"height:42px;\n"
"}\n"
"\n"
"QSpinBox {\n"
"    /*text-align: center;*/\n"
"    padding-right: 15px;\n"
"    border-width: 5px;\n"
"    border-radius:10px;\n"
"    padding-left:15px;\n"
"    font-size:20px;\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"     subcontrol-origin: border;\n"
"     padding-left: 10px;\n"
"     padding-right: 40px;\n"
"     width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
"     /*height: 14px;*/\n"
"     border-width: 1px;\n"
"     border-radius: 5px;\n"
"     background-color: #eeeeee;\n"
"\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-position: top right; /* position at the top right corner */\n"
"    height:42px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #bbbb;\n"
"}\n"
"\n"
"QSpinBox::up-arrow:disabled, QSpinBox::down-arrow:disabled {\n"
"    image: none;\n"
"}\n"
"QSpinBox::up-arrow, QSpinBox::down-arrow {\n"
"     width: 20px;\n"
"     height: 20px;\n"
"     border: 1px;\n"
"}\n"
"QSpinBox::up-arrow {\n"
"padding-left:20px;\n"
"    image: url(:/resimler/icons/chevron-up.png);\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-position: bottom left; /* position at bottom right corner */\n"
"    height:42px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"image: url(:/resimler/icons/chevron-down.png);\n"
"padding-left:20px;\n"
"}\n"
"\n"
"QGroupBox{\n"
"border: none;\n"
"}\n"
"\n"
"QToolButton{\n"
"margin-left:10px;\n"
"height:42px;\n"
"width:500px;\n"
" border-width: 1px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox.setStyleSheet("QLineEdit{\n"
"height:42px;\n"
"}\n"
"QComboBox{\n"
"height:42px;\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cmb_Vardiya = QtWidgets.QComboBox(self.groupBox)
        self.cmb_Vardiya.setObjectName("cmb_Vardiya")
        self.gridLayout_2.addWidget(self.cmb_Vardiya, 5, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.btn_kayit = QtWidgets.QPushButton(self.groupBox)
        self.btn_kayit.setObjectName("btn_kayit")
        self.gridLayout_2.addWidget(self.btn_kayit, 8, 0, 1, 3)
        self.txt_Adi = QtWidgets.QLineEdit(self.groupBox)
        self.txt_Adi.setText("")
        self.txt_Adi.setPlaceholderText("")
        self.txt_Adi.setObjectName("txt_Adi")
        self.gridLayout_2.addWidget(self.txt_Adi, 3, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 5, 0, 1, 1)
        self.txt_Soyadi = QtWidgets.QLineEdit(self.groupBox)
        self.txt_Soyadi.setText("")
        self.txt_Soyadi.setPlaceholderText("")
        self.txt_Soyadi.setObjectName("txt_Soyadi")
        self.gridLayout_2.addWidget(self.txt_Soyadi, 4, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.txt_Vardiyano = QtWidgets.QLineEdit(self.groupBox)
        self.txt_Vardiyano.setText("")
        self.txt_Vardiyano.setPlaceholderText("")
        self.txt_Vardiyano.setObjectName("txt_Vardiyano")
        self.gridLayout_2.addWidget(self.txt_Vardiyano, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 2)
        self.gridLayout_3.addWidget(self.groupBox, 3, 0, 1, 1)
        self.btn_resimCek = QtWidgets.QToolButton(self.frame_2)
        self.btn_resimCek.setObjectName("btn_resimCek")
        self.gridLayout_3.addWidget(self.btn_resimCek, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(SinifYukleForm)
        QtCore.QMetaObject.connectSlotsByName(SinifYukleForm)

    def retranslateUi(self, SinifYukleForm):
        _translate = QtCore.QCoreApplication.translate
        SinifYukleForm.setWindowTitle(_translate("SinifYukleForm", "Form"))
        self.label_3.setText(_translate("SinifYukleForm", "Adı"))
        self.btn_kayit.setText(_translate("SinifYukleForm", "İşçi Ekle"))
        self.label_10.setText(_translate("SinifYukleForm", "Vardiya"))
        self.label_5.setText(_translate("SinifYukleForm", "Soyadı"))
        self.label_2.setText(_translate("SinifYukleForm", "İşçi  No"))
        self.btn_resimCek.setText(_translate("SinifYukleForm", "Resim Çek"))
        self.label.setText(_translate("SinifYukleForm", "KAMERA EKRANI"))