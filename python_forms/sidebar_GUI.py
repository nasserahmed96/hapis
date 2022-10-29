# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/sidebar_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SideBar(object):
    def setupUi(self, SideBar):
        SideBar.setObjectName("SideBar")
        SideBar.resize(218, 718)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SideBar.sizePolicy().hasHeightForWidth())
        SideBar.setSizePolicy(sizePolicy)
        SideBar.setSizeIncrement(QtCore.QSize(1, 0))
        SideBar.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(SideBar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.invoices_btn = QtWidgets.QPushButton(SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(218)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.invoices_btn.sizePolicy().hasHeightForWidth())
        self.invoices_btn.setSizePolicy(sizePolicy)
        self.invoices_btn.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.invoices_btn.setFont(font)
        self.invoices_btn.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Icons/analysis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.invoices_btn.setIcon(icon)
        self.invoices_btn.setIconSize(QtCore.QSize(24, 24))
        self.invoices_btn.setObjectName("invoices_btn")
        self.verticalLayout.addWidget(self.invoices_btn)
        self.offers_btn = QtWidgets.QPushButton(SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.offers_btn.sizePolicy().hasHeightForWidth())
        self.offers_btn.setSizePolicy(sizePolicy)
        self.offers_btn.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.offers_btn.setFont(font)
        self.offers_btn.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/Icons/business-proposal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.offers_btn.setIcon(icon1)
        self.offers_btn.setIconSize(QtCore.QSize(24, 24))
        self.offers_btn.setObjectName("offers_btn")
        self.verticalLayout.addWidget(self.offers_btn)
        self.products_btn = QtWidgets.QPushButton(SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.products_btn.sizePolicy().hasHeightForWidth())
        self.products_btn.setSizePolicy(sizePolicy)
        self.products_btn.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.products_btn.setFont(font)
        self.products_btn.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/Icons/PngItem_3256236.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.products_btn.setIcon(icon2)
        self.products_btn.setIconSize(QtCore.QSize(24, 24))
        self.products_btn.setObjectName("products_btn")
        self.verticalLayout.addWidget(self.products_btn)
        self.brands_btn = QtWidgets.QPushButton(SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brands_btn.sizePolicy().hasHeightForWidth())
        self.brands_btn.setSizePolicy(sizePolicy)
        self.brands_btn.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.brands_btn.setFont(font)
        self.brands_btn.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/Icons/brands_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.brands_btn.setIcon(icon3)
        self.brands_btn.setIconSize(QtCore.QSize(24, 24))
        self.brands_btn.setObjectName("brands_btn")
        self.verticalLayout.addWidget(self.brands_btn)
        self.categories_btn = QtWidgets.QPushButton(SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categories_btn.sizePolicy().hasHeightForWidth())
        self.categories_btn.setSizePolicy(sizePolicy)
        self.categories_btn.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.categories_btn.setFont(font)
        self.categories_btn.setAutoFillBackground(False)
        self.categories_btn.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/Icons/product-icon-17.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.categories_btn.setIcon(icon4)
        self.categories_btn.setIconSize(QtCore.QSize(24, 24))
        self.categories_btn.setObjectName("categories_btn")
        self.verticalLayout.addWidget(self.categories_btn)
        self.calender_btn = QtWidgets.QPushButton(SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calender_btn.sizePolicy().hasHeightForWidth())
        self.calender_btn.setSizePolicy(sizePolicy)
        self.calender_btn.setMinimumSize(QtCore.QSize(200, 40))
        self.calender_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.calender_btn.setFont(font)
        self.calender_btn.setStyleSheet("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/Icons/pngegg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calender_btn.setIcon(icon5)
        self.calender_btn.setIconSize(QtCore.QSize(24, 24))
        self.calender_btn.setObjectName("calender_btn")
        self.verticalLayout.addWidget(self.calender_btn)
        self.customers_btn = QtWidgets.QPushButton(SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customers_btn.sizePolicy().hasHeightForWidth())
        self.customers_btn.setSizePolicy(sizePolicy)
        self.customers_btn.setMinimumSize(QtCore.QSize(200, 40))
        self.customers_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.customers_btn.setFont(font)
        self.customers_btn.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/Icons/people-ge35158f96_640.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.customers_btn.setIcon(icon6)
        self.customers_btn.setIconSize(QtCore.QSize(24, 24))
        self.customers_btn.setObjectName("customers_btn")
        self.verticalLayout.addWidget(self.customers_btn)
        self.employees_btn = QtWidgets.QPushButton(SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.employees_btn.sizePolicy().hasHeightForWidth())
        self.employees_btn.setSizePolicy(sizePolicy)
        self.employees_btn.setMinimumSize(QtCore.QSize(200, 40))
        self.employees_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.employees_btn.setFont(font)
        self.employees_btn.setStyleSheet("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/Icons/group+people+management+business+work+employees-1320567856204506545_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.employees_btn.setIcon(icon7)
        self.employees_btn.setIconSize(QtCore.QSize(24, 24))
        self.employees_btn.setObjectName("employees_btn")
        self.verticalLayout.addWidget(self.employees_btn)
        self.system_properties_btn = QtWidgets.QPushButton(SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.system_properties_btn.sizePolicy().hasHeightForWidth())
        self.system_properties_btn.setSizePolicy(sizePolicy)
        self.system_properties_btn.setMinimumSize(QtCore.QSize(200, 40))
        self.system_properties_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.system_properties_btn.setFont(font)
        self.system_properties_btn.setAutoFillBackground(False)
        self.system_properties_btn.setStyleSheet("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/Icons/gear_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.system_properties_btn.setIcon(icon8)
        self.system_properties_btn.setIconSize(QtCore.QSize(24, 24))
        self.system_properties_btn.setFlat(False)
        self.system_properties_btn.setObjectName("system_properties_btn")
        self.verticalLayout.addWidget(self.system_properties_btn)

        self.retranslateUi(SideBar)
        QtCore.QMetaObject.connectSlotsByName(SideBar)

    def retranslateUi(self, SideBar):
        _translate = QtCore.QCoreApplication.translate
        SideBar.setWindowTitle(_translate("SideBar", "SideBar"))
        self.invoices_btn.setToolTip(_translate("SideBar", "Create new or search in invoices"))
        self.invoices_btn.setText(_translate("SideBar", "Invoices"))
        self.offers_btn.setToolTip(_translate("SideBar", "Create new offer, or search old ones"))
        self.offers_btn.setText(_translate("SideBar", "Proposals"))
        self.products_btn.setToolTip(_translate("SideBar", "Manage products, and get reports about the,"))
        self.products_btn.setText(_translate("SideBar", "Products"))
        self.brands_btn.setToolTip(_translate("SideBar", "Manage products, and get reports about the,"))
        self.brands_btn.setText(_translate("SideBar", "Brands"))
        self.categories_btn.setToolTip(_translate("SideBar", "Manage categories"))
        self.categories_btn.setText(_translate("SideBar", "Categories"))
        self.calender_btn.setToolTip(_translate("SideBar", "Check calnder for appointment"))
        self.calender_btn.setText(_translate("SideBar", "Calender"))
        self.customers_btn.setToolTip(_translate("SideBar", "Manage cusutomers and get reports about them"))
        self.customers_btn.setText(_translate("SideBar", "Clients"))
        self.employees_btn.setToolTip(_translate("SideBar", "Create, View, edit or delete employees"))
        self.employees_btn.setText(_translate("SideBar", "Employees"))
        self.system_properties_btn.setToolTip(_translate("SideBar", "Go to job titles, status, and other system related functions"))
        self.system_properties_btn.setText(_translate("SideBar", "System properties"))
import resources_rc
