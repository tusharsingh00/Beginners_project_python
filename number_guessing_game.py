import random

def number_guess_game():
    min_num = int(input("Enter the minimum value: "))
    max_num = int(input("Enter the max number: "))
    number_to_guess = random.randint(min_num, max_num)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    
    print(f"I have selected a number between {min_num} and {max_num}. Can you guess it?")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            attempts += 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    number_guess_game()
