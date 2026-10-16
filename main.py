def number_guessing_game():
    import random
    number = random.randint(1, 100)
    print(f"{'='*40}\n{' '*5}{'*'*30}")
    print(f"{' '*5}*{' ' * 27} *")
    print(f"{' '*5}*   NUMBER GUESSING SYSTEM {' ' * 2}*")
    print(f"{' '*5}*{' ' * 27} *")
    print(f"{' '*5}{'*'*30}\n{'='*40}")
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    attempts = 0
    while True:
        guess = input("Enter your number (type 'exit' to quit): ")
        if guess == 'exit':
            print("Thanks for playing the game!")
            break
        elif guess.isdigit():
            guess = int(guess)
        else:
            print("Please enter a valid input!")
            continue
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue
        attempts +=1
        if number > guess:
            print("Too low! Try again")
        elif number < guess:
            print("Too high! Try again")
        else:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
            break
           
number_guessing_game()