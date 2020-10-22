-- TABLE
CREATE TABLE classes(
id INTEGER PRIMARY KEY,
teacher_id INTEGER,
name TEXT,
FOREIGN KEY(teacher_id) REFERENCES people(id)
);
CREATE TABLE people(
id INTEGER PRIMARY KEY,
isTeacher INTEGER,
username TEXT,
password TEXT,
name TEXT,
email TEXT
);
CREATE TABLE questions(
id INTEGER PRIMARY KEY,
correct_answer INTEGER,
topic_id INTEGER,
question_text BLOB,
a_answer_text BLOB,
b_answer_text BLOB,
c_answer_text BLOB,
d_answer_text BLOB, quiz_id INTEGER,
FOREIGN KEY(topic_id) REFERENCES topics(id)
);
CREATE TABLE quiz_grades(
id INTEGER PRIMARY KEY,
student_id integer,
quiz_id INTEGER,
grade REAL,
FOREIGN KEY(student_id) REFERENCES people(id),
FOREIGN KEY(quiz_id) REFERENCES quizzes(id)
);
CREATE TABLE quizzes(
id INTEGER PRIMARY KEY,
topic_id INTEGER,
creator_id INTEGER,
class_id INTEGER, name text,
FOREIGN KEY(topic_id) REFERENCES topics(id),
FOREIGN KEY(creator_id) REFERENCES people(id),
FOREIGN KEY(class_id) REFERENCES classes(id)
);
CREATE TABLE roster(
id INTEGER PRIMARY KEY,
people_id INTEGER,
class_id INTEGER,
FOREIGN KEY (people_id) REFERENCES people(id),
FOREIGN KEY (class_id) REFERENCES classes(id)
);
CREATE TABLE topics(
id INTEGER PRIMARY KEY,
class_id INTEGER,
name TEXT,
FOREIGN KEY(class_id) REFERENCES classes(id)
);
 
-- INDEX
 
-- TRIGGER
 
-- VIEW
 
