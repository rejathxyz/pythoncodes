#reverse the words in the string without reversing the letters

def word_reversal(str):
    word_list = str.split(" ")
    reversed_word_list = word_list[::-1]
    return " ".join(reversed_word_list)

str = input("Enter the sentance: ")
print(word_reversal(str))
    