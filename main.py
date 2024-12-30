import random
from inventory import title, uppercase_letters, lowercase_letters, digits, special_characters
import pyperclip

# Copy text to clipboard
text = "Hello, this is copied to clipboard!"
pyperclip.copy(text)

# Verify the text has been copied
copied_text = pyperclip.paste()
print("Copied text:", copied_text)

# Prompt user for customization
print(title)
# Function to validate user input for 'y' or 'n'
def get_yes_no_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'y' or user_input == 'n':
            return True

        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# Ask user for each option with validation
include_uppercase = get_yes_no_input("Include uppercase letters? (y/n): ")
include_lowercase = get_yes_no_input("Include lowercase letters? (y/n): ")
include_digits = get_yes_no_input("Include digits? (y/n): ")
include_specials = get_yes_no_input("Include special characters? (y/n): ")


# Ask for the desired length
while True:
    try:
        length = int(input("Enter the desired length of the string: ").strip())
        if length <= 0:
            print("Please enter a positive number.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Build the character pool based on user choices
character_pool = []
if include_uppercase:
    character_pool.extend(uppercase_letters)
if include_lowercase:
    character_pool.extend(lowercase_letters)
if include_digits:
    character_pool.extend(digits)
if include_specials:
    character_pool.extend(special_characters)

# Validate if the pool is not empty
if not character_pool:
    print("You must include at least one type of character to generate the string.")
else:
    # Generate the random string
    result = ''.join(random.choices(character_pool, k=length))
    print("\nGenerated String:", result)
    if get_yes_no_input('Want to copy (y/n)?'):
        copied = pyperclip.copy(result) == f'{result}'
        print('generated password is copied to your clipboard')
    else:
        print("unexpected error occurred")

