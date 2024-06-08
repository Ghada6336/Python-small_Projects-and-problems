import string
import random

characters = list(string.ascii_letters + string.digits + " !@#$%^&*()")


def generate_password():
    password_length = int(input("enter the password length"))
    random.shuffle(characters)
    password = []

    for x in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(password)
    password = "".join(password)

    print(password)


option = input("do you want to generate password (yeas/NO)")
option.upper()
if option == "YES":
    generate_password()
elif option == "NO":
    print("programme ended")
    quit()
else:
    print("invalid input")
    quit()
