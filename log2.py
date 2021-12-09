import sqlite3

connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()

# email = 'mkg@gmail.com'
# password = '1234lsdf'

email = 'lily@gmail.com'
password = 'aslf3'

user_type = []

def login_user(email, password):
  row = cursor.execute('SELECT user_id, user_type FROM Users WHERE email = ?', (email,)).fetchone()
  user_type.append(row[1])
  user_id = row[0]
  
  if email and password == None:

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
login_user(email, password)
print(user_type)