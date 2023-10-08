def check_palindrome(str):
    rev_string = str[::-1]
    if rev_string == str:
        return True
    return False

input_string = input("Enter the string: ")
if check_palindrome(input_string) :
    print("The input string ", input_string, "is a palindrome")
else:
    print("The input string ", input_string, "is not a palindrome")