import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operator.get()

        if op == '+':
            res = num1 + num2
        elif op == '-':
            res = num1 - num2
        elif op == '*':
            res = num1 * num2
        elif op == '/':
            res = num1 / num2 if num2 != 0 else "Cannot divide by zero"
        elif op == '%':
            res = num1 % num2
        elif op == '**':
            res = num1 ** num2
        else:
            res = "Invalid operator"
        result_label.config(text=f"Result: {res}")
    except:
        result_label.config(text="Error in input")

# GUI setup
root = tk.Tk()
root.title("Simple Python Calculator")

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
