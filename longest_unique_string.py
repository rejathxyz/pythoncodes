# to find the longest unique substring
def unique_characters(str):
    longest_string=""
    i = 0
    string_set = set()
    for j in range(len(str)):

        if str[j] not in string_set:
            string_set.add(str[j])

        else:
            if len(longest_string) < len(string_set):             
                longest_string = str[i:j]
            i=j
            string_set.clear()
            string_set.add(str[j])
    
    if len(longest_string) < len(string_set):
                longest_string = str[i:j+1]
                
    return(longest_string)

str = input("Enter the string: ")
print(unique_characters(str))
