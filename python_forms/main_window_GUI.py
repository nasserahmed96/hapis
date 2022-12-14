# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/main_window_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 900))
        MainWindow.setMaximumSize(QtCore.QSize(10000, 10000))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(" QWidget#SideBar\n"
" {\n"
"            background-color: white;\n"
"            margin: 0\n"
" }\n"
"QPushButton{\n"
"  background-color: #838383;\n"
"  border: none;\n"
"  color: black;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #585858;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(54, 54, 54);\n"
"}\n"
"\n"
"QHeaderView{\n"
"background-color: #838383;\n"
"  border: none;\n"
"  color: black;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"\n"
"")
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SideBar = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.SideBar.sizePolicy().hasHeightForWidth())
        self.SideBar.setSizePolicy(sizePolicy)
        self.SideBar.setMinimumSize(QtCore.QSize(200, 0))
        self.SideBar.setMaximumSize(QtCore.QSize(250, 16777215))
        self.SideBar.setStyleSheet("  QPushButton\n"
"            { \n"
"                background-color: #FFFFFF;\n"
"                color: rgb(190, 190, 190);\n"
"                border: none;\n"
"                color: white;\n"
"                text-align: left;\n"
"                text-decoration: none;\n"
"                color: black;\n"
"                padding: 1px;\n"
"            }\n"
"            QPushButton:hover{\n"
"                background-color: grey;\n"
"            }\n"
"            QPushButton:hover:pressed{\n"
"                background-color: #bebebe;\n"
"            }")
        self.SideBar.setObjectName("SideBar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.SideBar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.invoices_btn = QtWidgets.QPushButton(self.SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(218)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.invoices_btn.sizePolicy().hasHeightForWidth())
        self.invoices_btn.setSizePolicy(sizePolicy)
        self.invoices_btn.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
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
        self.offers_btn = QtWidgets.QPushButton(self.SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.offers_btn.sizePolicy().hasHeightForWidth())
        self.offers_btn.setSizePolicy(sizePolicy)
        self.offers_btn.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.offers_btn.setFont(font)
        self.offers_btn.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/Icons/business-proposal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.offers_btn.setIcon(icon1)
        self.offers_btn.setIconSize(QtCore.QSize(24, 24))
        self.offers_btn.setObjectName("offers_btn")
        self.verticalLayout.addWidget(self.offers_btn)
        self.brokers_btn = QtWidgets.QPushButton(self.SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brokers_btn.sizePolicy().hasHeightForWidth())
        self.brokers_btn.setSizePolicy(sizePolicy)
        self.brokers_btn.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.brokers_btn.setFont(font)
        self.brokers_btn.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/Icons/PngItem_3256236.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.brokers_btn.setIcon(icon2)
        self.brokers_btn.setIconSize(QtCore.QSize(24, 24))
        self.brokers_btn.setObjectName("brokers_btn")
        self.verticalLayout.addWidget(self.brokers_btn)
        self.leads_btn = QtWidgets.QPushButton(self.SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leads_btn.sizePolicy().hasHeightForWidth())
        self.leads_btn.setSizePolicy(sizePolicy)
        self.leads_btn.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.leads_btn.setFont(font)
        self.leads_btn.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/Icons/brands_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.leads_btn.setIcon(icon3)
        self.leads_btn.setIconSize(QtCore.QSize(24, 24))
        self.leads_btn.setObjectName("leads_btn")
        self.verticalLayout.addWidget(self.leads_btn)
        self.companies_btn = QtWidgets.QPushButton(self.SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.companies_btn.sizePolicy().hasHeightForWidth())
        self.companies_btn.setSizePolicy(sizePolicy)
        self.companies_btn.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.companies_btn.setFont(font)
        self.companies_btn.setAutoFillBackground(False)
        self.companies_btn.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/Icons/product-icon-17.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.companies_btn.setIcon(icon4)
        self.companies_btn.setIconSize(QtCore.QSize(24, 24))
        self.companies_btn.setObjectName("companies_btn")
        self.verticalLayout.addWidget(self.companies_btn)
        self.calender_btn = QtWidgets.QPushButton(self.SideBar)
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
        font.setWeight(75)
        font.setStrikeOut(False)
        self.calender_btn.setFont(font)
        self.calender_btn.setStyleSheet("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/Icons/pngegg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calender_btn.setIcon(icon5)
        self.calender_btn.setIconSize(QtCore.QSize(24, 24))
        self.calender_btn.setObjectName("calender_btn")
        self.verticalLayout.addWidget(self.calender_btn)
        self.clients_btn = QtWidgets.QPushButton(self.SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clients_btn.sizePolicy().hasHeightForWidth())
        self.clients_btn.setSizePolicy(sizePolicy)
        self.clients_btn.setMinimumSize(QtCore.QSize(200, 40))
        self.clients_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.clients_btn.setFont(font)
        self.clients_btn.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/Icons/people-ge35158f96_640.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clients_btn.setIcon(icon6)
        self.clients_btn.setIconSize(QtCore.QSize(24, 24))
        self.clients_btn.setObjectName("clients_btn")
        self.verticalLayout.addWidget(self.clients_btn)
        self.employees_btn = QtWidgets.QPushButton(self.SideBar)
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
        font.setWeight(75)
        font.setStrikeOut(False)
        self.employees_btn.setFont(font)
        self.employees_btn.setStyleSheet("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/Icons/group+people+management+business+work+employees-1320567856204506545_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.employees_btn.setIcon(icon7)
        self.employees_btn.setIconSize(QtCore.QSize(24, 24))
        self.employees_btn.setObjectName("employees_btn")
        self.verticalLayout.addWidget(self.employees_btn)
        self.system_properties_btn = QtWidgets.QPushButton(self.SideBar)
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
        font.setWeight(75)
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
        self.dashboard_btn = QtWidgets.QPushButton(self.SideBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dashboard_btn.sizePolicy().hasHeightForWidth())
        self.dashboard_btn.setSizePolicy(sizePolicy)
        self.dashboard_btn.setMinimumSize(QtCore.QSize(200, 40))
        self.dashboard_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.dashboard_btn.setFont(font)
        self.dashboard_btn.setAutoFillBackground(False)
        self.dashboard_btn.setStyleSheet("")
        self.dashboard_btn.setIcon(icon8)
        self.dashboard_btn.setIconSize(QtCore.QSize(24, 24))
        self.dashboard_btn.setFlat(False)
        self.dashboard_btn.setObjectName("dashboard_btn")
        self.verticalLayout.addWidget(self.dashboard_btn)
        self.horizontalLayout.addWidget(self.SideBar)
        self.window_content = QtWidgets.QStackedWidget(self.centralwidget)
        self.window_content.setFrameShape(QtWidgets.QFrame.Box)
        self.window_content.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.window_content.setObjectName("window_content")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.window_content.addWidget(self.page)
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.window_content.addWidget(self.widget)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.window_content.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.window_content)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuProfile = QtWidgets.QMenu(self.menubar)
        self.menuProfile.setObjectName("menuProfile")
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionView_profile = QtWidgets.QAction(MainWindow)
        self.actionView_profile.setObjectName("actionView_profile")
        self.actionSignout = QtWidgets.QAction(MainWindow)
        self.actionSignout.setObjectName("actionSignout")
        self.menuFile.addAction(self.actionExit)
        self.menuProfile.addAction(self.actionView_profile)
        self.menuProfile.addAction(self.actionSignout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuProfile.menuAction())

        self.retranslateUi(MainWindow)
        self.window_content.setCurrentIndex(0)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.invoices_btn.setToolTip(_translate("MainWindow", "Create new or search in invoices"))
        self.invoices_btn.setText(_translate("MainWindow", "Invoices"))
        self.offers_btn.setToolTip(_translate("MainWindow", "Create new offer, or search old ones"))
        self.offers_btn.setText(_translate("MainWindow", "Proposals"))
        self.brokers_btn.setToolTip(_translate("MainWindow", "Manage products, and get reports about the,"))
        self.brokers_btn.setText(_translate("MainWindow", "Brokers"))
        self.leads_btn.setToolTip(_translate("MainWindow", "Manage products, and get reports about the,"))
        self.leads_btn.setText(_translate("MainWindow", "Leads"))
        self.companies_btn.setToolTip(_translate("MainWindow", "Manage categories"))
        self.companies_btn.setText(_translate("MainWindow", "Companies"))
        self.calender_btn.setToolTip(_translate("MainWindow", "Check calnder for appointment"))
        self.calender_btn.setText(_translate("MainWindow", "Calender"))
        self.clients_btn.setToolTip(_translate("MainWindow", "Manage cusutomers and get reports about them"))
        self.clients_btn.setText(_translate("MainWindow", "Clients"))
        self.employees_btn.setToolTip(_translate("MainWindow", "Create, View, edit or delete employees"))
        self.employees_btn.setText(_translate("MainWindow", "Employees"))
        self.system_properties_btn.setToolTip(_translate("MainWindow", "Go to job titles, status, and other system related functions"))
        self.system_properties_btn.setText(_translate("MainWindow", "System properties"))
        self.dashboard_btn.setToolTip(_translate("MainWindow", "Go to job titles, status, and other system related functions"))
        self.dashboard_btn.setText(_translate("MainWindow", "Dashboard"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuProfile.setTitle(_translate("MainWindow", "Profile"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionView_profile.setText(_translate("MainWindow", "View profile"))
        self.actionSignout.setText(_translate("MainWindow", "Signout"))
import resources_rc
