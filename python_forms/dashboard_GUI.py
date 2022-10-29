# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/dashboard_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dashboard_widget(object):
    def setupUi(self, dashboard_widget):
        dashboard_widget.setObjectName("dashboard_widget")
        dashboard_widget.resize(496, 227)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(dashboard_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(dashboard_widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self._2 = QtWidgets.QHBoxLayout()
        self._2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self._2.setSpacing(36)
        self._2.setObjectName("_2")
        self.invoices_number_icon = QtWidgets.QLabel(dashboard_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.invoices_number_icon.sizePolicy().hasHeightForWidth())
        self.invoices_number_icon.setSizePolicy(sizePolicy)
        self.invoices_number_icon.setMinimumSize(QtCore.QSize(88, 88))
        self.invoices_number_icon.setMaximumSize(QtCore.QSize(100, 100))
        self.invoices_number_icon.setText("")
        self.invoices_number_icon.setPixmap(QtGui.QPixmap(":/icons/Icons/analysis.png"))
        self.invoices_number_icon.setScaledContents(True)
        self.invoices_number_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.invoices_number_icon.setWordWrap(True)
        self.invoices_number_icon.setObjectName("invoices_number_icon")
        self._2.addWidget(self.invoices_number_icon)
        self.invoices_this_month_label = QtWidgets.QLabel(dashboard_widget)
        font = QtGui.QFont()
        font.setPointSize(70)
        self.invoices_this_month_label.setFont(font)
        self.invoices_this_month_label.setScaledContents(True)
        self.invoices_this_month_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.invoices_this_month_label.setWordWrap(True)
        self.invoices_this_month_label.setObjectName("invoices_this_month_label")
        self._2.addWidget(self.invoices_this_month_label)
        self.verticalLayout.addLayout(self._2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(dashboard_widget)
        QtCore.QMetaObject.connectSlotsByName(dashboard_widget)

    def retranslateUi(self, dashboard_widget):
        _translate = QtCore.QCoreApplication.translate
        dashboard_widget.setWindowTitle(_translate("dashboard_widget", "Dashboard"))
        self.label.setText(_translate("dashboard_widget", "Number of invoices this month:"))
        self.invoices_this_month_label.setText(_translate("dashboard_widget", "0"))
import resources_rc