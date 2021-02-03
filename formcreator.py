import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5 import Qt
from question import Ui_question
from questiontemp import Ui_questiontemp

from form import Question

class FormCreator(qtw.QWidget):
    def __init__(self, questions, subjects):
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

        header = qtw.QHBoxLayout()
        headerwid = qtw.QWidget(self)
        headerwid.setLayout(header)

        self.subjectchooser = qtw.QComboBox(self)
        self.subjectchooser.setPlaceholderText("Subject..")
        self.subjectchooser.setSizePolicy(
            qtw.QSizePolicy.Maximum,
            qtw.QSizePolicy.Minimum
        )
        self.subjectchooser.setFont(Qt.QFont("Segoe UI", 12))
        for subject in subjects:
            self.subjectchooser.addItem(*subject)
        self.testheader = qtw.QLineEdit()
        self.testheader.setFont(Qt.QFont("Segoe UI", 22))
        self.testheader.setPlaceholderText("Test title..")
        self.testheader.setStyleSheet("background: transparent; border: 1px solid #bbb;")
        self.testheader.setAlignment(Qt.Qt.AlignCenter)

        header.addWidget(self.subjectchooser)
        header.addWidget(self.testheader)
        self.qbox.addWidget(headerwid)

        line = qtw.QFrame()
        line.setObjectName("line")
        line.setStyleSheet("#line { border-top: 1px solid #4589e8;}")
        line.setFrameShape(qtw.QFrame.HLine)
        line.setFrameShadow(qtw.QFrame.Sunken)
        self.qbox.addSpacing(10)
        self.qbox.addWidget(line)
        self.qbox.addSpacing(30)


        for i,q in enumerate(self.questions):
            x = Ui_questiontemp()
            qn = qtw.QWidget()
            x.setupUi(qn)
            x.label.setText(f"{i+1}.")
            x.atext.setText(q.a)
            x.btext.setText(q.b)
            x.ctext.setText(q.c)
            x.dtext.setText(q.d)
            x.questiontext.setText(q.question)

            if q.correct == 1: x.a.setChecked(True)
            elif q.correct == 2: x.b.setChecked(True)
            elif q.correct == 3: x.c.setChecked(True)
            elif q.correct == 4: x.d.setChecked(True)


            q.ui = x
            self.qbox.addWidget(qn)
            self.qbox.addSpacing(30)

        self.btn_row_wid = qtw.QWidget(self)
        btn_row = qtw.QHBoxLayout(self)

        self.addquestion = qtw.QPushButton(self)
        self.addquestion.setText("Add a question")
        self.addquestion.setObjectName("addquestionform")
        self.addquestion.setFont(Qt.QFont("Segoe UI", 12))
        self.addquestion.setStyleSheet("""
            #addquestionform { padding: 7.5px; }
        """)


        self.submit = qtw.QPushButton(self)
        self.submit.setText("Submit")
        self.submit.setObjectName("submitform")
        self.submit.setFont(Qt.QFont("Segoe UI", 12))
        self.submit.setStyleSheet("""
            #submitform { padding: 7.5px; }
        """)


        self.submit.setSizePolicy(
            qtw.QSizePolicy.Expanding,
            qtw.QSizePolicy.Maximum,
        )
        btn_row.addWidget(self.addquestion, 1)
        btn_row.addWidget(qtw.QWidget(self), 3)
        btn_row.addWidget(self.submit, 1)
        self.btn_row_wid.setLayout(btn_row)
        self.qbox.addWidget(self.btn_row_wid)

        self.qbox_cont = qtw.QScrollArea(self)
        self.qbox_cont.setWidgetResizable(True)
        self.qbox_cont.setAlignment(Qt.Qt.AlignCenter)
        self.qbox_cont.setFrameShape(qtw.QFrame.NoFrame)


        wid = qtw.QWidget()
        wid.setSizePolicy(
            qtw.QSizePolicy.Expanding,
            qtw.QSizePolicy.Expanding,
        )
        wid.setLayout(self.qbox)
        self.qbox_cont.setWidget(wid)
        main_layout.addWidget(self.qbox_cont)
        main_layout.addItem(qtw.QSpacerItem(60, 40, qtw.QSizePolicy.Maximum, qtw.QSizePolicy.Minimum))
        self.setLayout(main_layout)
        
    def add_question(self, q: Question):
        self.questions.append(q)
        x = Ui_questiontemp()
        qn = qtw.QWidget()
        x.setupUi(qn)
        x.label.setText(f"{len(self.questions)}.")
        x.atext.setText(q.a)
        x.btext.setText(q.b)
        x.ctext.setText(q.c)
        x.dtext.setText(q.d)
        x.questiontext.setText(q.question)

        if q.correct == 1: x.a.setChecked(True)
        elif q.correct == 2: x.b.setChecked(True)
        elif q.correct == 3: x.c.setChecked(True)
        elif q.correct == 4: x.d.setChecked(True)

        q.ui = x
        self.qbox.removeWidget(self.btn_row_wid)
        self.qbox.addWidget(qn)
        self.qbox.addSpacing( 30)
        self.qbox.addWidget(self.btn_row_wid)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    questions = [
          Question("Why can't I think of other questions? This really ought to overflow by now", 'Why now', '41', '43', 'idk', 7, 4),
    ]
    testname = "A test test"
    subjects = [("A long subject", 1), ("B", 2)]
    mw = FormCreator(questions, subjects)
    mw.addquestion.clicked.connect(lambda: mw.add_question(Question("", "", "", "", "", 51, 0)))
    mw.show()
    mw.resize(800, 600)
    sys.exit(app.exec())