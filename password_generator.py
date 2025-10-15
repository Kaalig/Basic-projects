import string
import random

def generate_password(len=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.digits),
        random.choice(string.punctuation),
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase)
    ]
    password += [random.choice(alphabet) for i in range(len)]
    random.shuffle(password)
    return "".join(password)


generate = input("Salutation soldier. Would you like a generated password (Y/N) ? ")


while generate == "Y" or generate == "y" or generate == "N" or generate == "n":

    if generate == "N" or generate == "n":
        print("No problem, take care ! ")
        quit()

    else:
        print(generate_password())
        break
else:
    print("Please choose y or n to continue.")
    generate = input("Salutation soldier. Would you like a generated password (Y/N) ? ")
