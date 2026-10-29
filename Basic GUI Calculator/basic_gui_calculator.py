import tkinter as tk


def compute(num1, op, num2):
    """Return the result of num1 <op> num2, or an error message."""
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2 if num2 != 0 else "Cannot divide by zero"
    elif op == "%":
        return num1 % num2 if num2 != 0 else "Cannot divide by zero"
    elif op == "**":
        return num1 ** num2
    return "Invalid operator"


def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operator.get().strip()
        res = compute(num1, op, num2)
        result_label.config(text=f"Result: {res}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")
    except OverflowError:
        result_label.config(text="Result is too large")


# GUI setup
root = tk.Tk()
root.title("Basic GUI Calculator")

tk.Label(root, text="Enter First Number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Operator (+, -, *, /, %, **):").pack()
operator = tk.Entry(root)
operator.pack()

tk.Label(root, text="Enter Second Number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=5)

result_label = tk.Label(root, text="Result: ")
result_label.pack()

root.mainloop()
