# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTuiFrame_become_member.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame_become_member(object):
    def setupUi(self, Frame_become_member):
        Frame_become_member.setObjectName("Frame_become_member")
        Frame_become_member.resize(452, 340)
        self.gridLayout = QtWidgets.QGridLayout(Frame_become_member)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 59, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(79, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Frame_become_member)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Frame_become_member)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(Frame_become_member)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(Frame_become_member)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_mname = QtWidgets.QLineEdit(Frame_become_member)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_mname.setFont(font)
        self.lineEdit_mname.setText("")
        self.lineEdit_mname.setObjectName("lineEdit_mname")
        self.verticalLayout_2.addWidget(self.lineEdit_mname)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_man = QtWidgets.QRadioButton(Frame_become_member)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_man.setFont(font)
        self.radioButton_man.setObjectName("radioButton_man")
        self.horizontalLayout.addWidget(self.radioButton_man)
        self.radioButton_woman = QtWidgets.QRadioButton(Frame_become_member)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_woman.setFont(font)
        self.radioButton_woman.setChecked(True)
        self.radioButton_woman.setObjectName("radioButton_woman")
        self.horizontalLayout.addWidget(self.radioButton_woman)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.lineEdit_mtel = QtWidgets.QLineEdit(Frame_become_member)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_mtel.setFont(font)
        self.lineEdit_mtel.setText("")
        self.lineEdit_mtel.setObjectName("lineEdit_mtel")
        self.verticalLayout_2.addWidget(self.lineEdit_mtel)
        self.dateEdit_mdate = QtWidgets.QDateEdit(Frame_become_member)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dateEdit_mdate.setFont(font)
        self.dateEdit_mdate.setObjectName("dateEdit_mdate")
        self.verticalLayout_2.addWidget(self.dateEdit_mdate)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.label_hint = QtWidgets.QLabel(Frame_become_member)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_hint.setFont(font)
        self.label_hint.setText("")
        self.label_hint.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hint.setObjectName("label_hint")
        self.verticalLayout_3.addWidget(self.label_hint)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_ensure = QtWidgets.QPushButton(Frame_become_member)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_ensure.setFont(font)
        self.pushButton_ensure.setObjectName("pushButton_ensure")
        self.horizontalLayout_3.addWidget(self.pushButton_ensure)
        self.pushButton_back = QtWidgets.QPushButton(Frame_become_member)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")
        self.horizontalLayout_3.addWidget(self.pushButton_back)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(76, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 59, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)

        self.retranslateUi(Frame_become_member)
        QtCore.QMetaObject.connectSlotsByName(Frame_become_member)

    def retranslateUi(self, Frame_become_member):
        _translate = QtCore.QCoreApplication.translate
        Frame_become_member.setWindowTitle(_translate("Frame_become_member", "会员信息录入"))
        self.label.setText(_translate("Frame_become_member", "会员名"))
        self.label_2.setText(_translate("Frame_become_member", "姓别"))
        self.label_3.setText(_translate("Frame_become_member", "电话"))
        self.label_4.setText(_translate("Frame_become_member", "生日"))
        self.radioButton_man.setText(_translate("Frame_become_member", "男"))
        self.radioButton_woman.setText(_translate("Frame_become_member", "女"))
        self.pushButton_ensure.setText(_translate("Frame_become_member", "确认"))
        self.pushButton_back.setText(_translate("Frame_become_member", "返回"))

