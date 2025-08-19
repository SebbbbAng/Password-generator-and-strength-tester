# Password Generator
# This script generates a random password based on user input for the number of numbers, letters, and special characters.

import random
from itertools import product
from tkinter import *

# Define the different character sets used for password generation and testing
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
specials = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']

# Combine all character sets into one list for brute force guessing
character_set =  numbers + lowercase_letters + uppercase_letters + specials


def generate_password():
    # Attempt to generate a password based on user input
    try:
        # Get the number of each character type from user entries (input fields)
        numbers_count = int(ent_numbers.get())
        lowercase_count = int(ent_lowercase.get())
        uppercase_count = int(ent_uppercase.get())
        special_count = int(ent_special.get())

        # Check for negative inputs and warn the user
        if numbers_count < 0 or lowercase_count < 0 or uppercase_count < 0 or special_count < 0:
            lbl_result_password.config(text="Please enter only positive numbers.")
            return

        # Calculate total length of password requested
        password_length = numbers_count + lowercase_count + uppercase_count + special_count

        # Check that password length is greater than zero
        if password_length <= 0:
            lbl_result_password.config(text="You must include at least one character.")
            return
        
        # Create password list by selecting random characters from each category
        password_chars = []
        for i in range(numbers_count):
            password_chars.append(random.choice(numbers))
        for i in range(lowercase_count):
            password_chars.append(random.choice(lowercase_letters))
        for i in range(uppercase_count):
            password_chars.append(random.choice(uppercase_letters))
        for i in range(special_count):
            password_chars.append(random.choice(specials))

        # Shuffle the list to mix the characters randomly
        random.shuffle(password_chars)
        # Join the list into a string to form the final password
        password_str = ''.join(password_chars)

        # Display the generated password in the result label
        lbl_result_password.config(text="Password: " + password_str)
    
    except ValueError:
        # Handle case where user inputs are not whole numbers
        lbl_result_password.config(text="Please enter only whole numbers.")


# Strength tester
# This script tests the strength of a password by attempting to guess it using the rockyou.txt common password dictionary and brute force and gives the password a score based on how many attempts it took to guess.

def bruteForce_strengthTester(user_input):
    # Initialize score and counters
    password_strength_score = 0
    guess_count = 0
    guessed = False
    progress_count = 0

    # Open the rockyou.txt password dictionary file for reading
    f = open("rockyou.txt", "r", encoding="utf-8", errors="ignore")
    
    # First attempt: try to guess using common passwords from the dictionary
    for line in f:
        progress_count = progress_count + 1
        guess_count = guess_count + 1
        # Update progress label every 10 million guesses
        if progress_count == 10000000:
            lbl_progress.config(text="Progress: " + str(guess_count) + " attempts so far...")
            window.update()
            progress_count = 0
        guess_password = line.strip("\n")
        # Check if guess matches the user's password
        if guess_password == user_input:
            lbl_guess_count.config(text="Guessed password in " + str(guess_count) + " attempts using rockyou.txt common password dictionary.")
            lbl_guessed_password.config(text="Guessed password: " + guess_password)
            guessed = True
            break
    f.close()

    # If not guessed from dictionary, try brute force with numbers only (length 1 to 7)
    if not guessed:
        for length in range(1, 8):
            for combo in product(numbers, repeat=length):
                guess_password = ''.join(combo)
                progress_count = progress_count + 1
                guess_count = guess_count + 1
                # Update progress periodically
                if progress_count == 10000000:
                    lbl_progress.config(text="Progress: " + str(guess_count) + " attempts so far...")
                    window.update()
                    progress_count = 0
                # Check for a match
                if guess_password == user_input:
                    lbl_guess_count.config(text="Guessed password in " + str(guess_count) + " attempts using the brute force method.")
                    lbl_guessed_password.config(text="Guessed password: " + guess_password)
                    guessed = True
                    break
            if guessed:
                break

    # If still not guessed, try brute force with full character set (length 1 to 10)
    if not guessed:
        for i in range(1, 6):
            for combo in product(character_set, repeat=i):
                guess_password = ''.join(combo)
                progress_count = progress_count + 1
                guess_count = guess_count + 1
                # Update progress periodically
                if progress_count == 10000000:
                    lbl_progress.config(text="Progress: " + str(guess_count) + " attempts so far...")
                    window.update()
                    progress_count = 0
                # Check for a match
                if guess_password == user_input:
                    lbl_guess_count.config(text="Guessed password in " + str(guess_count) + " attempts using the brute force method.")
                    lbl_guessed_password.config(text="Guessed password: " + guess_password)
                    guessed = True
                    break
                # Stop if guess attempts exceed 1 billion to avoid infinite loops
                if guess_count > 1000000000:
                    lbl_timeout.config(text="Timeout: Too many attempts, stopping the search.")
                    break
            if guessed or guess_count > 1000000000:
                break

    # Assign a password strength score based on number of guesses needed (logarithmic thresholds)
    if guess_count > 1000000000:
        password_strength_score = 10
    elif guess_count > 32000000:
        password_strength_score = 9
    elif guess_count > 10000000:
        password_strength_score = 8
    elif guess_count > 3200000:
        password_strength_score = 7
    elif guess_count > 1000000:
        password_strength_score = 6
    elif guess_count > 320000:
        password_strength_score = 5
    elif guess_count > 100000:
        password_strength_score = 4
    elif guess_count > 32000:
        password_strength_score = 3
    elif guess_count > 10000:
        password_strength_score = 2
    elif guess_count > 3200:
        password_strength_score = 1
    else:
        password_strength_score = 0
    
    # Display the password strength score in the GUI
    lbl_strength_score.config(text="Password strength score: " + str(password_strength_score) + "/10.")


