lower_limit = int(input("Enter lower limit : "))
upper_limit = int(input("Enter upper limit : "))

prime_numbers_dict = {}
prime_numbers_dict[1] = False
prime_numbers_dict[0] = False
for i in range(upper_limit+1):
    prime_numbers_dict[i] = True
i = 2

for i in range(2,(upper_limit+1)//2):
    j = i
    while( j*i <= upper_limit):
        prime_numbers_dict[i*j] = False
        j+=1

print("Prime numbers in the given range \n")

flg = True
for i in range(lower_limit, upper_limit+1):
    if prime_numbers_dict[i] == True:
        flg = False
        print(i,end=" ")

if flg == True:
    print("There are no prime numbers in the given range")