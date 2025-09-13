import tkinter as tk

# Main window
window = tk.Tk()
window.title("Modern Calculator")
window.geometry("320x420")
window.configure(bg="#FFD700")  # Yellow background

# Entry display
entry = tk.Entry(window, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)

# Function to add text to entry
def button_click(value):
    entry.insert(tk.END, value)

# Function to clear entry
def clear_entry():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Button layout and style
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', 'C', '+'),
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == 'C':
            btn = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), bg="red", fg="white",
                            command=clear_entry)
        else:
            btn = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18), bg="#1E90FF", fg="white",
                            command=lambda val=text: button_click(val))
        btn.grid(row=i+1, column=j, padx=5, pady=5)

# Equal button
equal_btn = tk.Button(window, text='=', width=22, height=2, font=("Arial", 18), bg="green", fg="white",
                      command=calculate)
equal_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

window.mainloop()