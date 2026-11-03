import random


def flip(stack, k):
    """Flip (reverse) the top k pancakes. stack[0] is the top of the stack."""
    return stack[:k][::-1] + stack[k:]


def print_stack(stack):
    print("Current stack (top -> bottom):", stack)


def pancake_game():
    # Random pancakes from 1 to 6, shuffled (re-shuffle if it starts already sorted)
    stack = random.sample(range(1, 7), 6)
    while stack == sorted(stack):
        stack = random.sample(range(1, 7), 6)
    moves = 0

    print("Welcome to the Pancake Sorting Game!")
    print("Arrange the pancakes with the smallest on top and the largest at the bottom.")
    print("Type the number of pancakes (from the top) you want to flip.\n")

    while stack != sorted(stack):
        print_stack(stack)
        try:
            k = int(input(f"Flip top how many pancakes? (2-{len(stack)}): "))
        except ValueError:
            print("Enter a valid number.")
            continue

        if k < 2 or k > len(stack):
            print("Invalid number. Try again.")
            continue

        stack = flip(stack, k)
        moves += 1

    print_stack(stack)
    print(f"You sorted the pancakes in {moves} moves!")


if __name__ == "__main__":
    pancake_game()
