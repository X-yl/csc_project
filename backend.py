import mysql.connector
import bcrypt
from form import Question
from tests_list import ResultListing
import csv
class BackendStuff():
    def __init__(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="kyle",
            passwd="hello",
            database="projectorwhatever"
        )
        cursor = mydb.cursor()
        self.cursor = cursor
        self.mydb = mydb

    def validate_password(self, id: str,  password: str) -> bool:
        if id == 'admin':
            return bcrypt.checkpw(password.encode('utf-8'), '$2a$12$HHIQAhNqBMjQx68rei39h.TdNPYJpVEl9VadSQlHSP194K.dMVTDu'.encode('utf-8'))
        try:
            self.cursor.execute("SELECT password FROM students WHERE studentcode = %s", (int(id),))
            result = self.cursor.fetchall()
            if len(result) == 0: return False
            return bcrypt.checkpw(password.encode('utf-8'), result[0][0].encode('utf-8'))
        except ValueError:
            # called when id isn't an int
            return False

    def export_csv(self, testcode, filename, results):
        with open(filename, "w",newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Test code", "Student code", "Student name", "Score", "Total", "Percentage"])
            for result in results:
                writer.writerow([testcode, result.studentcode, result.testname, result.score, result.total, f"{100*result.score/result.total}%"])

    def get_test_details(self, testcode: int):

        self.cursor.execute("SELECT testname FROM tests WHERE testcode = %s", (testcode,))
        testname = self.cursor.fetchall()[0][0]
        self.cursor.execute("SELECT * FROM questions WHERE testcode = %s", (testcode,))
        questiontuples = self.cursor.fetchall()
        return testname,questiontuples

    def submit_test(self, testcode: int, sid: int, qcodes: list, choices: list, numcorrect: int):
        self.cursor.executemany(
            "INSERT INTO choices VALUES(%s, %s, %s, %s)",
            [(testcode, sid, questioncode, choice) for questioncode, choice in zip(qcodes, choices)]
        )
        self.cursor.execute("INSERT INTO scores VALUES (%s, %s, %s)", (sid, testcode, numcorrect))
        
        self.mydb.commit()

    def fetchtests(self, sid: int):
        self.cursor.execute(
            """SELECT tests.testcode, testname, COUNT(questioncode), timemin, subjects.name 
            FROM tests 
            JOIN subjects 
                ON tests.subjectcode = subjects.subjectcode
            JOIN questions
                ON tests.testcode = questions.testcode
            GROUP BY testcode
            ORDER BY testcode;
            """
        )
        tests= self.cursor.fetchall()
        self.cursor.execute("SELECT DISTINCT testcode FROM choices WHERE studentcode=%s", (sid,))
        attempted = [x[0] for x in self.cursor.fetchall()]

        return [(*test, test[0] in attempted) for test in tests]


    def fetchscores(self, sid: int):
        #testcode: int, testname: int, score:int
        self.cursor.execute(
            """SELECT tests.testcode, tests.testname, score, COUNT(questioncode), subjects.name
            FROM scores 
            INNER JOIN tests 
                ON scores.testcode = tests.testcode
            INNER JOIN subjects
                ON tests.subjectcode = subjects.subjectcode
            INNER JOIN questions
                ON tests.testcode = questions.testcode
            WHERE scores.studentcode = %s 
            GROUP BY testcode""", 
            (sid,)
        )
        return self.cursor.fetchall()

    def get_name(self, sid):
        self.cursor.execute("SELECT name FROM students WHERE studentcode = %s", (sid,))
        return self.cursor.fetchall()[0][0]

    def get_choices(self, testcode, studentcode, questioncodes):
        # executemany is undefined for select, so we need to perform one select and assemble the data ourselves
        self.cursor.execute(
            "SELECT choice,questioncode FROM choices WHERE testcode=%s AND studentcode=%s", 
            (testcode, studentcode)
        )
        resultdict = {x[1]: x[0] for x in self.cursor.fetchall()}
        return [resultdict[qcode] for qcode in questioncodes]

    def submit_test_creator(self, subjectcode, testcode, testname, questions):
        if testcode == 0:
            self.cursor.execute(
                "INSERT INTO tests VALUES (0, %s, %s, 15)", 
                (subjectcode, testname)
            )

            self.mydb.commit()
            # a valid testcode is needed to insert questions
            self.cursor.execute("SELECT LAST_INSERT_ID()")
            testcode = self.cursor.fetchall()[0][0]
        else:
            self.cursor.execute("UPDATE tests SET subjectcode = %s WHERE testcode = %s", (subjectcode, testcode))

        tuplesNew = []
        tuplesOld = []
        for q in questions:
            if q.qcode == 0:
                tuplesNew.append(
                (0, q.question, q.a, q.b, q.c, q.d, q.correct, testcode)
                )
            else:
                tuplesOld.append(
                ( q.question, q.a, q.b, q.c, q.d, q.correct, testcode, q.qcode,)
                )
        q: Question = None
        self.cursor.executemany(
            # qcode, question, a, b, c, d, correct, testcode
            "INSERT INTO questions VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            tuplesNew
        )

        self.mydb.commit()

        self.cursor.executemany(
            # qcode, question, a, b, c, d, correct, testcode
            "UPDATE questions SET question = %s, optiona = %s, optionb = %s, optionc = %s, optiond = %s, correctopt= %s, testcode = %s WHERE questioncode = %s",
            tuplesOld
        )
        self.mydb.commit()

    def get_subjects(self):
        self.cursor.execute("SELECT name, subjectcode FROM subjects;")
        return self.cursor.fetchall()

    def get_subject_code(self, testcode):
        self.cursor.execute("SELECT subjectcode FROM tests WHERE testcode = %s", (testcode,))
        return self.cursor.fetchall()[0][0]

    def get_graph(self, sid):
        self.cursor.execute(
            """SELECT ROUND(100*(score/(SELECT COUNT(questioncode) FROM questions WHERE questions.testcode = tests.testcode)) + 0e0, 2), testname FROM scores 
            JOIN tests ON scores.testcode = tests.testcode 
            WHERE studentcode = %s ORDER BY tests.testcode;""", (sid,))
        r= self.cursor.fetchall()
        return zip(*r) if len(r) > 0 else ([], [])

    def get_last_test(self, sid: int):
        #testcode: int, testname: int, score:int
        self.cursor.execute(
            """SELECT tests.testcode, tests.testname, score, COUNT(questioncode)
            FROM scores  
            INNER JOIN tests 
                ON scores.testcode = tests.testcode
            INNER JOIN subjects
                ON tests.subjectcode = subjects.subjectcode
            INNER JOIN questions
                ON tests.testcode = questions.testcode
            WHERE scores.studentcode = %s 
            GROUP BY tests.testcode
            ORDER BY tests.testcode DESC
            LIMIT 1;""", 
            (sid,)
        )
        r = self.cursor.fetchall()
        return r[0] if len(r) > 0 else None

    def get_avgs(self, sid: int):
        # query from hell
        self.cursor.execute(""" 
        SELECT subjects.name, AVG(SCORE/(SELECT COUNT(*) FROM questions WHERE questions.testcode = tests.testcode)) 
        FROM scores 
        JOIN tests ON tests.testcode = scores.testcode
        JOIN subjects ON tests.subjectcode = subjects.subjectcode 
        WHERE studentcode = %s GROUP BY tests.subjectcode;""", (sid,))
        subjects = self.cursor.fetchall()
        overall = sum([x[1] for x in subjects])/(len([x[1] for x in subjects]) or 1)
        return overall, subjects

    def get_test_scores(self, testcode: int):
        #(self, sid, name, score, total)
        testname, _ = self.get_test_details(testcode)
        self.cursor.execute("""
        SELECT testcode, students.name, score, (SELECT COUNT(questioncode) FROM questions WHERE questions.testcode = scores.testcode), scores.studentcode
        FROM scores
        JOIN students ON scores.studentcode = students.studentcode
        WHERE scores.testcode = %s
        """, (testcode,))

        results = []
        for r in self.cursor.fetchall():
            t= ResultListing(*(r[:-1]), '')
            results.append(t)
            t.studentcode = r[-1]

        return testname, results
