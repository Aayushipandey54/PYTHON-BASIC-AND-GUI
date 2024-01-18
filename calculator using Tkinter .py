import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def calculate_result(choice, num1, num2):
    if choice == 1:
        return add(num1, num2)
    elif choice == 2:
        return subtract(num1, num2)
    elif choice == 3:
        return multiply(num1, num2)
    elif choice == 4:
        return divide(num1, num2)

def on_calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        choice = int(var_operation.get())
        result = calculate_result(choice, num1, num2)
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and set up widgets
entry_num1 = tk.Entry(root, width=10)
entry_num2 = tk.Entry(root, width=10)
var_operation = tk.StringVar(value="1")

label_num1 = tk.Label(root, text="Enter the first number:")
label_num2 = tk.Label(root, text="Enter the second number:")
label_operation = tk.Label(root, text="Select operation:")
result_label = tk.Label(root, text="Result: ")

button_calculate = tk.Button(root, text="Calculate", command=on_calculate)

# Arrange widgets using grid layout
label_num1.grid(row=0, column=0)
entry_num1.grid(row=0, column=1)
label_num2.grid(row=1, column=0)
entry_num2.grid(row=1, column=1)
label_operation.grid(row=2, column=0)

operations = [("Add", "1"), ("Subtract", "2"), ("Multiply", "3"), ("Divide", "4")]

for i, (operation_text, operation_value) in enumerate(operations, start=3):
    radio_button = tk.Radiobutton(root, text=operation_text, variable=var_operation, value=operation_value)
    radio_button.grid(row=i, column=0, columnspan=2)

button_calculate.grid(row=i+1, column=0, columnspan=2)
result_label.grid(row=i+2, column=0, columnspan=2)

# Start the Tkinter main loop
root.mainloop()

