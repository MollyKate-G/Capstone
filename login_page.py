import sqlite3

connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()

# manager
# email = 'mkg@gmail.com'
# password = '1234'

# student
# email = 'mark@gmail.com'
# password = '1234'

email = input("Enter your email: ")
password = input("Enter your password: ")

user_type = []
check_login = True

def login_user(email, password, check_login):
  row = cursor.execute('SELECT user_id, user_type FROM Users WHERE email = ?', (email,)).fetchone()
  user_type.append(row[1])
  user_id = row[0]
  
  if check_login == True:
    print(f'''
  .--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--.
/ .. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \\
\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/ /
 \/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /
 / /\/ /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /\/ /\\
/ /\ \/`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\ \/\ \\
\ \/\ \                                                    /\ \/ /
 \/ /\ \                  Welcome to the                  / /\\/ /
 / /\/ /             Competency Tracker Tool              \ \/ /\\
/ /\ \/      your information has been entered below       \ \/\ \\
\ \/\ \                                                    /\ \/ /
 \/ /\ \                      LOGIN                       / /\/ /
 / /\/ /                                                  \ \/ /\\
/ /\ \/       Email: {email}                         \ \/\ \\
\ \/\ \              ----------------------------------    /\ \/ /
 \/ /\ \   Password: {password}                           / /\/ /
 / /\/ /             ----------------------------------   \ \/ /\\
/ /\ \/                                                    \ \/\ \\
\ \/\ \.--..--..--..--..--..--..--..--..--..--..--..--..--./\ \/ /
 \/ /\/ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ /\/ /
 / /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\\
/ /\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \\
\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `' /
 `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'
 ''')
  else:
    pass
  return user_id
login_user(email, password, check_login)
