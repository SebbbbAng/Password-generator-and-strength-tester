#Password Generator and Strength Tester
This is a simple Python application that lets you generate secure passwords and test the strength of any password using a graphical interface. It’s built with Tkinter and provides both rule-based and brute-force testing for password strength.
#Features
Password Generator
Customize how many numbers, lowercase letters, uppercase letters, and special characters you want.
Generates a random password based on your preferences.
Ensures passwords are shuffled for maximum unpredictability.
Password Strength Tester
Rule-based tester: Scores passwords based on length, character variety, and repeated characters.
Brute-force tester: Simulates guessing the password using the rockyou.txt dictionary and brute-force attempts, showing how many tries it would take to crack it.
Provides a strength score from 0 to 10.
#How to Use
Run the program with Python (python password_tool.py).
Choose between generating a password or testing a password.
For generation:
Enter the number of each character type you want.
Click Generate Password to see the result.
For testing:
Enter the password you want to check.
Choose Brute Force Password Strength Tester or Password Strength Tester.
View the password score and analysis.
#Requirements
Python 3.x
Tkinter (usually included with Python)
rockyou.txt file for brute-force testing (optional but recommended)
logo.png file for the application icon
#Notes
The brute-force tester can be very slow for long or complex passwords.
Passwords shorter than 5 characters or longer than 15 are considered out of range by the rule-based tester.
Always keep your rockyou.txt file in the same folder as the program if you want dictionary-based testing.
#License
This project is open-source and available under the MIT License.
