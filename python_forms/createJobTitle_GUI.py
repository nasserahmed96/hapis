# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/createJobTitle_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_createJobtitle(object):
    def setupUi(self, createJobtitle):
        createJobtitle.setObjectName("createJobtitle")
        createJobtitle.resize(501, 321)
        self.centralwidget = QtWidgets.QWidget(createJobtitle)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.descriptionLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.descriptionLabel.setFont(font)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.descriptionLabel)
        self.descriptionLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.descriptionLineEdit.setObjectName("descriptionLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.descriptionLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 86, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.save_btn.setFont(font)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout.addWidget(self.save_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.clear_btn.setFont(font)
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout.addWidget(self.clear_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        createJobtitle.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(createJobtitle)
        self.statusbar.setObjectName("statusbar")
        createJobtitle.setStatusBar(self.statusbar)

        self.retranslateUi(createJobtitle)
        self.clear_btn.clicked.connect(self.nameLineEdit.clear)
        self.clear_btn.clicked.connect(self.descriptionLineEdit.clear)
        self.cancel_btn.clicked.connect(createJobtitle.close)
        QtCore.QMetaObject.connectSlotsByName(createJobtitle)

    def retranslateUi(self, createJobtitle):
        _translate = QtCore.QCoreApplication.translate
        createJobtitle.setWindowTitle(_translate("createJobtitle", "Create job title"))
        self.nameLabel.setText(_translate("createJobtitle", "Name"))
        self.descriptionLabel.setText(_translate("createJobtitle", "Description"))
        self.save_btn.setText(_translate("createJobtitle", "Save"))
        self.clear_btn.setText(_translate("createJobtitle", "Clear"))
        self.cancel_btn.setText(_translate("createJobtitle", "Cancel"))