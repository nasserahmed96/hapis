# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/commissionStructure_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1028, 485)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.creditLayout = QtWidgets.QHBoxLayout()
        self.creditLayout.setSpacing(6)
        self.creditLayout.setObjectName("creditLayout")
        self.creditLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.creditLabel.sizePolicy().hasHeightForWidth())
        self.creditLabel.setSizePolicy(sizePolicy)
        self.creditLabel.setMinimumSize(QtCore.QSize(172, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.creditLabel.setFont(font)
        self.creditLabel.setObjectName("creditLabel")
        self.creditLayout.addWidget(self.creditLabel)
        self.creditLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.creditLineEdit.sizePolicy().hasHeightForWidth())
        self.creditLineEdit.setSizePolicy(sizePolicy)
        self.creditLineEdit.setMinimumSize(QtCore.QSize(320, 71))
        self.creditLineEdit.setObjectName("creditLineEdit")
        self.creditLayout.addWidget(self.creditLineEdit)
        self.horizontalLayout.addLayout(self.creditLayout)
        self.commercialLayout = QtWidgets.QHBoxLayout()
        self.commercialLayout.setSpacing(6)
        self.commercialLayout.setObjectName("commercialLayout")
        self.commercialLabel = QtWidgets.QLabel(self.centralwidget)
        self.commercialLabel.setMinimumSize(QtCore.QSize(172, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.commercialLabel.setFont(font)
        self.commercialLabel.setObjectName("commercialLabel")
        self.commercialLayout.addWidget(self.commercialLabel)
        self.commercialLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commercialLineEdit.sizePolicy().hasHeightForWidth())
        self.commercialLineEdit.setSizePolicy(sizePolicy)
        self.commercialLineEdit.setMinimumSize(QtCore.QSize(320, 71))
        self.commercialLineEdit.setObjectName("commercialLineEdit")
        self.commercialLayout.addWidget(self.commercialLineEdit)
        self.horizontalLayout.addLayout(self.commercialLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fireBurflaryLayout = QtWidgets.QHBoxLayout()
        self.fireBurflaryLayout.setObjectName("fireBurflaryLayout")
        self.fireBurglaryLabel = QtWidgets.QLabel(self.centralwidget)
        self.fireBurglaryLabel.setMinimumSize(QtCore.QSize(172, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.fireBurglaryLabel.setFont(font)
        self.fireBurglaryLabel.setObjectName("fireBurglaryLabel")
        self.fireBurflaryLayout.addWidget(self.fireBurglaryLabel)
        self.fireBurglaryLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fireBurglaryLineEdit.sizePolicy().hasHeightForWidth())
        self.fireBurglaryLineEdit.setSizePolicy(sizePolicy)
        self.fireBurglaryLineEdit.setMinimumSize(QtCore.QSize(320, 71))
        self.fireBurglaryLineEdit.setObjectName("fireBurglaryLineEdit")
        self.fireBurflaryLayout.addWidget(self.fireBurglaryLineEdit)
        self.horizontalLayout_2.addLayout(self.fireBurflaryLayout)
        self.gigStandardLayout = QtWidgets.QHBoxLayout()
        self.gigStandardLayout.setObjectName("gigStandardLayout")
        self.gigStandardLabel = QtWidgets.QLabel(self.centralwidget)
        self.gigStandardLabel.setMinimumSize(QtCore.QSize(172, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.gigStandardLabel.setFont(font)
        self.gigStandardLabel.setObjectName("gigStandardLabel")
        self.gigStandardLayout.addWidget(self.gigStandardLabel)
        self.gigStandardLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gigStandardLineEdit.sizePolicy().hasHeightForWidth())
        self.gigStandardLineEdit.setSizePolicy(sizePolicy)
        self.gigStandardLineEdit.setMinimumSize(QtCore.QSize(320, 71))
        self.gigStandardLineEdit.setObjectName("gigStandardLineEdit")
        self.gigStandardLayout.addWidget(self.gigStandardLineEdit)
        self.horizontalLayout_2.addLayout(self.gigStandardLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cargoLayout = QtWidgets.QHBoxLayout()
        self.cargoLayout.setSpacing(6)
        self.cargoLayout.setObjectName("cargoLayout")
        self.cargoLabel = QtWidgets.QLabel(self.centralwidget)
        self.cargoLabel.setMinimumSize(QtCore.QSize(172, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.cargoLabel.setFont(font)
        self.cargoLabel.setObjectName("cargoLabel")
        self.cargoLayout.addWidget(self.cargoLabel)
        self.cargoLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cargoLineEdit.sizePolicy().hasHeightForWidth())
        self.cargoLineEdit.setSizePolicy(sizePolicy)
        self.cargoLineEdit.setMinimumSize(QtCore.QSize(320, 71))
        self.cargoLineEdit.setObjectName("cargoLineEdit")
        self.cargoLayout.addWidget(self.cargoLineEdit)
        self.horizontalLayout_3.addLayout(self.cargoLayout)
        self.gigGoldenLayout = QtWidgets.QHBoxLayout()
        self.gigGoldenLayout.setSpacing(6)
        self.gigGoldenLayout.setObjectName("gigGoldenLayout")
        self.gigGoldenLabel = QtWidgets.QLabel(self.centralwidget)
        self.gigGoldenLabel.setMinimumSize(QtCore.QSize(172, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.gigGoldenLabel.setFont(font)
        self.gigGoldenLabel.setObjectName("gigGoldenLabel")
        self.gigGoldenLayout.addWidget(self.gigGoldenLabel)
        self.gigGoldenLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gigGoldenLineEdit.sizePolicy().hasHeightForWidth())
        self.gigGoldenLineEdit.setSizePolicy(sizePolicy)
        self.gigGoldenLineEdit.setMinimumSize(QtCore.QSize(320, 71))
        self.gigGoldenLineEdit.setObjectName("gigGoldenLineEdit")
        self.gigGoldenLayout.addWidget(self.gigGoldenLineEdit)
        self.horizontalLayout_3.addLayout(self.gigGoldenLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.liabilityLayout = QtWidgets.QHBoxLayout()
        self.liabilityLayout.setSpacing(6)
        self.liabilityLayout.setObjectName("liabilityLayout")
        self.liabilityLabel = QtWidgets.QLabel(self.centralwidget)
        self.liabilityLabel.setMinimumSize(QtCore.QSize(172, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.liabilityLabel.setFont(font)
        self.liabilityLabel.setObjectName("liabilityLabel")
        self.liabilityLayout.addWidget(self.liabilityLabel)
        self.liabilityLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.liabilityLineEdit.sizePolicy().hasHeightForWidth())
        self.liabilityLineEdit.setSizePolicy(sizePolicy)
        self.liabilityLineEdit.setMinimumSize(QtCore.QSize(320, 71))
        self.liabilityLineEdit.setText("")
        self.liabilityLineEdit.setObjectName("liabilityLineEdit")
        self.liabilityLayout.addWidget(self.liabilityLineEdit)
        self.horizontalLayout_4.addLayout(self.liabilityLayout)
        self.sarwaLayout = QtWidgets.QHBoxLayout()
        self.sarwaLayout.setSpacing(6)
        self.sarwaLayout.setObjectName("sarwaLayout")
        self.sarwaLabel = QtWidgets.QLabel(self.centralwidget)
        self.sarwaLabel.setMinimumSize(QtCore.QSize(172, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.sarwaLabel.setFont(font)
        self.sarwaLabel.setObjectName("sarwaLabel")
        self.sarwaLayout.addWidget(self.sarwaLabel)
        self.sarwaLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sarwaLineEdit.sizePolicy().hasHeightForWidth())
        self.sarwaLineEdit.setSizePolicy(sizePolicy)
        self.sarwaLineEdit.setMinimumSize(QtCore.QSize(320, 71))
        self.sarwaLineEdit.setObjectName("sarwaLineEdit")
        self.sarwaLayout.addWidget(self.sarwaLineEdit)
        self.horizontalLayout_4.addLayout(self.sarwaLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lifeTermLayout = QtWidgets.QHBoxLayout()
        self.lifeTermLayout.setSpacing(6)
        self.lifeTermLayout.setObjectName("lifeTermLayout")
        self.lifeTermLabel = QtWidgets.QLabel(self.centralwidget)
        self.lifeTermLabel.setMinimumSize(QtCore.QSize(172, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.lifeTermLabel.setFont(font)
        self.lifeTermLabel.setObjectName("lifeTermLabel")
        self.lifeTermLayout.addWidget(self.lifeTermLabel)
        self.lifeTermLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lifeTermLineEdit.sizePolicy().hasHeightForWidth())
        self.lifeTermLineEdit.setSizePolicy(sizePolicy)
        self.lifeTermLineEdit.setMinimumSize(QtCore.QSize(320, 71))
        self.lifeTermLineEdit.setText("")
        self.lifeTermLineEdit.setObjectName("lifeTermLineEdit")
        self.lifeTermLayout.addWidget(self.lifeTermLineEdit)
        self.horizontalLayout_6.addLayout(self.lifeTermLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.brokerLabel = QtWidgets.QLabel(self.centralwidget)
        self.brokerLabel.setMinimumSize(QtCore.QSize(172, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.brokerLabel.setFont(font)
        self.brokerLabel.setObjectName("brokerLabel")
        self.horizontalLayout_5.addWidget(self.brokerLabel)
        self.brokerComoBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brokerComoBox.sizePolicy().hasHeightForWidth())
        self.brokerComoBox.setSizePolicy(sizePolicy)
        self.brokerComoBox.setMinimumSize(QtCore.QSize(320, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.brokerComoBox.setFont(font)
        self.brokerComoBox.setObjectName("brokerComoBox")
        self.brokerComoBox.addItem("")
        self.horizontalLayout_5.addWidget(self.brokerComoBox)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_7.addWidget(self.cancelButton)
        self.generateCommissionStructureButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generateCommissionStructureButton.sizePolicy().hasHeightForWidth())
        self.generateCommissionStructureButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.generateCommissionStructureButton.setFont(font)
        self.generateCommissionStructureButton.setObjectName("generateCommissionStructureButton")
        self.horizontalLayout_7.addWidget(self.generateCommissionStructureButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Commission structure"))
        self.creditLabel.setText(_translate("MainWindow", "Credit"))
        self.commercialLabel.setText(_translate("MainWindow", "commercial"))
        self.fireBurglaryLabel.setText(_translate("MainWindow", "Fire & Burglary"))
        self.gigStandardLabel.setText(_translate("MainWindow", "GIG standard"))
        self.cargoLabel.setText(_translate("MainWindow", "Cargo"))
        self.gigGoldenLabel.setText(_translate("MainWindow", "GIG Golden"))
        self.liabilityLabel.setText(_translate("MainWindow", "Liability"))
        self.sarwaLabel.setText(_translate("MainWindow", "Sarwa"))
        self.lifeTermLabel.setText(_translate("MainWindow", "Life term"))
        self.brokerLabel.setText(_translate("MainWindow", "Broker"))
        self.brokerComoBox.setItemText(0, _translate("MainWindow", "Select broker"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))
        self.generateCommissionStructureButton.setText(_translate("MainWindow", "Generate commission structure"))
