def is_palindrome(string):
    # Remove any whitespace and convert to lowercase
    string = string.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return string == string[::-1]

# Prompt the user to enter a string
input_string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(input_string):
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")
