# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/leads_manager_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_leads_management_window(object):
    def setupUi(self, leads_management_window):
        leads_management_window.setObjectName("leads_management_window")
        leads_management_window.resize(1000, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(leads_management_window.sizePolicy().hasHeightForWidth())
        leads_management_window.setSizePolicy(sizePolicy)
        leads_management_window.setMinimumSize(QtCore.QSize(1000, 800))
        leads_management_window.setMaximumSize(QtCore.QSize(1000000, 1000000))
        leads_management_window.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(leads_management_window)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.name_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_line_edit.sizePolicy().hasHeightForWidth())
        self.name_line_edit.setSizePolicy(sizePolicy)
        self.name_line_edit.setMinimumSize(QtCore.QSize(394, 50))
        self.name_line_edit.setMaximumSize(QtCore.QSize(194, 50))
        self.name_line_edit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.name_line_edit.setStyleSheet("background-color:white;")
        self.name_line_edit.setObjectName("name_line_edit")
        self.horizontalLayout.addWidget(self.name_line_edit)
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_btn.sizePolicy().hasHeightForWidth())
        self.search_btn.setSizePolicy(sizePolicy)
        self.search_btn.setMinimumSize(QtCore.QSize(250, 50))
        self.search_btn.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.search_btn.setFont(font)
        self.search_btn.setAutoFillBackground(False)
        self.search_btn.setStyleSheet("")
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.email_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email_line_edit.sizePolicy().hasHeightForWidth())
        self.email_line_edit.setSizePolicy(sizePolicy)
        self.email_line_edit.setMinimumSize(QtCore.QSize(194, 50))
        self.email_line_edit.setMaximumSize(QtCore.QSize(194, 50))
        self.email_line_edit.setStyleSheet("background-color:white;")
        self.email_line_edit.setObjectName("email_line_edit")
        self.horizontalLayout_2.addWidget(self.email_line_edit)
        self.phone_number_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phone_number_line_edit.sizePolicy().hasHeightForWidth())
        self.phone_number_line_edit.setSizePolicy(sizePolicy)
        self.phone_number_line_edit.setMinimumSize(QtCore.QSize(194, 50))
        self.phone_number_line_edit.setMaximumSize(QtCore.QSize(194, 50))
        self.phone_number_line_edit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.phone_number_line_edit.setStyleSheet("background-color:white;")
        self.phone_number_line_edit.setObjectName("phone_number_line_edit")
        self.horizontalLayout_2.addWidget(self.phone_number_line_edit)
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_btn.sizePolicy().hasHeightForWidth())
        self.add_btn.setSizePolicy(sizePolicy)
        self.add_btn.setMinimumSize(QtCore.QSize(250, 50))
        self.add_btn.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.add_btn.setFont(font)
        self.add_btn.setStyleSheet("")
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout_2.addWidget(self.add_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.table_view = QtWidgets.QTableView(self.centralwidget)
        self.table_view.setObjectName("table_view")
        self.table_view.horizontalHeader().setCascadingSectionResizes(True)
        self.verticalLayout.addWidget(self.table_view)
        leads_management_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(leads_management_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 20))
        self.menubar.setObjectName("menubar")
        leads_management_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(leads_management_window)
        self.statusbar.setObjectName("statusbar")
        leads_management_window.setStatusBar(self.statusbar)

        self.retranslateUi(leads_management_window)
        QtCore.QMetaObject.connectSlotsByName(leads_management_window)

    def retranslateUi(self, leads_management_window):
        _translate = QtCore.QCoreApplication.translate
        leads_management_window.setWindowTitle(_translate("leads_management_window", "Leads management"))
        self.name_line_edit.setPlaceholderText(_translate("leads_management_window", "Name"))
        self.search_btn.setText(_translate("leads_management_window", "Search"))
        self.email_line_edit.setPlaceholderText(_translate("leads_management_window", "Email"))
        self.phone_number_line_edit.setPlaceholderText(_translate("leads_management_window", "Phone number"))
        self.add_btn.setText(_translate("leads_management_window", "Add new lead"))
