import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from form import Form, Question
from login import Ui_Login
from backend import BackendStuff
from question import Ui_question
from  thanks import Ui_Thanks
from dash import Ui_Dash
from tests_list import TestListing, ResultListing
from test_listing import Ui_TestListing
from PyQt5.Qt import QFont, Qt
from scoredash import Ui_scoredash
from test_result import Ui_ResultListing
from dash_admin import Ui_DashAdmin
from questiontemp import Ui_questiontemp
from formcreator import FormCreator
from score_list import ScoreList
import pyqtgraph as pg

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.backend = BackendStuff()
        self.setWindowTitle("ExamSim 9000")
        self.resize(900, 600)
        
        self.main_wid = qtw.QStackedWidget(self)
        self.generate_login()
        self.setCentralWidget(self.main_wid)
        self.show()

    def generate_login(self):
        self.login_wid = qtw.QWidget(self)
        self.login = Ui_Login()
        self.login.setupUi(self.login_wid)
        self.login.submit.clicked.connect(self.validate_password) 
        self.main_wid.addWidget(self.login_wid)
        self.login.username.setFocus()

    def generate_dash(self):
        self.dashwid = qtw.QWidget(self)
        self.dash = Ui_Dash()
        self.dash.setupUi(self.dashwid)
        name = self.backend.get_name(self.currentid)
        self.dash.welcome.setText(f"Welcome, {name}")
        self.gen_dash_test_list()
        self.gen_score_dash()
        self.gen_all_scores()
        self.main_wid.addWidget(self.dashwid)

    def gen_all_scores(self):
        resulttuples = self.backend.fetchscores(self.currentid)
        rbox = qtw.QVBoxLayout()
        rwid = qtw.QWidget(self)
        rwid.setLayout(rbox)
        contscroll = qtw.QScrollArea(self)
        contscroll.setWidget(rwid)
        rwid.setObjectName("rwid") 
        self.dash.allscoreslayout.addWidget(rwid)
        tests = [ResultListing(*a) for a in resulttuples]

        for i,result in enumerate(tests):
            x = Ui_ResultListing()
            rw = qtw.QWidget(self)
            x.setupUi(rw)
            x.score.setText(f"{result.score}/{result.total}")
            #self.tuis.append(tw)
            result.ui=x
            x.testname.setText(f"{result.testname} — {result.subjectname} ")
            x.viewDetails.clicked.connect(lambda annoyingbug, result=result: self.view_test_results(result.testcode, f"{result.score}/{result.total}", self.currentid))
            #x.attempt.clicked.connect(lambda annoyingbug, test=result: self.goto_test(test.testcode))
            rbox.addWidget(rw)
            rbox.addSpacing(30)
        
        rwid.setStyleSheet("#rwid { background-color: #f7f7f7;}")
        self.dash.tests.setAlignment(Qt.AlignCenter)
        rbox.setAlignment(Qt.AlignCenter)

    def gen_score_dash(self):
        scrwid = qtw.QWidget()
        self.score_dash = Ui_scoredash()
        self.score_dash.setupUi(scrwid)
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        pg.setConfigOption('antialias', True)
        graphWidget = pg.PlotWidget()

        scores, testnames = self.backend.get_graph(self.currentid)

        ticks = list(enumerate(testnames))
        pen = pg.mkPen(color=(80,80,80), width=1.5)
        graphWidget.plot([x[0] for x in ticks], scores, pen=pen, symbol='o', size=1)
        graphWidget.getPlotItem().getAxis('bottom').setTicks([ticks])
        graphWidget.setYRange(0, 100)
        graphWidget.setMouseEnabled(True, False)

        lt = self.backend.get_last_test(self.currentid)
        if lt is not None:
            tcode, tname, tscore, total = lt
            self.score_dash.testname.setText(tname)
            self.score_dash.score.setText(f"{tscore}/{total}")
            self.score_dash.viewDetails.clicked.connect(lambda ab, tcode=tcode: self.view_test_results(tcode,f"{tscore}/{total}", self.currentid))
        else:
            self.score_dash.testname.setText("No tests available")
            self.score_dash.score.setText("-")
            self.score_dash.viewDetails.setDisabled(True)

        overall, subjects = self.backend.get_avgs(self.currentid)
        self.score_dash.overallavg.setText(f"{overall*100:.2f}%")
        namefont = QFont("Segoe UI", 16)
        pfont = QFont("Segoe UI Light", 14)
        for subject in subjects:
            sname = qtw.QLabel(f"{subject[0]}", self)
            sname.setFont(namefont)
            sname.setSizePolicy(
                qtw.QSizePolicy.Preferred,
                qtw.QSizePolicy.Fixed
            )
            p = qtw.QLabel(f"{subject[1]*100:.2f}%", self)
            p.setStyleSheet("padding: 5px")
            p.setFont(pfont)
            p.setSizePolicy(
                qtw.QSizePolicy.Preferred,
                qtw.QSizePolicy.Fixed
            )
            p.setMinimumHeight(40)
            sname.setMinimumHeight(40)
            self.score_dash.avgs.layout().addRow(sname, p)


        self.score_dash.graphcontainer.addWidget(graphWidget)
        self.dash.scoredashlayout.addWidget(scrwid)
        self.dash.scoretab.setCurrentIndex(0)

    def view_test_results(self, testcode, score, sid):
        self.generate_test(testcode)
        qcodes = [question.qcode for question in self.questions]
        choices = self.backend.get_choices(testcode, sid, qcodes)

        # the lord alone can save us now
        for question, choice in zip(self.questions, choices):
            qui = question.ui
            ctext= '<font color=\"green\">Correct</font>'
            if question.correct == 1:
                qui.aans.setText(ctext)
            elif question.correct == 2:
                qui.bans.setText(ctext)
            elif question.correct == 3:
                qui.cans.setText(ctext)
            elif question.correct == 4:
                qui.dans.setText(ctext)

            if question.correct == choice:
                question.uiwid.setStyleSheet(question.uiwid.styleSheet() + "#question{background-color: #e6f9e5;}" )
            else:
                question.uiwid.setStyleSheet(question.uiwid.styleSheet() + "#question{background-color: #fcd4d6;}" )

            s = """
            #a:disabled,#b:disabled,#c:disabled,#d:disabled{
                color: #000000;
            }
            QRadioButton::indicator::checked{
                 border: 1px solid white; border-radius: 6px; background-color: #333; width: 10px; height: 10px;}
            """
            
            qui.a.setStyleSheet(s)
            qui.b.setStyleSheet(s)
            qui.c.setStyleSheet(s)
            qui.d.setStyleSheet(s)

            if choice == 1: qui.a.setChecked(True)
            elif choice == 2: qui.b.setChecked(True)
            elif choice == 3: qui.c.setChecked(True)
            elif choice == 4: qui.d.setChecked(True)

            qui.a.setDisabled(True)
            qui.b.setDisabled(True)
            qui.c.setDisabled(True)
            qui.d.setDisabled(True)
        
        self.form.submit.disconnect() # disconnect from submit
        self.form.submit.setText("Back")
        self.form.submit.clicked.connect(self.return_to_dash)

        self.form.testheader.setText(self.form.testheader.text() + "  —  " + score)
        self.main_wid.setCurrentWidget(self.form)

    def gen_dash_test_list(self):
        testtuples = self.backend.fetchtests(self.currentid)
        tbox = qtw.QVBoxLayout()
        twid = qtw.QWidget(self)
        twid.setLayout(tbox)
        self.dash.tests.setWidget(twid)
        twid.setObjectName("twid")
        self.tests = [TestListing(*a) for a in testtuples]

        for i,test in enumerate(self.tests):
            if not test.attempted:
                x = Ui_TestListing()
                tw = qtw.QWidget(self)
                x.setupUi(tw)
                x.testname.setText(f"{test.testname} — {test.subjectname} ")
                x.questioncount.setText(f"{test.questions} questions")
                x.time.setText(f"{test.time} minutes")
                #self.tuis.append(tw)
                test.ui=x
                x.attempt.clicked.connect(lambda annoyingbug, test=test: self.goto_test(test.testcode))
                tbox.addWidget(tw)
                tbox.addSpacing(30)
        
        twid.setStyleSheet("#twid { background-color: #f7f7f7;}")
        self.dash.tests.setAlignment(Qt.AlignCenter)
        tbox.setAlignment(Qt.AlignCenter)

    def goto_test(self, testcode):
        self.generate_test(testcode)
        self.main_wid.setCurrentWidget(self.form)

    def generate_admin_dash(self):
        self.dashwid = qtw.QWidget(self)
        self.dash = Ui_DashAdmin()
        self.dash.setupUi(self.dashwid)
        self.main_wid.addWidget(self.dashwid)
        self.generate_admin_tests()

    def modify_test(self, testcode: int):
        testname, questiontuples = self.backend.get_test_details(testcode)
        self.questions = []
        self.testcode = testcode
        for question in questiontuples:
            self.questions.append(
                Question(
                    # q,a,b,c,d,qcode,correct
                    *[str(x) for x in question[1:6]], question[0], question[6]
                )
            )

        subjects = self.backend.get_subjects()
        self.creator = FormCreator(self.questions, subjects)
        self.subjectcode = self.backend.get_subject_code(testcode)
        self.creator.subjectchooser.setCurrentIndex(self.creator.subjectchooser.findData(self.subjectcode))
        self.creator.addquestion.clicked.connect(lambda: self.creator.add_question(Question("", "", "", "", "", 0, -1)))
        self.creator.submit.clicked.connect(self.submit_new_test)
        self.creator.testheader.setText(testname)
        self.main_wid.addWidget(self.creator)
        self.main_wid.setCurrentWidget(self.creator)
        
    def submit_new_test(self):
        subjectcode = self.creator.subjectchooser.currentData()
        testname = self.creator.testheader.text()
        testcode = self.testcode
        questions = []
        question: Question = None
        for question in self.questions:
            qui: Ui_questiontemp = question.ui
            optcode = None
            if qui.a.isChecked(): optcode = 1
            elif qui.b.isChecked(): optcode = 2
            elif qui.c.isChecked(): optcode = 3
            elif qui.d.isChecked(): optcode = 4
            questions.append(
                Question(qui.questiontext.text(),qui.atext.text(), qui.btext.text(), qui.ctext.text(), qui.dtext.text(), question.qcode, optcode)
            )
        self.backend.submit_test_creator(subjectcode, testcode,testname, questions)
        self.return_to_admin_dash()

    def create_new_test(self):
        self.questions = [
                Question("", '', '', '', '', 0,-1),
        ]
        self.testcode = 0
        subjects = self.backend.get_subjects()
        self.creator = FormCreator(self.questions, subjects)
        self.creator.addquestion.clicked.connect(lambda: self.creator.add_question(Question("", "", "", "", "", 0, -1)))
        self.main_wid.addWidget(self.creator)
        self.main_wid.setCurrentWidget(self.creator)
        self.creator.submit.clicked.connect(self.submit_new_test)


    def finish_update_test(self):
        testname = self.creator.testheader.text()

    def export_csv(self):
        options = qtw.QFileDialog.Options()
        filename, _ = qtw.QFileDialog.getSaveFileName(self,"Export as CSV","","Comma Separated Value Files (*.csv);;All Files (*)", options=options)
        if filename:
            self.backend.export_csv(self.testcode, filename, self.score_list.results)

    def show_test_scores(self, testcode):
        testname, results = self.backend.get_test_scores(testcode)
        self.testcode = testcode
        self.score_list = ScoreList(testname, results)
        for result in self.score_list.results:
            result.ui.viewDetails.clicked.connect(lambda annoyingbug, result=result: 
                (
                    self.view_test_results(result.testcode, f"{result.score}/{result.total}", result.studentcode), 
                    self.form.submit.clicked.disconnect(),
                    self.form.submit.clicked.connect(lambda: self.show_test_scores(testcode))
                ) 
            )
            
        self.score_list.back.clicked.connect(self.return_to_admin_dash)
        self.score_list.export.clicked.connect(self.export_csv)
        self.main_wid.addWidget(self.score_list)
        self.main_wid.setCurrentWidget(self.score_list)

    def generate_admin_tests(self):
        self.dash.newtest.clicked.connect(self.create_new_test)
        # just so lazy
        self.gen_dash_test_list()
        for test in self.tests:
            test.ui.attempted.setText('')
            scoresBtn = qtw.QPushButton()
            scoresBtn.setText("View Scores")
            scoresBtn.setSizePolicy(
                qtw.QSizePolicy.Expanding,
                qtw.QSizePolicy.Fixed
            )
            scoresBtn.clicked.connect(lambda annoyingbug, test=test: self.show_test_scores(test.testcode))
            test.ui.horizontalLayout.addWidget(scoresBtn)
            test.ui.attempt.setText('Edit')
            test.ui.attempt.disconnect()
            test.ui.line_3.setVisible(False)
            test.ui.attempt.clicked.connect(lambda annoyingbug, test=test: self.modify_test(test.testcode))


    def validate_password(self):
        if self.backend.validate_password(self.login.username.text(), self.login.password.text()):
            if self.login.username.text() != "admin":
                self.currentid = int(self.login.username.text())
                self.generate_dash()
                self.main_wid.setCurrentWidget(self.dashwid)
            else:
                self.currentid = None
                self.generate_admin_dash()
                self.main_wid.setCurrentWidget(self.dashwid)
        else:
            self.login.status.setText("<font color=\"red\"><b>Invalid credentials</b></font>")

    def generate_test(self, testcode):
        testname, questiontuples = self.backend.get_test_details(testcode)
        self.questions = []
        self.testcode = testcode
        for question in questiontuples:
            self.questions.append(
                Question(
                    # q,a,b,c,d,qcode,correct
                    *[str(x) for x in question[1:6]], question[0], question[6]
                )
            )
        self.form = Form(testname, self.questions)
        self.form.submit.clicked.connect(self.submit_test)
        self.main_wid.addWidget(self.form)

    def submit_test(self):
        testcode = self.testcode
        sid = self.currentid
        choices = []
        qcodes = []
        for question in self.form.questions:
            qui = question.ui
            if qui.a.isChecked(): choices.append(1)
            elif qui.b.isChecked(): choices.append(2)
            elif qui.c.isChecked(): choices.append(3)
            elif qui.d.isChecked(): choices.append(4)
            else: choices.append(None)

            qcodes.append(question.qcode)
        numcorrect = len([q for q, a in zip(self.form.questions, choices) if q.correct == a])

        self.backend.submit_test(testcode, sid, qcodes, choices, numcorrect)
        self.generate_thanks()
        self.main_wid.setCurrentWidget(self.thankswid)

    def return_to_admin_dash(self):
        self.generate_admin_dash()
        self.main_wid.setCurrentWidget(self.dashwid)


    def return_to_dash(self):
        self.generate_dash()
        self.main_wid.setCurrentWidget(self.dashwid)

    def generate_thanks(self):
        self.thankswid = qtw.QWidget()
        self.dash = Ui_Thanks()
        self.dash.setupUi(self.thankswid)
        self.main_wid.addWidget(self.thankswid)
        self.dash.back.clicked.connect(self.return_to_dash)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())