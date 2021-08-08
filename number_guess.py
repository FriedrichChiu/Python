import random


user = input("Please enter your name: ")
print("Hi " + user + '''
Thanks for joining our game.
In this game, you will have 6 chances to guess the number between 1 and 10.
After each guess, we will give you a hint to help you approximate the correct number
Are you ready to take challenges ? Let's go ! 
''')

number = random.randint(1,10)
print(number) 
counter = 0


print("We've set up a number between 1 to 10. Now it's your turn to guess.")

while counter <= 6:
    answer = input("Type your guess here: ") 
    if int(answer) == number:
        counter += 1
        print('Excellent! You only take ' + str(counter) + ' guess(es)' )
        print('The number is: ' + str(number))
        break
    else:
        counter += 1
        if int(answer) > number:        
            print("It's above the number.")
            print("Take another guess.")
        else:
            print("It's below the number")
            print("Please take another guess")

if counter > 6:
    print("Sorry, you've guessed six times without hitting the number")
    print("The correct answer is: " + str(number))


        







    
