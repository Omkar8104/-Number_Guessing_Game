import random

def computer_number_guessing_game():
    
    secret_number = random.randint(1, 100)

    
    attempts = 0
    max_attempts = 5

    print("Welcome to the Computer Number Guessing Game!")
    print("I've selected a number between 1 and 100. Can you guess it?")

    while attempts < max_attempts:
        
        user_guess = int(input("Enter your guess: "))

        
        if user_guess == secret_number:
            print("Congratulations! You guessed the correct number:", secret_number)
            break
        elif user_guess < secret_number:
            print("Too low. Try again!")
        else:
            print("Too high. Try again!")

        attempts += 1
        print("Attempts remaining:", max_attempts - attempts)

   
    if attempts == max_attempts:
        print("Sorry, you ran out of attempts. The correct number was:", secret_number)


computer_number_guessing_game()