# Password strength tester based on character types, length, and repetition
def password_strengthTester(user_input):
    # Initialize score and flags for character types
    password_strength_score = 0
    has_number = False
    has_lowercase_letter = False
    has_uppercase_letter = False
    has_special_character = False

    # Check if password length is within the allowed range
    if len(user_input) < 5:
        lbl_range_check.config(text="Password is too short. It should be at least 5 characters long.")
        return
    elif len(user_input) > 15:
        lbl_range_check.config(text="Password is too long. It should be at most 15 characters long.") 
        return
    else:
        # Increment score based on password length tiers
        if len(user_input) > 14:
            password_strength_score = password_strength_score + 5
        elif len(user_input) > 12:
            password_strength_score = password_strength_score + 4
        elif len(user_input) > 10:
            password_strength_score = password_strength_score + 3
        elif len(user_input) > 8:
            password_strength_score = password_strength_score + 2
        elif len(user_input) > 6:
            password_strength_score = password_strength_score + 1
        else:
            password_strength_score = password_strength_score + 0

    # Check the presence of different character types in the password
    for char in user_input:
        if char in numbers:
            has_number = True
        elif char in lowercase_letters:
            has_lowercase_letter = True
        elif char in uppercase_letters:
            has_uppercase_letter = True
        elif char in specials:
            has_special_character = True

    # Count how many character types are present
    type_count = sum([has_number, has_lowercase_letter, has_uppercase_letter, has_special_character])

    # Add to score for each character type present if at least two types are found
    if type_count >= 2:
        if has_number:
            password_strength_score = password_strength_score + 1
        if has_lowercase_letter:
            password_strength_score = password_strength_score + 1
        if has_uppercase_letter:
            password_strength_score = password_strength_score + 1
        if has_special_character:
            password_strength_score = password_strength_score + 3

    # Analyze consecutive repeated characters to penalize repetition
    repeat_count = 0
    max_repeat = 0

    for i in range(1, len(user_input)):

        if user_input[i] == user_input[i - 1]:
            repeat_count = repeat_count + 1
        else:
            repeat_count = repeat_count + 1  # Include the last character in the count
            if repeat_count > max_repeat:
                max_repeat = repeat_count
            repeat_count = 0

    # Check final max repetition count
    repeat_count = repeat_count + 1  # Include the last character in the count
    if repeat_count > max_repeat:
        max_repeat = repeat_count
        
    # Penalize score based on how many repeated characters in a row
    if max_repeat > 7:
        password_strength_score = password_strength_score - 3
    elif max_repeat > 5:
        password_strength_score = password_strength_score - 2
    elif max_repeat > 3:
        password_strength_score = password_strength_score - 1
    
    # Make sure score stays between 0 and 10
    if password_strength_score < 0:
        password_strength_score = 0
    elif password_strength_score > 10:
        password_strength_score = 10
    
    # Display the password strength score in the GUI
    lbl_strength_score.config(text="Password strength score: " + str(password_strength_score) + "/10.")


# Create the main window for the GUI application
window = Tk()
window.geometry("600x600")
window.title("Password Generator and Strength Tester")

# Set application icon and background color
icon = PhotoImage(file = "logo.png")
window.iconphoto(True, icon)
window.config(background="black")

