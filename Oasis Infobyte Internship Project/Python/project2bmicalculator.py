import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    # Get user inputs
    weight = weight_entry.get()
    height = height_entry.get()
    
    try:
        # Convert to numbers and validate
        weight = float(weight)
        height = float(height)
        
        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Values must be greater than zero!")
            return
        
        # Calculate BMI
        bmi = weight / (height ** 2)
        category = get_bmi_category(bmi)
        
        # Show result
        result_text = f"BMI: {bmi:.1f}\nCategory: {category}"
        result_label.config(text=result_text)
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")

# Create main window
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("300x250")

# Create input fields
input_frame = tk.Frame(window)
input_frame.pack(pady=20)

tk.Label(input_frame, text="Weight (kg):").grid(row=0, column=0, padx=5, pady=5)
weight_entry = tk.Entry(input_frame)
weight_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Height (m):").grid(row=1, column=0, padx=5, pady=5)
height_entry = tk.Entry(input_frame)
height_entry.grid(row=1, column=1, padx=5, pady=5)

# Create buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

calc_button = tk.Button(button_frame, text="Calculate BMI", command=calculate_bmi)
calc_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_fields)
clear_button.pack(side=tk.LEFT, padx=5)

# Result display
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=15)

# Start the application
window.mainloop()
