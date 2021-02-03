# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_listing.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TestListing(object):
    def setupUi(self, TestListing):
        TestListing.setObjectName("TestListing")
        TestListing.resize(608, 322)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TestListing.sizePolicy().hasHeightForWidth())
        TestListing.setSizePolicy(sizePolicy)
        TestListing.setMinimumSize(QtCore.QSize(600, 100))
        TestListing.setStyleSheet("#TestListing {\n"
"background: #fff;\n"
"border: 1px solid #4589e8;\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(TestListing)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.testname = QtWidgets.QLabel(TestListing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.testname.sizePolicy().hasHeightForWidth())
        self.testname.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.testname.setFont(font)
        self.testname.setStyleSheet("#testname {\n"
"margin-left: 20px;\n"
"}")
        self.testname.setObjectName("testname")
        self.verticalLayout.addWidget(self.testname)
        self.line = QtWidgets.QFrame(TestListing)
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.time = QtWidgets.QLabel(TestListing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.time.sizePolicy().hasHeightForWidth())
        self.time.setSizePolicy(sizePolicy)
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setObjectName("time")
        self.horizontalLayout.addWidget(self.time)
        self.line_2 = QtWidgets.QFrame(TestListing)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.questioncount = QtWidgets.QLabel(TestListing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.questioncount.sizePolicy().hasHeightForWidth())
        self.questioncount.setSizePolicy(sizePolicy)
        self.questioncount.setAlignment(QtCore.Qt.AlignCenter)
        self.questioncount.setObjectName("questioncount")
        self.horizontalLayout.addWidget(self.questioncount)
        self.line_3 = QtWidgets.QFrame(TestListing)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.attempted = QtWidgets.QLabel(TestListing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.attempted.sizePolicy().hasHeightForWidth())
        self.attempted.setSizePolicy(sizePolicy)
        self.attempted.setAlignment(QtCore.Qt.AlignCenter)
        self.attempted.setObjectName("attempted")
        self.horizontalLayout.addWidget(self.attempted)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.attempt = QtWidgets.QPushButton(TestListing)
        self.attempt.setObjectName("attempt")
        self.horizontalLayout.addWidget(self.attempt)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 1)
        self.horizontalLayout.setStretch(6, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(TestListing)
        QtCore.QMetaObject.connectSlotsByName(TestListing)

    def retranslateUi(self, TestListing):
        _translate = QtCore.QCoreApplication.translate
        TestListing.setWindowTitle(_translate("TestListing", "Form"))
        self.testname.setText(_translate("TestListing", "First Test"))
        self.time.setText(_translate("TestListing", "25 Minutes"))
        self.questioncount.setText(_translate("TestListing", "35 Questions"))
        self.attempted.setText(_translate("TestListing", "Not Attempted"))
        self.attempt.setText(_translate("TestListing", "Attempt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TestListing = QtWidgets.QWidget()
    ui = Ui_TestListing()
    ui.setupUi(TestListing)
    TestListing.show()
    sys.exit(app.exec_())