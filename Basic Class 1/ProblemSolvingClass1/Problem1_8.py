# 1. Python Program to Swap Two Variables
num1 = 1
num2 = 2
print("Before Swap Two Variables" , num1, num2)
#Swap Two Variables
number = num1
num1 = num2
num2 = number
print("After Swap Two Variables" , num1, num2)

# 2. Python Program to Swap Two Variables Without a Temporary Variable
num1 = 1
num2 = 2
print("Before Swap Two Variables" , num1, num2)
#Swap Two Variables using tuple
num1, num2 = num2, num1
print("After Swap Two Variables" , num1, num2)

# 3. Python Program to Find the Largest of Three Numbers
num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))
num3 = int(input("Enter a number 3: "))
if (num1 >= num2) and (num1 >= num3):
    print("large", num1)
elif (num2 >= num1) and (num2 >= num3):
    print("Large", num2)
else:
    print("large", num3)

# 4.Python Program to Calculate the Square Root
a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
print("The Square Root of a^b", a**b)

# 5.Python Program to Calculate the Area of a Triangle
base = float(input("Enter Triangle's base: "))
height = float(input("Enter Triangle's height: "))
area = base * height / 2
print("The area of a triangle is ", area)

# 6.Python Program to Check if a Number is Prime
number = int(input("Enter a number : "))
if number % 2 == 0:
    print(number, " is not a prime number")
else:
    print("prime number")

# 7.Python Program to Print All Prime Numbers in an Interval
startNumber = int(input("Enter a start number : "))
endNumber = int(input("Enter a end number : "))
for num in range(startNumber, endNumber+1):
    if num>1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

# 8.Python Program to Find the Sum of Natural Numbers
# Sum of first n natural numbers = n * (n + 1) / 2
n = int(input("Enter a number : "))
if n > 0:
    sumNumber = n * (n+1)/2
    print("The sum of ", n, " is ", sumNumber)
else:
    print("please enter a positive number")








