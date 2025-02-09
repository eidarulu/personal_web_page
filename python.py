import random

# Assignment 2

# 1 - Greeting
print("Hello! What is your name?")
name = input("> ")

# 2 - Mood
print("Nice to meet you, " + name + "! How are you today?")
mood = input("> ")

while True:
    if mood == "good":
        print("That's great to hear!")
        break
    elif mood == "bad":
        print("Oh no! I hope you feel better soon!")
        break
    else:
        print("I'm sorry, I don't understand. Please enter 'good' or 'bad'")
        mood = input("> ")

# 3 - Even or Odd
print("Enter a number to see if it is even or odd")
number = int(input("> "))

if number % 2 == 0:
    print("The number " + str(number) + " is even")
else:
    print("The number " + str(number) + " is odd")

# 4 - Guessing Game
guessed_number = random.randint(1, 10)

print("Now guess a number between 1 and 10")
guess = int(input("> "))

if guess == guessed_number:
    print("You guessed the correct number!")
else:
    print("Wrong! The correct number was " + str(guessed_number))

# 5 - Farewell
print("Thanks for playing! See you next time, " + name + "!")