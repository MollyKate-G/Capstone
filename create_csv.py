import csv
import sqlite3


connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()

fields = ['User ID', 'First Name', 'Last Name', 'Score', 'Competency Name', 'Score Note', 'Assessment ID', 'Due Date',]

def create_data():
    with open('comp_users.csv', 'w', newline='') as outfile:
        competencies = cursor.execute(f'''
    Select Users.user_id, Users.first_name, Users.last_name, Assessment_Results.score, 
    Competencies.competency_name, Assessment_Results.score_notes, Assessments.assessment_id, Assessments.due_date
    FROM Users JOIN Assessment_Results ON Users.user_id = Assessment_Results.user_id
    JOIN  Assessments ON Assessment_Results.assessment_id = Assessments.assessment_id
    JOIN Competencies  ON Assessments.competency_id = Competencies.competency_id ORDER BY Users.user_id
    ''').fetchall()
        wrt = csv.writer(outfile)
        wrt.writerow(fields)
        wrt.writerows(competencies)
# create_data()

data = ['ID','First Name','Last Name','Score', 'Competency Name','Score Notes', 'Assessment_id', 'Due Date']
def person_data():
    with open('comp_individual.csv', 'w', newline='') as outfile:
        user_input = input('Enter the User ID again to write it to a csv file: ')
        competencies = cursor.execute(f'''
    Select Users.user_id, Users.first_name, Users.last_name, Assessment_Results.score, 
    Competencies.competency_name, Assessment_Results.score_notes, Assessments.assessment_id, Assessments.due_date
    FROM Users JOIN Assessment_Results ON Users.user_id = Assessment_Results.user_id
    JOIN  Assessments ON Assessment_Results.assessment_id = Assessments.assessment_id
    JOIN Competencies  ON Assessments.competency_id = Competencies.competency_id Where Users.user_id = ?
    ''',(user_input,)).fetchall()
        wrt = csv.writer(outfile)
        wrt.writerow(data)
        wrt.writerows(competencies)
# person_data()

def csv_import():
    with open('comp_individual.csv', 'r') as csvfile:
        results = []
        for line in csvfile:
            words = line.split(',')
            results.append((words[0], words[1:]))
    print(f'{results}')  
# csv_import()