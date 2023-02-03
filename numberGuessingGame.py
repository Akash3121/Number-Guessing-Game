import random
print("***Game of Guess***")
question = input("Hello! \nWould you like to play a guess game? \nEnter y/n : ")
tries = 1

if question == 'y' or question == 'Y':
    howmany = int(input("Enter how many games would you like to play :"))
    
    #running the loop till no.of times
    for game in range(howmany):
        print("I am going to think a number between 1-25")
        number = random.randint(1,26) 
        guess = int(input("Guess a number between 1-25 : "))
       
        #This loop runs until guess mathches with Actual number and counting it in 
        while guess != number:
            
            #Inform User about his/her Guess number selection, to select precisely
            if guess > number:
                print("your selction is high")
            else:
                print("you selection is low")
            
            guess = int(input("Wrong guess, try again: "))
            
            #Tries incremented if guessed number was a wrong one
            tries += 1
            
        if number == guess:
            print("Your guess is correct\n")
            print("The number was ",number)
            print("No of tries:",tries)
        
else:
    print("Exiting the Game")