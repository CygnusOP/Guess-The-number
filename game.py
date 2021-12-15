import random

number = random.randint(0,100)

guess = int(input("Guess a number Between 1 to 100: "))
guess_count = 0
guess_limit = 10


#loop
while guess != number:
    guess_count += 1

    if guess_count == 1:
        print("You have 9 chances left")
    elif guess_count == 2 :
        print("You have 8 chances left")
    elif guess_count == 3:
        print("You have 7 chances left")
    elif guess_count == 4:
        print("You have 6 chances left")
    elif guess_count == 5:
        print("You have 5 chances left")
    elif guess_count == 6:
        print("You have 4 chances left")
    elif guess_count == 7:
        print("You have 3 chances left")
    elif guess_count == 8:
        print("You have 2 chances left")
    elif guess_count == 9:
        print("You have 1 chances left")
    else :
        print("You are out of chances. Good Luck next time!")
        quit()



    if guess < number:
        print("You have to guess something higher.")
        guess =int(input("\nGuess the number: "))
    else :
        print("You need guess something lower.")
        guess = int(input("\nGuess the number: "))

print ("You have won the game")
    





    
    
