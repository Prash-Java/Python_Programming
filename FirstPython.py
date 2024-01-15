print("Hello To Python World From Java World")
print("Total Sum = ", 5 + 6)


# For Loop
def _my_for_iteration():
    for step in range(5):
        print(step)


# While Loop
def _my_while_iteration():
    result = int(input("Enter Integer Value:"))
    while result >= 0:
        print(result)
        result = result - 1


# If Else Conditional Constructs
def _if_else_impl():
    value = int(input("Enter Integer Value:"))
    if value >= 9:
        print("Excellent")
    elif value > 5 and value < 9:
        print("Good")
    else:
        print("Fair")


# Function
def _my_arithmetic(a, b):
    c = a + b
    print("Sum: ", c)
    c = a - b
    print("Difference: ", c)
    c = a * b
    print("Product: ", c)
    c = a / b
    print("Quotient: ", c)


# Function Calls
_my_for_iteration()
_my_while_iteration()
_if_else_impl()
x = int(input("Enter First Value: "))
y = int(input("Enter Last Value: "))
_my_arithmetic(x, y)
