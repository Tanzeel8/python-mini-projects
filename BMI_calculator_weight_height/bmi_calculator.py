#start code

import tkinter as tk

from tkinter import messagebox



def calculate_bmi():

    try:

        weight = float(weight_entry.get())

        height = float(height_entry.get())

        if height <= 0:

            messagebox.showerror("Error", "Height must be greater than 0")

            return

        bmi = weight / (height ** 2)

        result_label.config(text=f"Your BMI: {bmi:.2f}")

    except ValueError:

        messagebox.showerror("Error", "Please enter valid numbers")



# GUI Window

root = tk.Tk()

root.title("BMI Calculator")

root.config(bg="#EAF6FF")  # Light blue background



# Heading

heading = tk.Label(root, text="BMI Calculator", font=("Arial", 20, "bold"), bg="#EAF6FF")

heading.grid(row=0, column=0, columnspan=3, pady=10)



# Weight input

tk.Label(root, text="Weight", font=("Arial", 12), bg="#EAF6FF").grid(row=1, column=0, pady=5)

weight_entry = tk.Entry(root, font=("Arial", 12))

weight_entry.grid(row=1, column=1, pady=5)

tk.Label(root, text="kg", font=("Arial", 12), bg="#EAF6FF").grid(row=1, column=2, pady=5)



# Height input

tk.Label(root, text="Height", font=("Arial", 12), bg="#EAF6FF").grid(row=2, column=0, pady=5)

height_entry = tk.Entry(root, font=("Arial", 12))

height_entry.grid(row=2, column=1, pady=5)

tk.Label(root, text="m", font=("Arial", 12), bg="#EAF6FF").grid(row=2, column=2, pady=5)



# Formula display

formula_label = tk.Label(root, text="BMI = weight / height²", font=("Arial", 12), bg="#EAF6FF")

formula_label.grid(row=3, column=0, columnspan=3, pady=10)



# Calculate button

calc_btn = tk.Button(root, text="Calculate", font=("Arial", 12, "bold"), bg="black", fg="white", command=calculate_bmi)

calc_btn.grid(row=4, column=0, columnspan=3, pady=10)



# Result label

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#EAF6FF")

result_label.grid(row=5, column=0, columnspan=3, pady=10)

root.mainloop()

#end code