"""10)
WAP for check the number is positive or not
if not then print message "sorry this is
negative number" and convert into positive
number else print that number
(Getting value from the user)
"""
value = int(input("Enter a value : "))
if(value < 0):
    print("Sorry this is negative number")
    value = abs(value)
    print(value)
elif(value == 0):
    print("Number is zero")
else:
    print(value)

