# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/invoice_manager_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_invoicesManagerWindow(object):
    def setupUi(self, invoicesManagerWindow):
        invoicesManagerWindow.setObjectName("invoicesManagerWindow")
        invoicesManagerWindow.resize(1291, 674)
        self.centralwidget = QtWidgets.QWidget(invoicesManagerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_date_chbox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_date_chbox.setFont(font)
        self.search_date_chbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.search_date_chbox.setTristate(False)
        self.search_date_chbox.setObjectName("search_date_chbox")
        self.horizontalLayout.addWidget(self.search_date_chbox)
        self.form_date_edit = QtWidgets.QLabel(self.centralwidget)
        self.form_date_edit.setMaximumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.form_date_edit.setFont(font)
        self.form_date_edit.setObjectName("form_date_edit")
        self.horizontalLayout.addWidget(self.form_date_edit)
        self.from_date_edit = QtWidgets.QDateEdit(self.centralwidget)
        self.from_date_edit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.from_date_edit.sizePolicy().hasHeightForWidth())
        self.from_date_edit.setSizePolicy(sizePolicy)
        self.from_date_edit.setMinimumSize(QtCore.QSize(160, 50))
        self.from_date_edit.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.from_date_edit.setFont(font)
        self.from_date_edit.setCalendarPopup(True)
        self.from_date_edit.setObjectName("from_date_edit")
        self.horizontalLayout.addWidget(self.from_date_edit)
        self.to_label = QtWidgets.QLabel(self.centralwidget)
        self.to_label.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.to_label.setFont(font)
        self.to_label.setObjectName("to_label")
        self.horizontalLayout.addWidget(self.to_label)
        self.to_date_edit = QtWidgets.QDateEdit(self.centralwidget)
        self.to_date_edit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to_date_edit.sizePolicy().hasHeightForWidth())
        self.to_date_edit.setSizePolicy(sizePolicy)
        self.to_date_edit.setMinimumSize(QtCore.QSize(160, 50))
        self.to_date_edit.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.to_date_edit.setFont(font)
        self.to_date_edit.setCalendarPopup(True)
        self.to_date_edit.setObjectName("to_date_edit")
        self.horizontalLayout.addWidget(self.to_date_edit)
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_btn.sizePolicy().hasHeightForWidth())
        self.search_btn.setSizePolicy(sizePolicy)
        self.search_btn.setMinimumSize(QtCore.QSize(230, 50))
        self.search_btn.setMaximumSize(QtCore.QSize(230, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.search_btn.setFont(font)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(31)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.companies_label = QtWidgets.QLabel(self.centralwidget)
        self.companies_label.setMaximumSize(QtCore.QSize(555555, 5555555))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.companies_label.setFont(font)
        self.companies_label.setObjectName("companies_label")
        self.horizontalLayout_2.addWidget(self.companies_label)
        self.companies_cb = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.companies_cb.setFont(font)
        self.companies_cb.setObjectName("companies_cb")
        self.companies_cb.addItem("")
        self.companies_cb.addItem("")
        self.companies_cb.addItem("")
        self.horizontalLayout_2.addWidget(self.companies_cb)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.add_new_invoice_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_new_invoice_btn.sizePolicy().hasHeightForWidth())
        self.add_new_invoice_btn.setSizePolicy(sizePolicy)
        self.add_new_invoice_btn.setMinimumSize(QtCore.QSize(230, 50))
        self.add_new_invoice_btn.setMaximumSize(QtCore.QSize(230, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.add_new_invoice_btn.setFont(font)
        self.add_new_invoice_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.add_new_invoice_btn.setObjectName("add_new_invoice_btn")
        self.horizontalLayout_3.addWidget(self.add_new_invoice_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.invoices_table_view = QtWidgets.QTableView(self.centralwidget)
        self.invoices_table_view.setObjectName("invoices_table_view")
        self.invoices_table_view.horizontalHeader().setDefaultSectionSize(120)
        self.invoices_table_view.horizontalHeader().setMinimumSectionSize(80)
        self.invoices_table_view.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.invoices_table_view)
        invoicesManagerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(invoicesManagerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1291, 20))
        self.menubar.setObjectName("menubar")
        invoicesManagerWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(invoicesManagerWindow)
        self.statusbar.setObjectName("statusbar")
        invoicesManagerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(invoicesManagerWindow)
        QtCore.QMetaObject.connectSlotsByName(invoicesManagerWindow)

    def retranslateUi(self, invoicesManagerWindow):
        _translate = QtCore.QCoreApplication.translate
        invoicesManagerWindow.setWindowTitle(_translate("invoicesManagerWindow", "Invoices manager"))
        self.search_date_chbox.setText(_translate("invoicesManagerWindow", "Enable date"))
        self.form_date_edit.setText(_translate("invoicesManagerWindow", "From date:"))
        self.from_date_edit.setDisplayFormat(_translate("invoicesManagerWindow", "yyyy-MM-dd"))
        self.to_label.setText(_translate("invoicesManagerWindow", "To:"))
        self.to_date_edit.setDisplayFormat(_translate("invoicesManagerWindow", "yyyy-MM-dd"))
        self.search_btn.setText(_translate("invoicesManagerWindow", "Search"))
        self.companies_label.setText(_translate("invoicesManagerWindow", "Select company:"))
        self.companies_cb.setItemText(0, _translate("invoicesManagerWindow", "GIG"))
        self.companies_cb.setItemText(1, _translate("invoicesManagerWindow", "Sarwa"))
        self.companies_cb.setItemText(2, _translate("invoicesManagerWindow", "Watanya"))
        self.add_new_invoice_btn.setText(_translate("invoicesManagerWindow", "Add new invoice"))