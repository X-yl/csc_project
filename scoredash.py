# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scoredash.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_scoredash(object):
    def setupUi(self, scoredash):
        scoredash.setObjectName("scoredash")
        scoredash.resize(713, 548)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(scoredash.sizePolicy().hasHeightForWidth())
        scoredash.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(scoredash)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(scoredash)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.avgs = QtWidgets.QWidget(scoredash)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.avgs.sizePolicy().hasHeightForWidth())
        self.avgs.setSizePolicy(sizePolicy)
        self.avgs.setStyleSheet("#avgs {\n"
"background: #fff\n"
"}")
        self.avgs.setObjectName("avgs")
        self.formLayout = QtWidgets.QFormLayout(self.avgs)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.avgs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.overallavg = QtWidgets.QLabel(self.avgs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.overallavg.sizePolicy().hasHeightForWidth())
        self.overallavg.setSizePolicy(sizePolicy)
        self.overallavg.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        font.setKerning(True)
        self.overallavg.setFont(font)
        self.overallavg.setStyleSheet("#overallavg{\n"
"padding:5px;\n"
"}\n"
"")
        self.overallavg.setObjectName("overallavg")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.overallavg)
        self.gridLayout.addWidget(self.avgs, 5, 0, 1, 1)
        self.widget = QtWidgets.QWidget(scoredash)
        self.widget.setStyleSheet("#widget {\n"
"background: #ffffff\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.testname = QtWidgets.QLabel(self.widget)
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
        self.verticalLayout.addWidget(self.testname)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.score = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.score.setFont(font)
        self.score.setObjectName("score")
        self.horizontalLayout.addWidget(self.score)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.viewDetails = QtWidgets.QPushButton(self.widget)
        self.viewDetails.setObjectName("viewDetails")
        self.horizontalLayout.addWidget(self.viewDetails)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(scoredash)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(scoredash)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(scoredash)
        self.line_3.setStyleSheet("border-top: 1px solid #4589e8;")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 3, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(scoredash)
        self.line_4.setStyleSheet("#line_4{\n"
"border: 1px solid #4589e8;\n"
"border-top: 0px;\n"
"border-right: 0px;\n"
"border-bottom: 0px;\n"
"}")
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 0, 2, 6, 1)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 3, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 1, 0, 1, 1)
        self.graphcontainer = QtWidgets.QHBoxLayout()
        self.graphcontainer.setObjectName("graphcontainer")
        self.gridLayout_2.addLayout(self.graphcontainer, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 4, 5, 1)

        self.retranslateUi(scoredash)
        QtCore.QMetaObject.connectSlotsByName(scoredash)

    def retranslateUi(self, scoredash):
        _translate = QtCore.QCoreApplication.translate
        scoredash.setWindowTitle(_translate("scoredash", "Form"))
        self.label.setText(_translate("scoredash", "Last Released Score"))
        self.label_3.setText(_translate("scoredash", "Overall:"))
        self.overallavg.setText(_translate("scoredash", "9999"))
        self.testname.setText(_translate("scoredash", "Test name"))
        self.score.setText(_translate("scoredash", "7/10"))
        self.viewDetails.setText(_translate("scoredash", "View details"))
        self.label_4.setText(_translate("scoredash", "Performance by test: "))
        self.label_2.setText(_translate("scoredash", "Average Scores"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    scoredash = QtWidgets.QWidget()
    ui = Ui_scoredash()
    ui.setupUi(scoredash)
    scoredash.show()
    sys.exit(app.exec_())