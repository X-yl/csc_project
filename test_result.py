# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_result.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ResultListing(object):
    def setupUi(self, ResultListing):
        ResultListing.setObjectName("ResultListing")
        ResultListing.resize(580, 161)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ResultListing.sizePolicy().hasHeightForWidth())
        ResultListing.setSizePolicy(sizePolicy)
        ResultListing.setMinimumSize(QtCore.QSize(550, 0))
        ResultListing.setStyleSheet("#ResultListing \n"
"{\n"
"background: #fff;\n"
"border: 1px solid #4589e8;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(ResultListing)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.score = QtWidgets.QLabel(ResultListing)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.score.setFont(font)
        self.score.setObjectName("score")
        self.horizontalLayout.addWidget(self.score)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.line_2 = QtWidgets.QFrame(ResultListing)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.viewDetails = QtWidgets.QPushButton(ResultListing)
        self.viewDetails.setObjectName("viewDetails")
        self.horizontalLayout.addWidget(self.viewDetails)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 2, 2)
        self.testname = QtWidgets.QLabel(ResultListing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testname.sizePolicy().hasHeightForWidth())
        self.testname.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.testname.setFont(font)
        self.testname.setObjectName("testname")
        self.gridLayout.addWidget(self.testname, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(ResultListing)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)

        self.retranslateUi(ResultListing)
        QtCore.QMetaObject.connectSlotsByName(ResultListing)

    def retranslateUi(self, ResultListing):
        _translate = QtCore.QCoreApplication.translate
        ResultListing.setWindowTitle(_translate("ResultListing", "Form"))
        self.score.setText(_translate("ResultListing", "7/10"))
        self.viewDetails.setText(_translate("ResultListing", "View details"))
        self.testname.setText(_translate("ResultListing", "Test name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ResultListing = QtWidgets.QWidget()
    ui = Ui_ResultListing()
    ui.setupUi(ResultListing)
    ResultListing.show()
    sys.exit(app.exec_())
