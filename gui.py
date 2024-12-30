import random
import tkinter as tk
from tkinter import messagebox
from inventory import title, uppercase_letters, lowercase_letters, digits, special_characters

# Create main window (named anirudh)
anirudh = tk.Tk()
anirudh.title("Password Generator")
anirudh.geometry("600x600")
anirudh.config(bg="#f0f8ff")  # Set background color

# Title label with attractive font and color
title_label = tk.Label(anirudh, text='Password Generator', font=("Helvetica Neue", 38, "bold"), fg="#2e8b57", bg="#f0f8ff")
title_label.grid(row=0, column=0, columnspan=2, pady=20)

# Uppercase letter checkbox with custom style
include_uppercase = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(anirudh, text="Include Uppercase Letters", variable=include_uppercase, font=("Arial", 12), fg="#4b0082", bg="#f0f8ff")
uppercase_checkbox.grid(row=1, column=0, sticky="w")

# Lowercase letter checkbox with custom style
include_lowercase = tk.BooleanVar()
lowercase_checkbox = tk.Checkbutton(anirudh, text="Include Lowercase Letters", variable=include_lowercase, font=("Arial", 12), fg="#4b0082", bg="#f0f8ff")
lowercase_checkbox.grid(row=2, column=0, sticky="w")

# Digit checkbox with custom style
include_digits = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(anirudh, text="Include Digits", variable=include_digits, font=("Arial", 12), fg="#4b0082", bg="#f0f8ff")
digits_checkbox.grid(row=3, column=0, sticky="w")

# Special character checkbox with custom style
include_specials = tk.BooleanVar()
specials_checkbox = tk.Checkbutton(anirudh, text="Include Special Characters", variable=include_specials, font=("Arial", 12), fg="#4b0082", bg="#f0f8ff")
specials_checkbox.grid(row=4, column=0, sticky="w")

# Length input with border color change
length_label = tk.Label(anirudh, text="Enter the desired length of the string:", font=("Arial", 12), fg="#4b0082", bg="#f0f8ff")
length_label.grid(row=5, column=0, pady=10, sticky="w")

length_entry = tk.Entry(anirudh, font=("Arial", 12), bd=2, relief="solid", fg="#333", bg="#ffffff")
length_entry.grid(row=5, column=1, pady=10)

# Generate Button with custom styling
def generate_string():
    # Validate length input
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive number.")
    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Please enter a valid positive number for length.\n{str(e)}")
        return

    # Build the character pool based on user choices
    character_pool = []
    if include_uppercase.get():
        character_pool.extend(uppercase_letters)
    if include_lowercase.get():
        character_pool.extend(lowercase_letters)
    if include_digits.get():
        character_pool.extend(digits)
    if include_specials.get():
        character_pool.extend(special_characters)

    # Validate if the pool is not empty
    if not character_pool:
        messagebox.showerror("Input Error", "You must select at least one character type to generate the string.")
        return

    # Generate the random string
    result = ''.join(random.choices(character_pool, k=length))
    result_label.config(text=f"Generated String: {result}", fg="#333", bg="#f0f8ff")

generate_button = tk.Button(anirudh, text="Generate String", command=generate_string, font=("Arial", 14, "bold"), fg="white", bg="#4b0082", bd=0, relief="solid")
generate_button.grid(row=6, column=0, columnspan=2, pady=20)

# Result label with custom styling
result_label = tk.Label(anirudh, text="Generated String will appear here.", font=("Arial", 14, "italic"), fg="#000", bg="#f0f8ff")
result_label.grid(row=7, column=0, columnspan=2, pady=20)

# Run the application
anirudh.mainloop()
