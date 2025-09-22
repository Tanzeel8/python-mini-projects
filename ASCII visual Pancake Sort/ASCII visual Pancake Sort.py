import os

import time



def clear():

    os.system('cls' if os.name == 'nt' else 'clear')



def draw_stack(arr, max_width=40):

    """

    Draw stack of pancakes as ASCII.

    arr: list of integers (sizes)

    max_width: maximum characters width for the largest pancake

    """

    if not arr:

        print("(empty stack)")

        return



    max_val = max(arr)

    for size in reversed(arr):  # draw from top to bottom (smallest on top visually)

        # scale size to width

        width = max(1, int(size / max_val * max_width))

        # make the pancake look like: (====)

        pancake = "(" + "=" * width + ")"

        # center it in playground

        print(pancake.center(max_width + 6))

    print("\n")  # spacing



def flip(arr, k):

    """Reverse prefix arr[0:k] (k inclusive)"""

    return arr[:k+1][::-1] + arr[k+1:]



def pancake_sort_with_visual(arr, delay=1.0):

    """

    Perform pancake sort and animate flips in the terminal.

    delay: seconds to wait after each frame (smaller -> faster)

    """

    arr = arr[:]  # copy

    n = len(arr)

    print("Original stack (bottom -> top):", arr)

    time.sleep(1.0)

    clear()

    draw_stack(arr)

    time.sleep(delay)



    for size in range(n, 1, -1):

        # find index of max in arr[:size]

        max_val = max(arr[:size])

        max_idx = arr.index(max_val)



        # if it's already in place, continue

        if max_idx == size - 1:

            continue



        # 1) bring max to front (if needed)

        if max_idx != 0:

            arr = flip(arr, max_idx)

            clear()

            print(f"Flip at index {max_idx} (bring max to top)")

            draw_stack(arr)

            time.sleep(delay)



        # 2) flip it to its final position

        arr = flip(arr, size - 1)

        clear()

        print(f"Flip at index {size-1} (move max to position {size-1})")

        draw_stack(arr)

        time.sleep(delay)



    clear()

    print("Final sorted stack (bottom -> top):", arr)

    draw_stack(arr)

    return arr



if __name__ == "__main__":

    # Example stack: values represent pancake diameters (larger = wider)

    example = [3, 6, 1, 8, 4, 2]

    # smaller delay for faster animation

    pancake_sort_with_visual(example, delay=0.8)

