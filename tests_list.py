import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5 import Qt
from test_listing import Ui_TestListing

class TestListing():
    def __init__(self,testcode:int, testname: str, questions: int, time: int, subjectname: str, attempted: bool):
        self.testcode = testcode
        self.testname = testname
        self.questions = questions
        self.time = time 
        self.subjectname = subjectname
        self.attempted = attempted

class ResultListing():
    def __init__(self, testcode: int, testname: int, score:int, total:int, subjectname: str):
        self.testcode = testcode
        self.testname = testname
        self.score = score
        self.total = total
        self.subjectname = subjectname

class TestList(qtw.QWidget):
    def __init__(self, tests):
        super().__init__()
        self.tuis = []
        main_layout = qtw.QHBoxLayout()
        self.setStyleSheet("""
        #main {
            background: #eee;
        }
        """)
        self.setObjectName("main")
        self.tests = tests
        main_layout.addItem(qtw.QSpacerItem(60, 40, qtw.QSizePolicy.Maximum, qtw.QSizePolicy.Minimum))
        self.tbox = qtw.QVBoxLayout()
        testheader = qtw.QLabel("Available Tests")
        testheader.setFont(Qt.QFont("Segoe UI", 22))
        testheader.setAlignment(Qt.Qt.AlignCenter)
        self.tbox.addWidget(testheader)
        line = qtw.QFrame()
        line.setObjectName("line")
        line.setStyleSheet("#line { border-top: 1px solid #4589e8;}")
        line.setFrameShape(qtw.QFrame.HLine)
        line.setFrameShadow(qtw.QFrame.Sunken)
        self.tbox.addSpacing(10)
        self.tbox.addWidget(line)
        self.tbox.addSpacing(30)
        for i,test in enumerate(self.tests):
            if test.attempted:
                continue
            x = Ui_TestListing()
            tw = qtw.QWidget()
            x.setupUi(tw)
            x.testname.setText(test.testname)
            x.questioncount.setText(f"{test.questions} questions")
            x.time.setText(f"{test.time} minutes")
            self.tuis.append(tw)
            self.tbox.addWidget(self.tuis[-1])
            self.tbox.addSpacing(30)

        btn_row_wid = qtw.QWidget(self)
        btn_row = qtw.QHBoxLayout(self)
        btn_row.addWidget(qtw.QWidget(self), 3)
        self.submit = qtw.QPushButton(self)
        self.submit.setText("Submit")
        self.submit.setObjectName("submitform")
        self.submit.setFont(Qt.QFont("Segoe UI", 12))
        self.submit.setStyleSheet("""
            #submitform { padding: 7.5px; }
        """)
        self.submit.setSizePolicy(
            qtw.QSizePolicy.Expanding,
            qtw.QSizePolicy.Expanding,
        )
        btn_row.addWidget(self.submit, 1)
        btn_row_wid.setLayout(btn_row)
        self.tbox.addWidget(btn_row_wid)

        qbox_cont = qtw.QScrollArea(self)
        qbox_cont.setAlignment(Qt.Qt.AlignCenter)
        qbox_cont.setFrameShape(qtw.QFrame.NoFrame)
        wid = qtw.QWidget()
        wid.setSizePolicy(
            qtw.QSizePolicy.Expanding,
            qtw.QSizePolicy.Expanding,
        )
        wid.setLayout(self.tbox)
        qbox_cont.setWidget(wid)
        main_layout.addWidget(qbox_cont)
        main_layout.addItem(qtw.QSpacerItem(60, 40, qtw.QSizePolicy.Maximum, qtw.QSizePolicy.Minimum))
        self.setLayout(main_layout)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    tests = [
        TestListing('Test 1', 5, 25, False),
        TestListing('Test 2', 15, 45, False),
        TestListing('Test 3', 20, 60, False),
    ]
    mw = TestList(tests)
    mw.resize(800, 600)
    mw.show()
    sys.exit(app.exec())