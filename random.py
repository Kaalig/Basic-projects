import random
def random_number():
    return random.randint(1, 100)
    
true_number = random_number()

print("Je viens d'écrire un numéro entre 1 et 100 sur ce bout de papier...\n")
while True:
    choice = input("Quel est le numéro que j'ai choisi ? :")
    guess = int(choice)

    if guess == true_number:
        print("Correct! \n")
        print("Veux-tu encore continuer ? (y/n) : ")
        if input() == "y":
                print("C'est reparti ! ")
                true_number = random_number()
        else:
                break
        
    elif guess > true_number:
        print("Too High !")

    elif guess < true_number:
        print("Too Low !")




