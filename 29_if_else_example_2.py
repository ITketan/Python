print("Please enter your age:")
#Declare a variable to store the user input from the keyboard
inputStr = input()
#int(..)function convert string to integer
age = int(inputStr)
#print out your age
print("Your age:",age)

#if age<80 then..
if (age<80):
    print("You are pretty young")

#else if age between 80,100 then
elif (age>=80 and age<=100):
    print("Your are old")

#else (other case)
else:
    print("Your are very old")
