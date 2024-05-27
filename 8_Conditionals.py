# if statement
# Example 1: Simple if statement
x = 10
if x>5:
    print("x is greater than 5")

# Example 2: if statement with an else block

y = 3
if y%2==0:
    print("y s even")
else:
    print("y is odd")

# if elif else statement
# Example: Using if, elif, and else to handle multiple conditions

grade = 85

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("D")

# Nested if statements

# Example: Nested if statements
num = 15

if num > 10:
    print("Number is greater than 10.")
    
    if num % 2 == 0:
        print("Number is even.")
    else:
        print("Number is odd.")
else:
    print("Number is not greater than 10.")