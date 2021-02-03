# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'question.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_question(object):
    def setupUi(self, question):
        question.setObjectName("question")
        question.resize(608, 322)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(question.sizePolicy().hasHeightForWidth())
        question.setSizePolicy(sizePolicy)
        question.setMinimumSize(QtCore.QSize(600, 300))
        question.setStyleSheet("#question {\n"
"background: #fff;\n"
"border: 1px solid #4589e8;\n"
"}\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(question)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(question)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 87))
        self.groupBox.setStyleSheet("#groupBox {\n"
"border-top: 1px solid #4589e8;\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.a = QtWidgets.QRadioButton(self.groupBox)
        self.a.setGeometry(QtCore.QRect(0, 0, 381, 44))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.a.sizePolicy().hasHeightForWidth())
        self.a.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.a.setFont(font)
        self.a.setObjectName("a")
        self.d = QtWidgets.QRadioButton(self.groupBox)
        self.d.setGeometry(QtCore.QRect(0, 151, 381, 44))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.d.sizePolicy().hasHeightForWidth())
        self.d.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.d.setFont(font)
        self.d.setObjectName("d")
        self.c = QtWidgets.QRadioButton(self.groupBox)
        self.c.setGeometry(QtCore.QRect(0, 100, 381, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.c.sizePolicy().hasHeightForWidth())
        self.c.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.c.setFont(font)
        self.c.setObjectName("c")
        self.aans = QtWidgets.QLabel(self.groupBox)
        self.aans.setGeometry(QtCore.QRect(387, 0, 76, 44))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aans.sizePolicy().hasHeightForWidth())
        self.aans.setSizePolicy(sizePolicy)
        self.aans.setText("")
        self.aans.setObjectName("aans")
        self.dans = QtWidgets.QLabel(self.groupBox)
        self.dans.setGeometry(QtCore.QRect(387, 151, 76, 44))
        self.dans.setText("")
        self.dans.setObjectName("dans")
        self.bans = QtWidgets.QLabel(self.groupBox)
        self.bans.setGeometry(QtCore.QRect(387, 50, 76, 44))
        self.bans.setText("")
        self.bans.setObjectName("bans")
        self.b = QtWidgets.QRadioButton(self.groupBox)
        self.b.setGeometry(QtCore.QRect(0, 50, 381, 44))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.b.sizePolicy().hasHeightForWidth())
        self.b.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.b.setFont(font)
        self.b.setObjectName("b")
        self.cans = QtWidgets.QLabel(self.groupBox)
        self.cans.setGeometry(QtCore.QRect(387, 100, 76, 45))
        self.cans.setText("")
        self.cans.setObjectName("cans")
        self.gridLayout.addWidget(self.groupBox, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        self.questionText = QtWidgets.QLabel(question)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.questionText.sizePolicy().hasHeightForWidth())
        self.questionText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.questionText.setFont(font)
        self.questionText.setWordWrap(True)
        self.questionText.setObjectName("questionText")
        self.gridLayout.addWidget(self.questionText, 0, 2, 1, 1)

        self.retranslateUi(question)
        QtCore.QMetaObject.connectSlotsByName(question)

    def retranslateUi(self, question):
        _translate = QtCore.QCoreApplication.translate
        question.setWindowTitle(_translate("question", "Form"))
        self.a.setText(_translate("question", "Option A"))
        self.d.setText(_translate("question", "Option D"))
        self.c.setText(_translate("question", "Option C"))
        self.b.setText(_translate("question", "Option B"))
        self.questionText.setText(_translate("question", "1. Insert Question Text?"))
