import random

# Word list with hints
words_with_hints = {
    "giraffe": "A tall animal with a long neck 🦒",
    "python": "A powerful programming language 🐍",
    "moon": "Earth's natural satellite 🌕",
    "pakistan": "Country with green flag and crescent 🌙🇵🇰",
    "cricket": "A bat-and-ball game loved in Asia 🏏",
}

GUESS_LIMIT = 3


def play_game():
    # Randomly pick a word and its hint
    secret_word, hint = random.choice(list(words_with_hints.items()))

    print("🔤 Welcome to the Guessing Game!")
    print(f"Hint: {hint}")
    print(f"You have {GUESS_LIMIT} attempts to guess the word.\n")

    for attempt in range(1, GUESS_LIMIT + 1):
        guess = input(f"Attempt {attempt} - Enter your guess: ").strip().lower()
        if guess == secret_word:
            print(f"\n🎉 You Win in {attempt} attempts! ✅")
            return

    print(f"\n❌ Out of Guesses. You lose! The word was: '{secret_word}'")


def main():
    # Game loop with replay
    while True:
        play_game()
        replay = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
        if replay not in ["yes", "y"]:
            print("👋 Thanks for playing! Allah Hafiz!")
            break


if __name__ == "__main__":
    main()
