import sqlite3
import datetime


connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()


def add_assessment_results():
    print('Create an assessment result...\n')
    user_id = input('Enter a User ID:')
    assessment_id = input('Enter an Assessment ID:')
    score = input('Enter a score, (0-4):')
    manager_id = input('Enter a Manager ID:')

    insert_sql = '''INSERT INTO Assessment_Results (user_id, assessment_id, score, manager_id) VALUES (?,?,?,?)'''
    cursor.execute(insert_sql, (user_id, assessment_id, score, manager_id,))
    connection.commit() 
    print('Success!')
# add_assessment_results()

def add_user():
    print('Add a new user...\n')
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    phone = input('Phone Number: ')
    email = input('Email Address: ')
    password = input('Password: ')
    active = input('Active Status, (1 = Active, 0 = Inactive): ')
    dt = datetime.datetime.now()
    date_created = dt.replace(microsecond=0)
    hire_date = input('Hire Date: ')
    user_type = input('User Type, (manager/student): ')

    insert_sql = '''INSERT INTO Users (first_name,last_name,phone,email,password,active,date_created,hire_date,user_type) VALUES (?,?,?,?,?,?,?,?,?)'''
    cursor.execute(insert_sql,(first_name,last_name,phone,email,password,active,date_created,hire_date,user_type,))
    connection.commit() 
    print('Success!')
# add_user()

def add_competency():
    print('Create a new competency...\n')
    competency_name	= input('Competency Name: ')
    competency_description = input('Enter a competency description: ')
    insert_sql = '''INSERT INTO competencies (competency_name, competency_description) VALUES (?,?)'''
    cursor.execute(insert_sql,(competency_name,competency_description,))
    connection.commit() 
    print('Success!')
# add_competency()

def assessment_to_competency():
    print('Add an assessment to a competency...\n')
    due_date = '2022-05-07 23:59:00'
    dt = datetime.datetime.now()
    creation_date = dt.replace(microsecond=0)
    competency_id = input('Enter a competency_id: ')
    insert_sql = '''INSERT INTO Assessments (due_date, creation_date, competency_id) VALUES (?,?,?)'''
    cursor.execute(insert_sql,(due_date, creation_date, competency_id,))
    connection.commit() 
    print('Success!')
# assessment_to_competency()

def delete_data():
    print('Delete an assessment result...\n')
    has_results = False
    result_id = input('Enter a Result ID: ')
    delete_check = input(f'Are you sure you want to delete result {result_id}? Y/N')
    if delete_check.upper() == 'Y':
        rows = cursor.execute("Select result_id FROM Assessment_Results WHERE result_id = ?", (result_id,)).fetchone()
        if rows:
            has_results = True 
            rows = cursor.execute("DELETE FROM Assessment_Results WHERE result_id = ?", (result_id,)).fetchone()
            connection.commit()
            print(f'Result {result_id} has been deleted')
        else:
            print(f'No record found for Result ID {result_id} ')
    elif delete_check.upper() == 'N':
        print('Good choice!')
    else:
        print('Invalid Input')
# delete_data()

def add_info():
    choice = ''
    while choice.upper() != 'E':
        choice = input(f'''
            -----------------------------------------------
            -----------------------------------------------
            |                                             |
            |            Competency Tracker Tool          |
            |      Choose from the following options      |
            |                                             |
            |              Add Information                |
            |                     &                       |  
            |          Delete Assessment Results          |
            |                                             |
            |   [A] Add a new user                        |
            |   [B] Add a new competency                  |
            |   [C] Add a new assessment to a             |
            |       competency                            |
            |   [D] Add a new assessment result           |
            |       for a user                            |
            |                                             |
            |   [E] Delete Assessment Results             |
            |                                             |  
            |   [F] Return to main menu                   |
            |                                             |
            -----------------------------------------------
            -----------------------------------------------
\n''')

        if choice.upper() == 'A':
            add_user()

        if choice.upper() == 'B':
            add_competency()

        if choice.upper() == 'C':
            assessment_to_competency()

        if choice.upper() == 'D':
            add_assessment_results()

        if choice.upper() == 'E':
            delete_data()

        if choice.upper() == 'F':
            break
# add_info()