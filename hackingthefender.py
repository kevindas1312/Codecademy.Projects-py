import csv
import json as js
compromised_users = []
with open('passwords.csv') as password_file:
  password_file = csv.DictReader(password_file)
  for item in password_file:
    compromised_users.append(item['Username'])

with open('compromised_users.txt', 'w') as compromised_user_file:
  compromised_user_file.write("\n".join(compromised_users))

with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {"recipient" : "The Boss", "message" : "Mission Success"}
  js.dump(boss_message_dict,boss_message)

fields = ["line"]

with open("passwords.csv", "w") as new_passwords_obj:
    writer = csv.DictWriter(new_passwords_obj, fieldnames=fields)
    writer.writeheader()

    signature = """ _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/"""  # your block here
    for line in signature.splitlines():
        writer.writerow({"line": line})
