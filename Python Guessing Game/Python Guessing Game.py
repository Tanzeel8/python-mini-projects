import random

# 1. Word list with hints
words_with_hints = {
    "giraffe": "A tall animal with a long neck 🦒",
    "python": "A powerful programming language 🐍",
    "moon": "Earth's natural satellite 🌕",
    "pakistan": "Country with green flag and crescent 🌙🇵🇰",
    "cricket": "A bat-and-ball game loved in Asia 🏏"
}

def play_game():
    # 2. Randomly pick a word and its hint
    secret_word, hint = random.choice(list(words_with_hints.items()))
    guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False

    print("🔤 Welcome to the Guessing Game!")
    print(f"Hint: {hint}")
    print(f"You have {guess_limit} attempts to guess the word.\n")

    while guess != secret_word and not out_of_guesses:
        if guess_count < guess_limit:
            guess = input(f"Attempt {guess_count + 1} - Enter your guess: ").lower()
            guess_count += 1
        else:
            out_of_guesses = True

    if out_of_guesses:
        print(f"\n❌ Out of Guesses. You lose! The word was: '{secret_word}'")
    else:
        print(f"\n🎉 You Win in {guess_count} attempts! ✅")

# 3. Game loop with replay
while True:
    play_game()
    replay = input("\n🔁 Do you want to play again? (yes/no): ").lower()
    if replay not in ["yes", "y"]:
        print("👋 Thanks for playing! Allah Hafiz!")
        break

