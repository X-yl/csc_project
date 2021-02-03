import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5 import Qt
from question import Ui_question

class Question():
    def __init__(self, question, a, b, c, d, qcode, correct):
        self.question = question
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.qcode = qcode
        self.correct = correct
    
class Form(qtw.QWidget):
    def __init__(self, testname, questions):
        super().__init__()
        self.quis = []
        main_layout = qtw.QHBoxLayout()
        self.setStyleSheet("""
        #main {
            background: #eee;
        }
        """)
        self.setObjectName("main")
        self.questions = questions
        main_layout.addItem(qtw.QSpacerItem(60, 40, qtw.QSizePolicy.Maximum, qtw.QSizePolicy.Minimum))
        self.qbox = qtw.QVBoxLayout()
        self.testheader = qtw.QLabel(testname)
        self.testheader.setFont(Qt.QFont("Segoe UI", 22))
        self.testheader.setAlignment(Qt.Qt.AlignCenter)
        self.qbox.addWidget(self.testheader)
        line = qtw.QFrame()
        line.setObjectName("line")
        line.setStyleSheet("#line { border-top: 1px solid #4589e8;}")
        line.setFrameShape(qtw.QFrame.HLine)
        line.setFrameShadow(qtw.QFrame.Sunken)
        self.qbox.addSpacing(10)
        self.qbox.addWidget(line)
        self.qbox.addSpacing(30)
        for i,q in enumerate(self.questions):
            x = Ui_question()
            qn = qtw.QWidget()
            x.setupUi(qn)
            x.questionText.setText(q.question)
            x.a.setText(q.a)
            x.b.setText(q.b)
            x.c.setText(q.c)
            x.d.setText(q.d)
            x.qcode = q.qcode # save this in here to save us the trouble later..
            q.ui = x
            q.uiwid = qn
            self.qbox.addWidget(qn)
            self.qbox.addSpacing(30)

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
    app = qtw.QApplication(sys.argv)
    questions = [
            Question("What is the meaning of life?", '42', '41', '43', '40', '2'),
            Question("Why can't I think of other questions?", '42', '41', '43', 'idk', 4),
            Question("Why can't I think of other questions?", '42', '41', '43', 'idk', 4),
            Question("Why can't I think of other questions? This really ought to overflow by now", 'Why now', '41', '43', 'idk', 4),
    ]
    testname = "A test test"
    mw = Form(testname, questions)
    mw.show()
    sys.exit(app.exec())