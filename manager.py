import csv
import sqlite3
from create_csv import *

connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()



def view_all_users():
    rows = cursor.execute('''SELECT * FROM Users''').fetchall()
    print(f'\n{"ID  First Name  Last Name        Phone       Email                  Password      A.   Date Created          Hire Date             User Type"}\n')
    for row in rows:  
        print(f'{row[0]!s:<4}{row[1]!s:<12}{row[2]!s:<17}{row[3]!s:<12}{row[4]!s:<23}{row[5]!s:<14}{row[6]!s:<5}{row[7]!s:<22}{row[8]!s:<22}{row[9]!s:<14}')
# # view_all_users()

def view_search():
    has_results = False
    name_search = input("Enter a LAST NAME to search the database: ")
    name_results = cursor.execute("SELECT * FROM Users WHERE last_name like ?", (f'%{name_search}%',)).fetchall()
    for row in name_results:
        has_results = True
        print(f'''
User ID: {row[0]} 
First Name: {row[1]}
Last Name: {row[2]}       
Phone: {row[3]}      
Email: {row[4]}                
Password: {row[5]}   
Active:{row[6]}   
Date Created: {row[7]}         
Hire Date: {row[8]}            
User Type: {row[9]}\n''')

    if has_results == False:
        print(f"\nNo user with the last name {name_search} was not found in the database.")
# view_search()

def sql_join(sql_finished,checkpoint):
    global competencies
    # global checkpoint
    competencies = cursor.execute(f'''
    Select Users.user_id, Users.first_name, Users.last_name, Assessment_Results.score, 
    Competencies.competency_name, Assessment_Results.score_notes, Assessments.assessment_id, Assessments.due_date
    FROM Users JOIN Assessment_Results ON Users.user_id = Assessment_Results.user_id
    JOIN  Assessments ON Assessment_Results.assessment_id = Assessments.assessment_id
    JOIN Competencies  ON Assessments.competency_id = Competencies.competency_id {sql_finished}
    ''').fetchall()
    if checkpoint == True:
        pass 
    else:
        print('\nID   First Name    Last Name     Score Competency Name     Score Notes\n')
        for row in competencies:
            print(f'{row[0]!s:<5}{row[1]!s:<14}{row[2]!s:<14}{row[3]!s:<7}{row[4]!s:<19}{row[5]!s}')
    return competencies
    
    
def view_user_competencies():
    checkpoint = False
    print('Competencies levels by user...')
    sql_finished = 'ORDER BY Users.user_id'
    sql_join(sql_finished, checkpoint)
# view_user_competencies()

def user_sql():
    rows = cursor.execute('''SELECT * FROM Users''').fetchall()
    print(f'\n{"ID  First Name  Last Name"}\n')
    for row in rows:  
        print(f'{row[0]!s:<4}{row[1]!s:<12}{row[2]!s:<17}')
# user_sql()      

def view_all_competency():
    user_sql()
    checkpoint = False
    print('\nIndividual Competency Report...')
    user_input = input('Enter a User ID: ')
    sql_finished = f"WHERE Users.user_id = '{user_input}'"
    sql_join(sql_finished,checkpoint)
# view_all_competency()

def view_assessments():
    # global check_point
    user_sql()
    checkpoint = True
    user_input = input('Enter a User ID: ')
    sql_finished = f"WHERE Users.user_id = '{user_input}'"
    sql_join(sql_finished,checkpoint)
    print('\nAssessment report...')
    print('\nU.ID   First Name    Last Name     Score   Competency Name     Score Notes              Due Date              A.ID\n')
    for row in competencies:
        print(f'{row[0]!s:<7}{row[1]!s:<14}{row[2]!s:<14}{row[3]!s:8}{row[4]!s:<20}{row[5]!s:<25}{row[7]!s:<22}{row[6]!s}')
# view_assessments()

def view_menu():
    choice = ''
    while choice.upper != '4':

        choice = input('''
            -----------------------------------------------
            -----------------------------------------------
            |                                             |
            |            Competency Tracker Tool          |
            |       Pick from the following options:      |
            |                                             |
            |           *** Viewing Portal ***            |
            |                                             |
            |       [1] View all users information        |
            |       [2] Search for users                  |
            |       [3] Report of users and their         |
            |           competency levels/                |
            |           Write data to CSV file            |
            |       [4] Individual competency report/     |
            |           Write data to CSV file            |
            |       [5] Individual assessment report/     |
            |           To see CSV import data            |
            |                                             |
            |       [6] Return to main menu               |
            |                                             |
            -----------------------------------------------
            ----------------------------------------------- ''')

        if choice == '1':
            view_all_users() 

        elif choice == '2':
            view_search()

        elif choice == '3':
            view_user_competencies()
            create_data()

        elif choice == '4':
            view_all_competency()
            person_data()

        elif choice == '5':
            view_assessments()
            csv_file = input('Would you like to see the csv imported file? Y/N: ') 
            if csv_file.upper() == 'N':
                pass
            elif csv_file.upper() == 'Y':
                csv_import()
            else:
                print('Invalid Input')
        
        elif choice == '6':
            break

        else:
            print('Invalid Selection')

# view_menu()