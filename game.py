import random

number = random.randint(0,100)

guess = int(input("Guess a number Between 1 to 100: "))
guess_count = 0
guess_limit = 10


#loop
while guess != number:
    guess_count += 1

    if guess_count < guess_limit:
        print("You have (%d) chances left" % (guess_limit - guess_count))
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
    





    
    
