import random

def main():
    print("Hey! Welcome to my Guessing Game!")
    random_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
        except ValueError:
            print("Oops! That's not a valid number. Please try again.")
            continue
        
        if guess < 1 or guess > 100:
            print("Hey, stay within 1 and 100, please!")
        elif guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Yay! You guessed the number {random_number} in {attempts} tries. Well done!")
            break

if __name__ == "__main__":
    main()
