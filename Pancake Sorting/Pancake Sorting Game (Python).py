import random

def flip(stack, k):
    return stack[:k][::-1] + stack[k:]

def print_stack(stack):
    print("Current stack (top bottom):", stack)

def pancake_game():
    # Random pancakes from 1 to 6 in random order
    stack = random.sample(range(1, 7), 6)
    moves = 0

    print(" Welcome to Pancake Sorting Game!")
    print("Arrange pancakes from largest at bottom to smallest at top.")
    print("Type the number of pancakes (from top) you want to flip.\n")

    while stack != sorted(stack, reverse=True):
        print_stack(stack)
        try:
            k = int(input("Flip top how many pancakes? (2-6): "))
            if k < 2 or k > len(stack):
                print("Invalid number. Try again. ")
                continue
            stack = flip(stack, k)
            moves += 1
        except ValueError:
            print("Enter a valid number.")

    print_stack(stack)
    print(f" You sorted the pancakes in {moves} moves!")

if  __name__ == "__main__":
    pancake_game()