import sqlite3
import bcrypt

connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
    user_id	INTEGER,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    active INTEGER DEFAULT 1,
    date_created TEXT,
    hire_date TEXT,
    user_type TEXT NOT NULL,
    PRIMARY KEY(user_id AUTOINCREMENT)
);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Competencies (
    competency_id INTEGER,
    competency_name	TEXT NOT NULL UNIQUE,
    competency_description TEXT,
    PRIMARY KEY(competency_id)
);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Assessments (
    assessment_id INTEGER,
    due_date TEXT,
    creation_date TEXT,
    competency_id INTEGER,
    PRIMARY KEY(assessment_id AUTOINCREMENT),
    FOREIGN KEY(competency_id) REFERENCES Competencies (competency_id)
);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Assessment_Results (
    result_id INTEGER,
    user_id	INTEGER NOT NULL,
    assessment_id INTEGER NOT NULL,
    score INTEGER DEFAULT 0,
    assessment_date	TEXT,
    manager_id INTEGER,
    score_notes	TEXT,
    PRIMARY KEY(result_id AUTOINCREMENT),
    FOREIGN KEY(assessment_id) REFERENCES Assessments(assessment_id),
    FOREIGN KEY(user_id) REFERENCES Users(user_id),
    FOREIGN KEY(manager_id) REFERENCES Users(user_id)
);''')


password = '1234'
hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

users = [
    ('MollyKate','Greenhalgh',4357609627,'mkg@gmail.com',f'{hashed_password}','2021-12-07 16:50:20','2021-12-07 16:50:20','manager'),
    ('Lily','Rayback',4359999890,'lily@gmail.com',f'{hashed_password}','2021-12-07 16:50:20','2021-12-07 16:50:20','manager'),
    ('Michael','Greenhalgh',7196517906,'michael@yahoo.com',f'{hashed_password}','2021-12-07 16:50:20','2021-12-07 16:50:20','student'),
    ('Rachel','Taylor',8013458276,'rachel@gmail.com',f'{hashed_password}','2021-12-07 16:50:20','2021-12-07 16:50:20','manager'),
    ('Mark','Taylor',7953721234,'mark@gmail.com',f'{hashed_password}','2021-12-07 16:50:20','2021-12-07 16:50:20','student'),
    ('Benjamin','Cox',8016453782,'benjamin@yahoo.com',f'{hashed_password}','2021-12-07 16:50:20','2021-12-07 16:50:20','student'),
    ('Reuben','Greenhalgh',3863983627,'reuben@gmail.com',f'{hashed_password}','2021-12-07 16:50:20','2021-12-07 16:50:20','student'),
    ('Marissa','Popham',4357608421,'marissa@gmail.com',f'{hashed_password}','2021-12-07 16:50:20','2021-12-07 16:50:20','student')
]

insert_sql = "INSERT INTO Users (first_name,last_name,phone,email,password,date_created,hire_date,user_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

for data in users:
    cursor.execute(insert_sql, data)

connection.commit() 



competencies = [
    ('Data Types','Good stuff to know'),
    ('Variables','Good stuff to know'),
    ('Functions','Good stuff to know'),
    ('Boolean Logic','Good stuff to know'),
    ('Conditionals','Good stuff to know'),
    ('Loops','Good stuff to know'),
    ('Data Structures','Good stuff to know'),
    ('Lists','Good stuff to know'),
    ('Dictionaries','Good stuff to know'),
    ('Working with Files','Good stuff to know'),
    ('Exception Handling','Good stuff to know'),
    ('Quality Assurance (QA)','Good stuff to know'),
    ('Object-Oriented Programming','Good stuff to know'),
    ('Recursion','Good stuff to know'),
    ('Databases','Good stuff to know')
]

insert_sql = "INSERT INTO Competencies (competency_name, competency_description) VALUES (?,?)"

for data in competencies:
    cursor.execute(insert_sql, data)

connection.commit() 



assessments = [
    ('2021-12-07 23:00:00','2021-12-07 17:00:27',1),
    ('2021-12-07 23:00:00','2021-12-07 17:00:27',2),
    ('2021-12-07 23:00:00','2021-12-07 17:00:27',3),
    ('2021-12-07 23:00:00','2021-12-07 17:00:27',4),
    ('2021-12-07 23:00:00','2021-12-07 17:00:27',5),
    ('2021-12-07 23:00:00','2021-12-07 17:00:27',6),
    ('2021-12-07 23:00:00','2021-12-07 17:00:27',7),
    ('2021-12-07 23:00:00','2021-12-07 17:00:27',8),
    ('2021-12-07 23:00:00','2021-12-07 17:00:27',9),
    ('2021-12-07 23:00:00','2021-12-07 17:00:27',10),
    ('2021-12-07 23:00:00','2021-12-07 17:00:27',11),
    ('2021-12-07 23:00:00','2021-12-07 17:00:27',12),
    ('2021-12-07 23:00:00','2021-12-07 17:00:27',13),
    ('2021-12-07 23:00:00','2021-12-07 17:00:27',14),
    ('2021-12-07 23:00:00','2021-12-07 17:00:27',15)
]

insert_sql = "INSERT INTO Assessments (due_date, creation_date, competency_id) VALUES (?, ?, ?)"
for data in assessments:
    cursor.execute(insert_sql, data)

connection.commit() 


assessment_results = [
    (1,8,'2021-12-08 23:00:00',1,'No competency'),
    (2,7,'2021-12-08 23:00:00',1,'No competency'),
    (3,6,'2021-12-08 23:00:00',1,'No competency'),
    (4,5,'2021-12-08 23:00:00',1,'No competency'),
    (5,4,'2021-12-08 23:00:00',2,'No competency'),
    (6,3,'2021-12-08 23:00:00',2,'No competency'),
    (7,2,'2021-12-08 23:00:00',2,'No competency'),
    (8,1,'2021-12-08 23:00:00',2,'No competency')
]

insert_sql = "INSERT INTO Assessment_Results (user_id, assessment_id, assessment_date, manager_id,score_notes) VALUES (?, ?, ?, ?,?)"
for data in assessment_results:
    cursor.execute(insert_sql, data)

connection.commit() 

