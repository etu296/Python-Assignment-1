# 9.Python Program to Find the GCD of Two Numbers (using function)

def gdc(a, b):
    while b != 0:
        a,b = b,a%b
    return a
# enter 2 number
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

finalResult = gdc(a, b)
print("The common number is: ", finalResult)