import sqlite3
import datetime
import bcrypt
from manager import *
from login_page import *
from add_section import *
from edit_competency import *

connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()


def edit_user_info():
    choice = ''
    while choice.upper() != 'E':
        choice = input(f'''
            -----------------------------------------------
            -----------------------------------------------
            |                                             |
            |            Competency Tracker Tool          |
            |      Choose from the following options      |
            |                                             |
            |        *** Edit User Information ***        |
            |          (Student/Manager Portal)           |
            |                                             |
            |   [A] Update phone number                   |
            |   [B] Change password                       |
            |   [C] Update email address                  |
            |   [D] Change last name                      |
            |   [E] View assessment results               |
            |                                             |
            |      *** Edit Testing Information ***       |
            |              (Managers Portal)              |
            |                                             |
            |   [F] Edit a competency, assessment         |
            |        score, change test date, or          |
            |        change manager                       |
            |   [G] Edit an assessment's due date         |
            |                                             |
            |   [H] Return to previous menu               |
            |                                             |
            -----------------------------------------------
            -----------------------------------------------
\n''')

        if choice.upper() == 'A':
            first_last_name_print()
            replacement_var = 'phone'
            var_name_change = 'phone number'
            user_update_sql(var_name_change,replacement_var)

        elif choice.upper() == 'B':
            first_last_name_print()
            replacement_var = 'password'
            var_name_change = 'password'
            user_update_sql(var_name_change,replacement_var)
            
        elif choice.upper() == 'C':
            first_last_name_print()
            replacement_var = 'email'
            var_name_change = 'email address'
            user_update_sql(var_name_change,replacement_var)
            
        elif choice.upper() == 'D':
            first_last_name_print()
            replacement_var = 'last_name'
            var_name_change = 'last name'
            user_update_sql(var_name_change,replacement_var)

        elif choice.upper() == 'E'and user_type == ['manager'] or user_type == ['student']:
            assessment_preview(user_type)

        elif choice.upper() == 'F'and user_type == ['manager']:
            edit_assessment()

        elif choice.upper() == 'G'and user_type == ['manager']:
            assessment_changes()
            
        elif choice.upper() == 'H':
            break
        
        elif choice.upper() == 'E' or 'F' or 'H' and user_type != ['manager']:
            managers_only_print()

        else:
            print('Invalid Selection')

def assessment_changes():
    print('Update Assessment')
    rows = cursor.execute('''SELECT assessment_id, due_date, creation_date, competency_id FROM Assessments''').fetchall()
    print(f'\n{"Assessment ID    Due Date              Date Created           Competency ID"}\n')
    for row in rows:  
        print(f'{row[0]:<16}{row[1]:<23}{row[2]:<23}{row[3]}')
    assessment_id = input("\nEnter an assessment ID: ")
    due_date = input("Enter the updated due date: ")
    competency_id = input("Enter a competency ID: ")
    update_active = (f"UPDATE Assessments SET due_date = ? WHERE assessment_id = ? and competency_id = ?")
    update_values = (due_date,assessment_id,competency_id)
    cursor.execute(update_active, update_values)
    connection.commit()
    print('Success!')
# assessment_changes()

def managers_only_print():
    print(f'''
    ╔═════════════════════════════════════════════════════════════╗
    ║                                                             ║ 
    ║     Only managers can accesses this area of the program     ║
    ║                                                             ║
    ╚═════════════════════════════════════════════════════════════╝''')

def first_last_name_print():
    rows = cursor.execute("SELECT user_id, first_name, last_name From Users").fetchall()
    print('      ID   First Name       Last Name\n')
    for row in rows:
        print(f'''      {row[0]}    {row[1]:<17}{row[2]:<23}''')

def user_update_sql(var_name_change, replacement_var):
    user_input = input(f"\nEnter a User ID: ")
    person_info = cursor.execute(f"SELECT first_name, last_name, {replacement_var} FROM Users WHERE user_id = ?", (user_input)).fetchone()
    if var_name_change == 'password':
        pass
    else:
        print(f'Your current {var_name_change} is: {person_info[2]}')
    new_values = input(f"Enter your updated {var_name_change}: ")
    if var_name_change == 'password':
        new_values = bcrypt.hashpw(new_values.encode("utf-8"), bcrypt.gensalt())
    update_active = (f"UPDATE Users SET {replacement_var} = ? WHERE user_id = ?")
    update_values = (new_values,user_input)
    cursor.execute(update_active, update_values)
    connection.commit()
    person_name = cursor.execute("SELECT first_name, last_name FROM Users WHERE user_id = ?", (user_input)).fetchone()
    print(f'The changes to {person_name[0]} {person_name[1]}\'s {var_name_change} have been saved.')

def main_menu():
    choice = ''
    while choice.upper() != 'Q':
        choice = input('''
            -----------------------------------------------
            -----------------------------------------------
            |            Competency Tracker Tool          |
            |                  MAIN MENU                  |
            |                                             |
            |           *** Student Portal ***            |
            |                                             |
            |       [1] EDIT information                  |
            |           VIEW assessment results           |
            |                                             |
            |           *** Manager's Portal ***          |
            |                                             |
            |       [2] ADD/DELETE                        |
            |       [3] VIEW student information          |
            |           SEARCH for students               |
            |                                             |
            |       [Q] To logout of the program          |
            |                                             |
            -----------------------------------------------
            -----------------------------------------------
        ''')

        if choice == '1':
            edit_user_info()

        elif choice == '2' or '3' and user_type == ['student']:
            managers_only_print()

        elif choice == '2' and user_type == ['manager']:
            add_info()
        
        elif choice == '3' and user_type == ['manager']:
            view_menu()

        elif choice.upper() == 'Q':
            print('Goodbye')

        else:
            print('Invalid selection, please try again.')

main_menu()