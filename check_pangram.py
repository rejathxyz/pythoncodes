# program to check whether a string is pangram 
def check_pangram(str):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    string_in_lowercase = str.lower()
    for i in alphabets:
        if i not in string_in_lowercase:
            return False

    return True

input_string = input("Enter the string: ")
if check_pangram(input_string) :
    print("The input string ", input_string, "is a pangram")
else:
    print("The input string ", input_string, "is not a pangram")