import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = combo_unit.get().lower()

        if unit == "celsius":
            f = (temp * 9/5) + 32
            k = temp + 273.15
            result.set(f"Fahrenheit: {f:.2f} °F\nKelvin: {k:.2f} K")

        elif unit == "fahrenheit":
            c = (temp - 32) * 5/9
            k = c + 273.15
            result.set(f"Celsius: {c:.2f} °C\nKelvin: {k:.2f} K")

        elif unit == "kelvin":
            c = temp - 273.15
            f = (c * 9/5) + 32
            result.set(f"Celsius: {c:.2f} °C\nFahrenheit: {f:.2f} °F")

        else:
            messagebox.showerror("Invalid Unit", "Please select a valid unit.")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Create window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x250")
root.resizable(False, False)

# Input field
tk.Label(root, text="Enter Temperature:", font=("Arial", 12)).pack(pady=5)
entry_temp = tk.Entry(root, font=("Arial", 12))
entry_temp.pack(pady=5)

# Dropdown for unit selection
tk.Label(root, text="Select Unit:", font=("Arial", 12)).pack(pady=5)
combo_unit = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", font=("Arial", 12))
combo_unit.pack(pady=5)
combo_unit.set("Celsius")  # Default value

# Convert button
tk.Button(root, text="Convert", command=convert_temperature, font=("Arial", 12), bg="lightblue").pack(pady=10)

# Result display
result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 12), justify="center").pack(pady=10)

# Run the GUI
root.mainloop()
