    #this is the game which is modify guessing game , that's diffrent from the another game.
import random
guessing_number = random.randint(1,50)
winning_number = int(input('enter any number between 1 to 100'))


while true:
    if winning_number == guessing_number:
        print('you think exact number very good')

    else:
        if winning_number < guessing_number:
            print('too high')

        else:
            print('too law')
           