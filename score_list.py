import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5 import Qt
from question import Ui_question
from test_result import Ui_ResultListing
from tests_list import ResultListing

class ScoreList(qtw.QWidget):
    def __init__(self, testname, results):
        super().__init__()
        self.quis = []
        main_layout = qtw.QHBoxLayout()
        self.setStyleSheet("""
        #main {
            background: #eee;
        }
        """)
        self.setObjectName("main")
        main_layout.addItem(qtw.QSpacerItem(60, 40, qtw.QSizePolicy.Maximum, qtw.QSizePolicy.Minimum))
        self.qbox = qtw.QVBoxLayout()
        self.results = results
        testheader = qtw.QLabel()
        testheader.setText(testname)
        testheader.setFont(Qt.QFont("Segoe UI", 22))
        testheader.setAlignment(Qt.Qt.AlignCenter)
        self.qbox.addWidget(testheader)
        line = qtw.QFrame()
        line.setObjectName("line")
        line.setStyleSheet("#line { border-top: 1px solid #4589e8;}")
        line.setFrameShape(qtw.QFrame.HLine)
        line.setFrameShadow(qtw.QFrame.Sunken)
        self.qbox.addSpacing(10)
        self.qbox.addWidget(line)
        self.qbox.addSpacing(30)

        for result in results:
            rui = Ui_ResultListing()
            ruiwid = qtw.QWidget(self)
            rui.setupUi(ruiwid)
            rui.testname.setText(result.testname)
            rui.score.setText(f"{result.score}/{result.total}")
            result.ui = rui
            self.qbox.addWidget(ruiwid)
            self.qbox.addSpacing(30)

        btn_row_wid = qtw.QWidget(self)
        btn_row = qtw.QHBoxLayout(self)
        btn_row.addWidget(qtw.QWidget(self), 3)


        self.export = qtw.QPushButton(self)
        self.export.setText("Export Results to CSV")
        self.export.setObjectName("export")
        self.export.setFont(Qt.QFont("Segoe UI", 12))
        self.export.setStyleSheet("""
            #export { padding: 7.5px; }
        """)
        self.export.setSizePolicy(
            qtw.QSizePolicy.Expanding,
            qtw.QSizePolicy.Expanding,
        )
        btn_row.addWidget(self.export, 1)


        self.back = qtw.QPushButton(self)
        self.back.setText("Back")
        self.back.setObjectName("back")
        self.back.setFont(Qt.QFont("Segoe UI", 12))
        self.back.setStyleSheet("""
            #back { padding: 7.5px; }
        """)
        self.back.setSizePolicy(
            qtw.QSizePolicy.Expanding,
            qtw.QSizePolicy.Expanding,
        )
        btn_row.addWidget(self.back, 1)


        btn_row_wid.setLayout(btn_row)
        self.qbox.addWidget(btn_row_wid)

        qbox_cont = qtw.QScrollArea(self)
        qbox_cont.setAlignment(Qt.Qt.AlignCenter)
        qbox_cont.setFrameShape(qtw.QFrame.NoFrame)
        wid = qtw.QWidget()
        wid.setSizePolicy(
            qtw.QSizePolicy.Expanding,
            qtw.QSizePolicy.Expanding,
        )
        wid.setLayout(self.qbox)
        qbox_cont.setWidget(wid)
        main_layout.addWidget(qbox_cont)
        main_layout.addItem(qtw.QSpacerItem(60, 40, qtw.QSizePolicy.Maximum, qtw.QSizePolicy.Minimum))
        self.setLayout(main_layout)
        


if __name__ == '__main__':
    app = qtw.QApplication([])
    testname = "A test test"
    results = [
    ]
    mw = ScoreList(testname, results)
    mw.show()
    sys.exit(app.exec())