# Label prompting user to choose between password generation or testing
lbl_main_choice = Label(window, text = "Would you like to generate a password or test a password? ")
lbl_main_choice.pack(pady = 5)
lbl_main_choice.config(font=("Arial", 15, 'bold'))


# Password generation button and input fields setup
def generate_password_button():
    global ent_numbers, ent_lowercase, ent_uppercase, ent_special, lbl_result_password
    
    # Create the generate button and configure its appearance
    btn_generate_password = Button(window, text="Generate Password")
    btn_generate_password.config(command = generate_password)
    btn_generate_password.config(font=("Arial", 15, 'bold'))
    btn_generate_password.pack()

    # Create and pack label and entry for number of numbers
    lbl_numbers = Label(window, text="How many numbers would you like in your password?")
    ent_numbers = Entry(window)
    lbl_numbers.pack(pady = 5)
    ent_numbers.pack(pady = 5)

    # Create and pack label and entry for number of lowercase letters
    lbl_lowercase = Label(window, text="How many lowercase letters would you like in your password?")
    ent_lowercase = Entry(window)
    lbl_lowercase.pack(pady = 5)
    ent_lowercase.pack(pady = 5)

    # Create and pack label and entry for number of uppercase letters
    lbl_uppercase = Label(window, text="How many uppercase letters would you like in your password?")
    ent_uppercase = Entry(window)
    lbl_uppercase.pack(pady = 5)
    ent_uppercase.pack(pady = 5)

    # Create and pack label and entry for number of special characters
    lbl_special = Label(window, text="How many special characters would you like in your password?")
    ent_special = Entry(window)
    lbl_special.pack(pady = 5)
    ent_special.pack(pady = 5)

    # Label to show the generated password result
    lbl_result_password = Label(window, text="")
    lbl_result_password.pack(pady = 5)


# Password strength tester by brute force button setup
def bruteForce_strengthTester_button():
    global lbl_progress, lbl_guess_count, lbl_guessed_password, lbl_timeout, lbl_strength_score
    user_input = ent_password.get()

    # Create and pack labels to show progress, guesses, results, timeout and score
    lbl_progress = Label(window, text = "")
    lbl_progress.pack(pady = 5)

    lbl_guess_count = Label(window, text="")
    lbl_guess_count.pack(pady = 5)

    lbl_guessed_password = Label(window, text="")
    lbl_guessed_password.pack(pady = 5)

    lbl_timeout = Label(window, text="")
    lbl_timeout.pack(pady = 5)

    lbl_strength_score = Label(window, text="")
    lbl_strength_score.pack(pady = 5)

    # Force update of the window to show initial empty labels
    window.update()

    # Run the brute force strength test function
    bruteForce_strengthTester(user_input)

# Password strength tester button setup
def password_strengthTester_button():
    global lbl_range_check, lbl_strength_score
    user_input = ent_password.get()

    # Create and pack labels for length checks and strength score
    lbl_range_check = Label(window, text="")
    lbl_range_check.pack(pady = 5)

    lbl_strength_score = Label(window, text="")
    lbl_strength_score.pack(pady = 5)

    # Run the rule-based password strength tester
    password_strengthTester(user_input)


# Setup password input and tester choice buttons
def choice_test_password():
    global ent_password
    
    # Label prompting user to enter password to test
    password_entry_label = Label(window, text="Enter the password you want to test:")
    password_entry_label.pack(pady = 5)

    # Entry field for user to input password
    ent_password = Entry(window)
    ent_password.pack(pady = 5)

    # Button for brute force strength testing
    btn_brute_force = Button(window, text="Brute Force Password Strength Tester")
    btn_brute_force.config(font=("Arial", 15, 'bold'))
    btn_brute_force.config(command = bruteForce_strengthTester_button)
    btn_brute_force.pack(pady = 5)

    # Button for rule-based strength testing
    btn_rule_tester = Button(window, text="Password Strength Tester")
    btn_rule_tester.config(font=("Arial", 15, 'bold'))
    btn_rule_tester.config(command = password_strengthTester_button)
    btn_rule_tester.pack(pady = 5)

# Buttons to choose between generating password or testing password strength
btn_choice_generate = Button(window, text="Generate Password")
btn_choice_generate.config(font=("Arial", 15, 'bold'))
btn_choice_generate.config(command = generate_password_button)
btn_choice_generate.pack(pady = 5)

btn_choice_test = Button(window, text="Test Password Strength")
btn_choice_test.config(font=("Arial", 15, 'bold'))
btn_choice_test.config(command = choice_test_password)
btn_choice_test.pack(pady = 5)

# Start the Tkinter main loop (GUI event loop)
window.mainloop()
