import random

def rps():
    choices = ["rock", "paper", "scissors"]
    comp = random.choice(choices)

    you = input("Choose rock/paper/scissors: ").strip().lower()

    if you not in choices:
        print("Invalid choice.")
        return

    print("Computer:", comp)

    if you == comp:
        print("Tie!")
    elif (you == "rock" and comp == "scissors") or \
         (you == "paper" and comp == "rock") or \
         (you == "scissors" and comp == "paper"):
        print("You win!")
    else:
        print("You lose.")


def guess_number():
    number = random.randint(1, 20)
    attempts = 5

    print("Guess a number between 1 and 20. You have", attempts, "tries.")

    for i in range(attempts):
        try:
            g = int(input("Your guess: "))
        except ValueError:
            print("Enter a number.")
            continue

        if g == number:
            print("Correct! You won.")
            return
        elif g < number:
            print("Too low.")
        else:
            print("Too high.")

    print("Out of attempts. Number was", number)


def main():
    games = ["Rock-Paper-Scissors", "Guess the Number", "Exit"]

    while True:
        print("\n--- Game Machine ---")
        for i, g in enumerate(games, 1):
            print(i, g)

        choice = input("Pick a game (1-3): ").strip()

        if choice == "1":
            rps()
        elif choice == "2":
            guess_number()
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
