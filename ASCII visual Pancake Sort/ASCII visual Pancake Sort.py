import os
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_stack(arr, max_width=40):
    """
    Draw a stack of pancakes as ASCII (top of the stack first).
    arr: list of integers (sizes), arr[0] is the top pancake
    max_width: maximum characters width for the largest pancake
    """
    if not arr:
        print("(empty stack)")
        return

    max_val = max(arr)
    for size in arr:
        # scale size to width
        width = max(1, int(size / max_val * max_width))
        # make the pancake look like: (====)
        pancake = "(" + "=" * width + ")"
        # center it in the playground
        print(pancake.center(max_width + 6))
    print("\n")  # spacing


def flip(arr, k):
    """Reverse the prefix arr[0:k+1] (k inclusive)"""
    return arr[:k + 1][::-1] + arr[k + 1:]


def pancake_sort_with_visual(arr, delay=1.0):
    """
    Perform pancake sort and animate the flips in the terminal.
    delay: seconds to wait after each frame (smaller -> faster)
    """
    arr = arr[:]  # copy
    n = len(arr)
    print("Original stack (top -> bottom):", arr)
    time.sleep(1.0)
    clear()
    draw_stack(arr)
    time.sleep(delay)

    for size in range(n, 1, -1):
        # find the index of the largest pancake in arr[:size]
        max_val = max(arr[:size])
        max_idx = arr.index(max_val)

        # if it is already in place, continue
        if max_idx == size - 1:
            continue

        # 1) bring the largest pancake to the top (if needed)
        if max_idx != 0:
            arr = flip(arr, max_idx)
            clear()
            print(f"Flip at index {max_idx} (bring largest to top)")
            draw_stack(arr)
            time.sleep(delay)

        # 2) flip it down to its final position
        arr = flip(arr, size - 1)
        clear()
        print(f"Flip at index {size - 1} (move largest to position {size - 1})")
        draw_stack(arr)
        time.sleep(delay)

    clear()
    print("Final sorted stack (top -> bottom):", arr)
    draw_stack(arr)
    return arr


if __name__ == "__main__":
    # Example stack: values are pancake diameters (larger = wider)
    example = [3, 6, 1, 8, 4, 2]
    # smaller delay for a faster animation
    pancake_sort_with_visual(example, delay=0.8)
