#Providing Function Definition
def sum(x, y):
     #"Going to add x and y"
    s=x + y
    print("Sum of two numbers is")
    print(s)
       #Calling the sum Function
sum(10, 20)
sum(20, 30)


def sum1(a, b):
    "Adding the two values"
    print("Printing within Function")
    print( a + b )
    return( a + b )


def msg():
    print("Hello")
    return

total = sum1(10, 20)
print ?Printing Outside: ?,total
msg()
print("Rest of code")