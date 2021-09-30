#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""
num1 = ""
PosInt = False
while PosInt == False:
    num1 = float( input("Enter a number: "))
    num1 = num1/2
    if num1 == int(num1):
        PosInt = True
    else:
        print("That is not an even integer")
print("That is an even integer")