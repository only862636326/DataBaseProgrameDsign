# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTuiFrame_buy.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame_Buy(object):
    def setupUi(self, Frame_Buy):
        Frame_Buy.setObjectName("Frame_Buy")
        Frame_Buy.resize(678, 555)
        self.gridLayout_2 = QtWidgets.QGridLayout(Frame_Buy)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_buy = QtWidgets.QWidget(Frame_Buy)
        self.widget_buy.setObjectName("widget_buy")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_buy)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(33, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.widget_buy_info = QtWidgets.QWidget(self.widget_buy)
        self.widget_buy_info.setObjectName("widget_buy_info")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_buy_info)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.checkBox_buy_is_member = QtWidgets.QCheckBox(self.widget_buy_info)
        self.checkBox_buy_is_member.setObjectName("checkBox_buy_is_member")
        self.horizontalLayout_5.addWidget(self.checkBox_buy_is_member)
        self.widget_buy_member_info = QtWidgets.QWidget(self.widget_buy_info)
        self.widget_buy_member_info.setObjectName("widget_buy_member_info")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_buy_member_info)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_buy_mtel = QtWidgets.QRadioButton(self.widget_buy_member_info)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_buy_mtel.setFont(font)
        self.radioButton_buy_mtel.setChecked(True)
        self.radioButton_buy_mtel.setObjectName("radioButton_buy_mtel")
        self.horizontalLayout_2.addWidget(self.radioButton_buy_mtel)
        self.radioButton_buy_mno = QtWidgets.QRadioButton(self.widget_buy_member_info)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_buy_mno.setFont(font)
        self.radioButton_buy_mno.setObjectName("radioButton_buy_mno")
        self.horizontalLayout_2.addWidget(self.radioButton_buy_mno)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lineEdit_buy_member_input = QtWidgets.QLineEdit(self.widget_buy_member_info)
        self.lineEdit_buy_member_input.setObjectName("lineEdit_buy_member_input")
        self.verticalLayout.addWidget(self.lineEdit_buy_member_input)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget_buy_member_info)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_buy_show_mname = QtWidgets.QLabel(self.widget_buy_member_info)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_buy_show_mname.setFont(font)
        self.label_buy_show_mname.setObjectName("label_buy_show_mname")
        self.horizontalLayout_3.addWidget(self.label_buy_show_mname)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget_buy_member_info)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_buy_mi = QtWidgets.QLabel(self.widget_buy_member_info)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_buy_mi.setFont(font)
        self.label_buy_mi.setObjectName("label_buy_mi")
        self.horizontalLayout.addWidget(self.label_buy_mi)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5.addWidget(self.widget_buy_member_info)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.tableWidget_buy_info = QtWidgets.QTableWidget(self.widget_buy_info)
        self.tableWidget_buy_info.setMinimumSize(QtCore.QSize(350, 0))
        self.tableWidget_buy_info.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tableWidget_buy_info.setFont(font)
        self.tableWidget_buy_info.setTabletTracking(False)
        self.tableWidget_buy_info.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.tableWidget_buy_info.setRowCount(50)
        self.tableWidget_buy_info.setObjectName("tableWidget_buy_info")
        self.tableWidget_buy_info.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_buy_info.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_buy_info.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_buy_info.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_buy_info.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_buy_info.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_buy_info.setItem(2, 0, item)
        self.verticalLayout_3.addWidget(self.tableWidget_buy_info)
        self.label_buy_input_hint = QtWidgets.QLabel(self.widget_buy_info)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_buy_input_hint.setFont(font)
        self.label_buy_input_hint.setText("")
        self.label_buy_input_hint.setAlignment(QtCore.Qt.AlignCenter)
        self.label_buy_input_hint.setObjectName("label_buy_input_hint")
        self.verticalLayout_3.addWidget(self.label_buy_input_hint)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.widget_buy_info)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.widget_buy_info)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.widget_buy_info)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.label_buy_allprice = QtWidgets.QLabel(self.widget_buy_info)
        self.label_buy_allprice.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_buy_allprice.setFont(font)
        self.label_buy_allprice.setText("")
        self.label_buy_allprice.setObjectName("label_buy_allprice")
        self.horizontalLayout_4.addWidget(self.label_buy_allprice)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_4 = QtWidgets.QLabel(self.widget_buy_info)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_11.addWidget(self.label_4)
        self.lineEdit_buy_pay_money = QtWidgets.QLineEdit(self.widget_buy_info)
        self.lineEdit_buy_pay_money.setObjectName("lineEdit_buy_pay_money")
        self.horizontalLayout_11.addWidget(self.lineEdit_buy_pay_money)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.label_7 = QtWidgets.QLabel(self.widget_buy_info)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.lineEdit_odd_change = QtWidgets.QLineEdit(self.widget_buy_info)
        self.lineEdit_odd_change.setEnabled(False)
        self.lineEdit_odd_change.setObjectName("lineEdit_odd_change")
        self.horizontalLayout_11.addWidget(self.lineEdit_odd_change)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_8 = QtWidgets.QLabel(self.widget_buy_info)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_13.addWidget(self.label_8)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem5)
        self.label_buy_smname = QtWidgets.QLabel(self.widget_buy_info)
        self.label_buy_smname.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_buy_smname.setFont(font)
        self.label_buy_smname.setText("")
        self.label_buy_smname.setObjectName("label_buy_smname")
        self.horizontalLayout_13.addWidget(self.label_buy_smname)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem6)
        self.dateTimeEdit_buy = QtWidgets.QDateTimeEdit(self.widget_buy_info)
        self.dateTimeEdit_buy.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateTimeEdit_buy.setFont(font)
        self.dateTimeEdit_buy.setObjectName("dateTimeEdit_buy")
        self.horizontalLayout_13.addWidget(self.dateTimeEdit_buy)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.pushButton_buy_buy = QtWidgets.QPushButton(self.widget_buy_info)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_buy_buy.setFont(font)
        self.pushButton_buy_buy.setObjectName("pushButton_buy_buy")
        self.verticalLayout_3.addWidget(self.pushButton_buy_buy)
        self.gridLayout.addWidget(self.widget_buy_info, 0, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem7)
        self.pushButton_back = QtWidgets.QPushButton(self.widget_buy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")
        self.horizontalLayout_10.addWidget(self.pushButton_back)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.widget_buy_book_info = QtWidgets.QWidget(self.widget_buy)
        self.widget_buy_book_info.setEnabled(True)
        self.widget_buy_book_info.setMinimumSize(QtCore.QSize(200, 0))
        self.widget_buy_book_info.setObjectName("widget_buy_book_info")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_buy_book_info)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(20, 107, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem9)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.label_table_3_name = QtWidgets.QLabel(self.widget_buy_book_info)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_table_3_name.setFont(font)
        self.label_table_3_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_table_3_name.setObjectName("label_table_3_name")
        self.horizontalLayout_7.addWidget(self.label_table_3_name)
        self.pushButton_buy_book_info_hide = QtWidgets.QPushButton(self.widget_buy_book_info)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_buy_book_info_hide.setFont(font)
        self.pushButton_buy_book_info_hide.setObjectName("pushButton_buy_book_info_hide")
        self.horizontalLayout_7.addWidget(self.pushButton_buy_book_info_hide)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_19 = QtWidgets.QLabel(self.widget_buy_book_info)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_8.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.widget_buy_book_info)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_8.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.widget_buy_book_info)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_8.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.widget_buy_book_info)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_8.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.widget_buy_book_info)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_8.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.widget_buy_book_info)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_8.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.widget_buy_book_info)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_8.addWidget(self.label_25)
        self.horizontalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lineEdit_buy_bno = QtWidgets.QLineEdit(self.widget_buy_book_info)
        self.lineEdit_buy_bno.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_buy_bno.setFont(font)
        self.lineEdit_buy_bno.setText("")
        self.lineEdit_buy_bno.setObjectName("lineEdit_buy_bno")
        self.verticalLayout_9.addWidget(self.lineEdit_buy_bno)
        self.lineEdit_buy_bname = QtWidgets.QLineEdit(self.widget_buy_book_info)
        self.lineEdit_buy_bname.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_buy_bname.setFont(font)
        self.lineEdit_buy_bname.setObjectName("lineEdit_buy_bname")
        self.verticalLayout_9.addWidget(self.lineEdit_buy_bname)
        self.lineEdit_buy_bauthor = QtWidgets.QLineEdit(self.widget_buy_book_info)
        self.lineEdit_buy_bauthor.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_buy_bauthor.setFont(font)
        self.lineEdit_buy_bauthor.setObjectName("lineEdit_buy_bauthor")
        self.verticalLayout_9.addWidget(self.lineEdit_buy_bauthor)
        self.lineEdit_buy_bprice = QtWidgets.QLineEdit(self.widget_buy_book_info)
        self.lineEdit_buy_bprice.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_buy_bprice.setFont(font)
        self.lineEdit_buy_bprice.setObjectName("lineEdit_buy_bprice")
        self.verticalLayout_9.addWidget(self.lineEdit_buy_bprice)
        self.comboBox_buy_btype = QtWidgets.QComboBox(self.widget_buy_book_info)
        self.comboBox_buy_btype.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_buy_btype.setFont(font)
        self.comboBox_buy_btype.setObjectName("comboBox_buy_btype")
        self.comboBox_buy_btype.addItem("")
        self.comboBox_buy_btype.addItem("")
        self.comboBox_buy_btype.addItem("")
        self.comboBox_buy_btype.addItem("")
        self.comboBox_buy_btype.addItem("")
        self.comboBox_buy_btype.addItem("")
        self.comboBox_buy_btype.addItem("")
        self.comboBox_buy_btype.addItem("")
        self.comboBox_buy_btype.addItem("")
        self.comboBox_buy_btype.addItem("")
        self.comboBox_buy_btype.addItem("")
        self.verticalLayout_9.addWidget(self.comboBox_buy_btype)
        self.lineEdit_buy_publish = QtWidgets.QLineEdit(self.widget_buy_book_info)
        self.lineEdit_buy_publish.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_buy_publish.setFont(font)
        self.lineEdit_buy_publish.setObjectName("lineEdit_buy_publish")
        self.verticalLayout_9.addWidget(self.lineEdit_buy_publish)
        self.lineEdit_buy_bnum = QtWidgets.QLineEdit(self.widget_buy_book_info)
        self.lineEdit_buy_bnum.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_buy_bnum.setFont(font)
        self.lineEdit_buy_bnum.setObjectName("lineEdit_buy_bnum")
        self.verticalLayout_9.addWidget(self.lineEdit_buy_bnum)
        self.horizontalLayout_9.addLayout(self.verticalLayout_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        spacerItem12 = QtWidgets.QSpacerItem(20, 107, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem12)
        self.verticalLayout_4.addWidget(self.widget_buy_book_info)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 2, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 0, 3, 1, 1)
        self.gridLayout_2.addWidget(self.widget_buy, 0, 0, 1, 1)

        self.retranslateUi(Frame_Buy)
        QtCore.QMetaObject.connectSlotsByName(Frame_Buy)

    def retranslateUi(self, Frame_Buy):
        _translate = QtCore.QCoreApplication.translate
        Frame_Buy.setWindowTitle(_translate("Frame_Buy", "购买"))
        self.checkBox_buy_is_member.setText(_translate("Frame_Buy", "会员"))
        self.radioButton_buy_mtel.setText(_translate("Frame_Buy", "手机号"))
        self.radioButton_buy_mno.setText(_translate("Frame_Buy", "会员号"))
        self.label_2.setText(_translate("Frame_Buy", "会员名"))
        self.label_buy_show_mname.setText(_translate("Frame_Buy", "***"))
        self.label_3.setText(_translate("Frame_Buy", "等级"))
        self.label_buy_mi.setText(_translate("Frame_Buy", "1级"))
        self.tableWidget_buy_info.setSortingEnabled(True)
        item = self.tableWidget_buy_info.horizontalHeaderItem(0)
        item.setText(_translate("Frame_Buy", "书号"))
        item = self.tableWidget_buy_info.horizontalHeaderItem(1)
        item.setText(_translate("Frame_Buy", "单价"))
        item = self.tableWidget_buy_info.horizontalHeaderItem(2)
        item.setText(_translate("Frame_Buy", "数量"))
        __sortingEnabled = self.tableWidget_buy_info.isSortingEnabled()
        self.tableWidget_buy_info.setSortingEnabled(False)
        item = self.tableWidget_buy_info.item(0, 0)
        item.setText(_translate("Frame_Buy", "1012"))
        self.tableWidget_buy_info.setSortingEnabled(__sortingEnabled)
        self.label_5.setText(_translate("Frame_Buy", "折扣"))
        self.label_6.setText(_translate("Frame_Buy", "无"))
        self.label.setText(_translate("Frame_Buy", "总价/元："))
        self.label_4.setText(_translate("Frame_Buy", "支付金额"))
        self.label_7.setText(_translate("Frame_Buy", "找零"))
        self.label_8.setText(_translate("Frame_Buy", "销售人员"))
        self.pushButton_buy_buy.setText(_translate("Frame_Buy", "确认购买"))
        self.pushButton_back.setText(_translate("Frame_Buy", "返回"))
        self.label_table_3_name.setText(_translate("Frame_Buy", "书籍信息"))
        self.pushButton_buy_book_info_hide.setText(_translate("Frame_Buy", "隐藏"))
        self.label_19.setText(_translate("Frame_Buy", "书号"))
        self.label_20.setText(_translate("Frame_Buy", "书名"))
        self.label_21.setText(_translate("Frame_Buy", "作者"))
        self.label_22.setText(_translate("Frame_Buy", "原价/元"))
        self.label_23.setText(_translate("Frame_Buy", "分类"))
        self.label_24.setText(_translate("Frame_Buy", "出版社"))
        self.label_25.setText(_translate("Frame_Buy", "库存量/本"))
        self.comboBox_buy_btype.setCurrentText(_translate("Frame_Buy", "无"))
        self.comboBox_buy_btype.setItemText(0, _translate("Frame_Buy", "无"))
        self.comboBox_buy_btype.setItemText(1, _translate("Frame_Buy", "经典名著"))
        self.comboBox_buy_btype.setItemText(2, _translate("Frame_Buy", "专业图书类"))
        self.comboBox_buy_btype.setItemText(3, _translate("Frame_Buy", "古典文学"))
        self.comboBox_buy_btype.setItemText(4, _translate("Frame_Buy", "外国文学"))
        self.comboBox_buy_btype.setItemText(5, _translate("Frame_Buy", "现当代文学"))
        self.comboBox_buy_btype.setItemText(6, _translate("Frame_Buy", "历史地理类"))
        self.comboBox_buy_btype.setItemText(7, _translate("Frame_Buy", "哲学类"))
        self.comboBox_buy_btype.setItemText(8, _translate("Frame_Buy", "社会科学类"))
        self.comboBox_buy_btype.setItemText(9, _translate("Frame_Buy", "玄幻文学"))
        self.comboBox_buy_btype.setItemText(10, _translate("Frame_Buy", "儿童文学"))
        self.lineEdit_buy_bnum.setText(_translate("Frame_Buy", "0"))

