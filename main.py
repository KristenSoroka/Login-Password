user_name = 'Kristen'
user_password = 'password1'

name_input = input("Please enter your user ID (case sensitive):  ")
password_input = input("Please enter your password (case sensitive):  ")

attempts = 0
max_attempts = 3

while attempts < max_attempts:
  
  if user_name == name_input and user_password == password_input:
    print(f"Welcome, {user_name}!")
  else:
    attempts += 1
    attempts_left = max_attempts - attempts
    if attempts_left == 0:
      print("You must wait 15 minutes for your account to reset before signing in again.")
    else:
      print(f"Username and/or password incorrect.  You have {attempts_left} left!")

      name_input = input("Please enter your user ID (case sensitive):  ")

      password_input = input("Please enter your password (case sensitive):  ")
      