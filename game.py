import random

print("🎯 Welcome to Number Guessing Game!")

while True:

    number = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number between 1 and 100.")

    while True:
        guess = input("Enter your guess (or q to quit): ")

        if guess.lower() == 'q':
            print("Game Ended!")
            exit()

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("Too Low!")
        elif guess > number:
            print("Too High!")
        else:
            print(f"🎉 Correct! You guessed in {attempts} attempts.")
            break

    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
