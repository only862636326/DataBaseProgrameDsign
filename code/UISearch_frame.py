# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTuiFrame_search.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame_search(object):
    def setupUi(self, Frame_search):
        Frame_search.setObjectName("Frame_search")
        Frame_search.resize(738, 496)
        font = QtGui.QFont()
        font.setPointSize(10)
        Frame_search.setFont(font)
        self.gridLayout_2 = QtWidgets.QGridLayout(Frame_search)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(33, 88, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.widget = QtWidgets.QWidget(Frame_search)
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_find = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.pushButton_find.setFont(font)
        self.pushButton_find.setObjectName("pushButton_find")
        self.gridLayout.addWidget(self.pushButton_find, 3, 0, 1, 1)
        self.pushButton_clear = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout.addWidget(self.pushButton_clear, 4, 0, 1, 1)
        self.lineEdit_search_data = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.lineEdit_search_data.setFont(font)
        self.lineEdit_search_data.setText("")
        self.lineEdit_search_data.setObjectName("lineEdit_search_data")
        self.gridLayout.addWidget(self.lineEdit_search_data, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_bno = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.radioButton_bno.setFont(font)
        self.radioButton_bno.setChecked(False)
        self.radioButton_bno.setObjectName("radioButton_bno")
        self.verticalLayout.addWidget(self.radioButton_bno)
        self.radioButton_bname = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.radioButton_bname.setFont(font)
        self.radioButton_bname.setChecked(True)
        self.radioButton_bname.setObjectName("radioButton_bname")
        self.verticalLayout.addWidget(self.radioButton_bname)
        self.radioButton_bauthor = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.radioButton_bauthor.setFont(font)
        self.radioButton_bauthor.setObjectName("radioButton_bauthor")
        self.verticalLayout.addWidget(self.radioButton_bauthor)
        self.radioButton_pubulish = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.radioButton_pubulish.setFont(font)
        self.radioButton_pubulish.setObjectName("radioButton_pubulish")
        self.verticalLayout.addWidget(self.radioButton_pubulish)
        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 6, 1)
        self.comboBox_btype = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_btype.setFont(font)
        self.comboBox_btype.setObjectName("comboBox_btype")
        self.comboBox_btype.addItem("")
        self.comboBox_btype.addItem("")
        self.comboBox_btype.addItem("")
        self.comboBox_btype.addItem("")
        self.comboBox_btype.addItem("")
        self.comboBox_btype.addItem("")
        self.comboBox_btype.addItem("")
        self.comboBox_btype.addItem("")
        self.comboBox_btype.addItem("")
        self.comboBox_btype.addItem("")
        self.comboBox_btype.addItem("")
        self.gridLayout.addWidget(self.comboBox_btype, 3, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_day = QtWidgets.QPushButton(Frame_search)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(17)
        self.pushButton_day.setFont(font)
        self.pushButton_day.setObjectName("pushButton_day")
        self.verticalLayout_2.addWidget(self.pushButton_day)
        self.pushButton_weak = QtWidgets.QPushButton(Frame_search)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(17)
        self.pushButton_weak.setFont(font)
        self.pushButton_weak.setObjectName("pushButton_weak")
        self.verticalLayout_2.addWidget(self.pushButton_weak)
        self.pushButton_month = QtWidgets.QPushButton(Frame_search)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(17)
        self.pushButton_month.setFont(font)
        self.pushButton_month.setObjectName("pushButton_month")
        self.verticalLayout_2.addWidget(self.pushButton_month)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.label = QtWidgets.QLabel(Frame_search)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_back = QtWidgets.QPushButton(Frame_search)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")
        self.verticalLayout_3.addWidget(self.pushButton_back)
        self.pushButton_show_all = QtWidgets.QPushButton(Frame_search)
        self.pushButton_show_all.setObjectName("pushButton_show_all")
        self.verticalLayout_3.addWidget(self.pushButton_show_all)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Frame_search)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.tableWidget.setFont(font)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 1)

        self.retranslateUi(Frame_search)
        QtCore.QMetaObject.connectSlotsByName(Frame_search)
        Frame_search.setTabOrder(self.lineEdit_search_data, self.pushButton_find)
        Frame_search.setTabOrder(self.pushButton_find, self.pushButton_clear)
        Frame_search.setTabOrder(self.pushButton_clear, self.pushButton_day)
        Frame_search.setTabOrder(self.pushButton_day, self.pushButton_weak)
        Frame_search.setTabOrder(self.pushButton_weak, self.pushButton_month)
        Frame_search.setTabOrder(self.pushButton_month, self.tableWidget)
        Frame_search.setTabOrder(self.tableWidget, self.radioButton_bno)
        Frame_search.setTabOrder(self.radioButton_bno, self.radioButton_pubulish)
        Frame_search.setTabOrder(self.radioButton_pubulish, self.radioButton_bname)
        Frame_search.setTabOrder(self.radioButton_bname, self.radioButton_bauthor)

    def retranslateUi(self, Frame_search):
        _translate = QtCore.QCoreApplication.translate
        Frame_search.setWindowTitle(_translate("Frame_search", "     搜索"))
        self.pushButton_find.setText(_translate("Frame_search", "查询"))
        self.pushButton_clear.setText(_translate("Frame_search", "清空"))
        self.label_2.setText(_translate("Frame_search", "类别"))
        self.radioButton_bno.setText(_translate("Frame_search", "搜书号"))
        self.radioButton_bname.setText(_translate("Frame_search", "搜书名"))
        self.radioButton_bauthor.setText(_translate("Frame_search", "搜作者"))
        self.radioButton_pubulish.setText(_translate("Frame_search", "搜出版社"))
        self.comboBox_btype.setItemText(0, _translate("Frame_search", "无"))
        self.comboBox_btype.setItemText(1, _translate("Frame_search", "经典名著"))
        self.comboBox_btype.setItemText(2, _translate("Frame_search", "专业图书类"))
        self.comboBox_btype.setItemText(3, _translate("Frame_search", "古典文学"))
        self.comboBox_btype.setItemText(4, _translate("Frame_search", "外国文学"))
        self.comboBox_btype.setItemText(5, _translate("Frame_search", "现当代文学"))
        self.comboBox_btype.setItemText(6, _translate("Frame_search", "历史地理类"))
        self.comboBox_btype.setItemText(7, _translate("Frame_search", "哲学类"))
        self.comboBox_btype.setItemText(8, _translate("Frame_search", "社会科学类"))
        self.comboBox_btype.setItemText(9, _translate("Frame_search", "玄幻文学"))
        self.comboBox_btype.setItemText(10, _translate("Frame_search", "儿童文学"))
        self.pushButton_day.setText(_translate("Frame_search", "日榜"))
        self.pushButton_weak.setText(_translate("Frame_search", "周榜"))
        self.pushButton_month.setText(_translate("Frame_search", "月榜"))
        self.label.setText(_translate("Frame_search", "畅销榜\n"
"查看"))
        self.pushButton_back.setText(_translate("Frame_search", "返回"))
        self.pushButton_show_all.setText(_translate("Frame_search", "显示所有"))

