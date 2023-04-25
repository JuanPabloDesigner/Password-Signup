import time

print("Sign-up")

time.sleep(2)

while True:
  psswrd1 = input("Type your password: ")
  while True:
    psswrd2 = input("Type again to confirm: ")
    if psswrd2 == psswrd1:
      print("Registration completed!")
      break
    else:
      print("Wrong password. Please, try again.")
  break