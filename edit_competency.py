import sqlite3
import datetime
from login_page import *


connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()


def get_manager():
    rows = cursor.execute("""SELECT user_id, first_name, last_name, user_type FROM Users WHERE user_type like '%manager%'""").fetchall()
    print('''
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║ ''')     
    print(f'\n{"*** List of Managers ***":^65}\n')                                                         
    print(f'''
            User: ID   |   First Name   |   Last Name\n''')  
    for row in rows:
        print(f'''            {row[0]:<15}{row[1]:<17}{row[2]}''')
    print('''
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝''')


def assessment_preview(user_type):
    has_results = False
    if user_type == ['manager']:
        # user_id = login_user(email, password)
        print(f'\n{"********** Assessment Results **********":^86}\n')
        rows = cursor.execute('''SELECT result_id, user_id, assessment_id, score, assessment_date, manager_id, 
                                 score_notes FROM Assessment_Results''').fetchall()
        print(f'{"Result: ID   User: ID   Assessment: ID   Score   Assessment Date        Manager: ID   Score Notes"}\n')
        for row in rows:  
            has_results = True
            print(f'{row[0]!s:<13}{row[1]!s:<11}{row[2]!s:<17}{row[3]!s:<8}{row[4]!s:<23}{row[5]!s:<14}{row[6]!s}')
    elif user_type == ['student']:
        # user_id = login_user(email, password)
        rows = cursor.execute('''SELECT result_id, user_id, assessment_id, score, assessment_date, manager_id, score_notes 
                                 FROM Assessment_Results WHERE user_id = ?''', (user_id,)).fetchall()
        if rows:
            has_results = True 
            print(f'\n{"********** Assessment Results **********":^86}\n')
            print(f'{"Result: ID   User: ID   Assessment: ID   Score   Assessment Date        Manager: ID   Score Notes"}\n')
            for row in rows:
                print(f'{row[0]!s:<13}{row[1]!s:<11}{row[2]!s:<17}{row[3]!s:<8}{row[4]!s:<23}{row[5]!s:<14}{row[6]!s}')
        else:
            print('No records found')
    return has_results
# assessment_preview(user_type)   


def assessment_edits(the_edit,the_column):
    result_id = input('Enter a Result ID: ')
    update_active = f"UPDATE Assessment_Results SET {the_column} = ? WHERE result_id = ?;"
    update_values = (the_edit, result_id)
    cursor.execute(update_active, update_values)
    connection.commit()
    print('Success!')
    return result_id

def edit_assessment():
    choice = ''
    while choice.upper != '4':

        choice = input('''
            -----------------------------------------------
            -----------------------------------------------
            |                                             |
            |            Competency Tracker Tool          |
            |       Pick from the following options:      |
            |                                             |
            |           *** Manager Portal ***            |
            |                                             |
            |       [1] Edit assessment score             |
            |       [2] Change Test Date                  |
            |       [3] Change Manager                    |
            |                                             |
            |       [4] Return to main menu               |
            |                                             |
            -----------------------------------------------
            ----------------------------------------------- ''')
        # login_user = 'manager'
    
        if choice == '1':
            has_results = assessment_preview(user_type)
            if has_results:
                result_id = assessment_preview(user_type)
                the_edit = input('Enter the updated score (0-4): ')
                the_column = 'score'  
                if the_edit == '0':
                    score_notes = 'No competency'
                if the_edit == '1':
                    score_notes = 'Basic Competency'
                elif the_edit == '2':
                    score_notes = 'Intermediate Competency'
                elif the_edit == '3':
                    score_notes = 'Advanced Competency'
                elif the_edit == '4':
                    score_notes = 'Expert Competency'
                result_id = assessment_edits(the_edit,the_column)
                update_active = f"UPDATE Assessment_Results SET score_notes = ? WHERE result_id = ?;"
                update_values = (score_notes, result_id)
                cursor.execute(update_active, update_values)
                connection.commit()

        elif choice == '2':  
            autofill = input('Would you like to autofill today\'s date? Y/N: ')
            if autofill.upper() == 'Y':
                assessment_preview(user_type)
                dt = datetime.datetime.now()
                todays_date = dt.replace(microsecond=0)
                the_edit = todays_date
                the_column = 'assessment_date'
                assessment_edits(the_edit,the_column)
            elif autofill.upper() == 'N':
                assessment_preview(user_type)
                the_edit = input('Change date to: ')
                the_column = 'assessment_date'
                assessment_edits(the_edit,the_column)
            else:
                print('Invalid Selection')

        elif choice == '3':
            get_manager()
            assessment_preview(user_type)
            the_edit = input('Enter a Manager ID: ')
            the_column = 'manager_id'
            assessment_edits(the_edit,the_column)

        elif choice == '4':
            break

        else:
            print('Invalid Selection')

# edit_assessment()