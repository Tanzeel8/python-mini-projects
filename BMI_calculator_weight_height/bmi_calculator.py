import tkinter as tk
from tkinter import messagebox

BG_COLOR = "#EAF6FF"  # light blue background


def get_category(bmi):
    """Return the BMI category for a given BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    return "Obese"


def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and height must be greater than 0")
            return
        bmi = weight / (height ** 2)
        result_label.config(text=f"Your BMI: {bmi:.2f} ({get_category(bmi)})")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


# GUI window
root = tk.Tk()
root.title("BMI Calculator")
root.config(bg=BG_COLOR)

# Heading
heading = tk.Label(root, text="BMI Calculator", font=("Arial", 20, "bold"), bg=BG_COLOR)
heading.grid(row=0, column=0, columnspan=3, pady=10)

# Weight input
tk.Label(root, text="Weight", font=("Arial", 12), bg=BG_COLOR).grid(row=1, column=0, pady=5)
weight_entry = tk.Entry(root, font=("Arial", 12))
weight_entry.grid(row=1, column=1, pady=5)
tk.Label(root, text="kg", font=("Arial", 12), bg=BG_COLOR).grid(row=1, column=2, pady=5)

# Height input
tk.Label(root, text="Height", font=("Arial", 12), bg=BG_COLOR).grid(row=2, column=0, pady=5)
height_entry = tk.Entry(root, font=("Arial", 12))
height_entry.grid(row=2, column=1, pady=5)
tk.Label(root, text="m", font=("Arial", 12), bg=BG_COLOR).grid(row=2, column=2, pady=5)

# Formula display
formula_label = tk.Label(root, text="BMI = weight / height²", font=("Arial", 12), bg=BG_COLOR)
formula_label.grid(row=3, column=0, columnspan=3, pady=10)

# Calculate button
calc_btn = tk.Button(root, text="Calculate", font=("Arial", 12, "bold"),
                     bg="black", fg="white", command=calculate_bmi)
calc_btn.grid(row=4, column=0, columnspan=3, pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg=BG_COLOR)
result_label.grid(row=5, column=0, columnspan=3, pady=10)

root.mainloop()
