# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parameter.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(253, 439)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 20, 205, 252))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.radioButton = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.radioButton)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_8.setLineWidth(0)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 380, 160, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(30, 300, 201, 81))
        self.textEdit.setReadOnly(False)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 280, 161, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "设置训练参数"))
        self.label_6.setText(_translate("Form", "confidence：0.5"))
        self.label_7.setText(_translate("Form", "Cuda：False"))
        self.radioButton.setText(_translate("Form", "True"))
        self.label_8.setText(_translate("Form", "Epoch：10"))
        self.label_9.setText(_translate("Form", "trainval_percent：1 "))
        self.label_10.setText(_translate("Form", "train_percent：1"))
        self.label_11.setText(_translate("Form", "Batch_size：8"))
        self.label_12.setText(_translate("Form", "lr：1e-5"))
        self.label_2.setText(_translate("Form", "loc_loss："))
        self.label_3.setText(_translate("Form", "conf_loss："))
        self.pushButton.setText(_translate("Form", "确定"))
        self.pushButton_2.setText(_translate("Form", "取消"))
        self.label.setText(_translate("Form", "设置类别标签：(用空格隔开)"))
