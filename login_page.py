import sqlite3

connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()

# email = 'mkg@gmail.com'
# password = '1234'

# email = 'lily@gmail.com'
# password = '1234'
email = input("Enter your email: ")
password = input("Enter your password: ")

def password_check(email, password):
  try:
    password = bcrypt.hashpw(password.encode('utf-8'), check_value[0])
    check_value = cursor.execute("SELECT password FROM Users WHERE email = ?", (email,)).fetchone()
    password == check_value[0]
    print(True)
  except:
    print(False)

password_check(email, password)
user_type = []

def login_user():
  row = cursor.execute("""SELECT user_id, email, password, user_type FROM Users WHERE email = ? 
                          AND password = ?""", (email, password,)).fetchone()
  user_type.append(row[3])
  user_id = row[0]
  # if email and password == None:

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

  return user_id
# login_user()

