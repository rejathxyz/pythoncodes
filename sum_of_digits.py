# to find the sums of digits of number till it becomes one digit value
# this program will take the mod the input number if return the value as sum of its digits to 1 digit. 
# if the number is 0  or a multiple of 9 the result will be 0. If the number is 0 we will return it as 0 otherwise
# we will return it as 9 in case the mod is 0
def sum_of_digits(n):
    if (n == 0):
        return 0
    mod_value = n % 9
    if(mod_value == 0):
        return 9
    else:
        return mod_value

n = int(input("Enter the number: "))
print("Sum of the digit is : ",sum_of_digits(n))
    