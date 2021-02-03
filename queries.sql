-- password verification
SELECT password FROM students WHERE studentcode = %s

-- get test details
SELECT testname FROM tests WHERE testcode = %s
SELECT * FROM questions WHERE testcode = %s

-- submit tests
INSERT INTO choices VALUES(%s, %s, %s, %s)
INSERT INTO scores VALUES (%s, %s, %s)

-- fetch tests
SELECT tests.testcode, testname, COUNT(questioncode), timemin, subjects.name 
FROM tests 
JOIN subjects 
	ON tests.subjectcode = subjects.subjectcode
JOIN questions
	ON tests.testcode = questions.testcode
GROUP BY testcode
ORDER BY testcode;

SELECT DISTINCT testcode FROM choices WHERE studentcode=%s

-- fetch scores
SELECT tests.testcode, tests.testname, score, COUNT(questioncode), subjects.name
FROM scores 
INNER JOIN tests 
	ON scores.testcode = tests.testcode
INNER JOIN subjects
	ON tests.subjectcode = subjects.subjectcode
INNER JOIN questions
	ON tests.testcode = questions.testcode
WHERE scores.studentcode = %s 
GROUP BY testcode

-- get name
SELECT name FROM students WHERE studentcode = %s

-- get choices
SELECT choice,questioncode FROM choices WHERE testcode=%s AND studentcode=%s

-- create test
INSERT INTO tests VALUES (0, %s, %s, 15)
SELECT LAST_INSERT_ID()
UPDATE tests SET subjectcode = %s WHERE testcode = %s
INSERT INTO questions VALUES (%s, %s, %s, %s, %s, %s, %s, %s)

UPDATE questions SET question = %s, optiona = %s, optionb = %s, optionc = %s, optiond = %s, correctopt= %s, testcode = %s WHERE questioncode = %s

-- get subjects
SELECT name, subjectcode FROM subjects;

-- get subject code
SELECT subjectcode FROM tests WHERE testcode = %s

-- get graph data 
SELECT ROUND(100*(score/(SELECT COUNT(questioncode) FROM questions WHERE questions.testcode = tests.testcode)) + 0e0, 2), testname FROM scores 
JOIN tests ON scores.testcode = tests.testcode 
WHERE studentcode = %s ORDER BY tests.testcode;

-- get last test details
SELECT tests.testcode, tests.testname, score, COUNT(questioncode)
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
LIMIT 1;

-- get averages
SELECT subjects.name, AVG(SCORE/(SELECT COUNT(*) FROM questions WHERE questions.testcode = tests.testcode)) 
FROM scores 
JOIN tests ON tests.testcode = scores.testcode
JOIN subjects ON tests.subjectcode = subjects.subjectcode 
WHERE studentcode = %s GROUP BY tests.subjectcode;

-- get test scores
SELECT testcode, students.name, score, (SELECT COUNT(questioncode) FROM questions WHERE questions.testcode = scores.testcode), scores.studentcode
FROM scores
JOIN students ON scores.studentcode = students.studentcode
WHERE scores.testcode = %s


