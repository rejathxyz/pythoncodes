#to find the sums of digits of number till it becomes one digit value

def sum_of_digits(n):
    if (n == 0):
        return 0
    mod_value = n % 9
    if(mod_value == 0):
        return 9
    else:
        return mod_value

n = int(input("Enter the number: "))
print(sum_of_digits(n))
    