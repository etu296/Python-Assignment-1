# Section 1: Basic Shorthand Conditional (Commented)
# Get user input
x = int(input("Enter a number: "))
print("Positive" if x > 0 else "Negative")  # Commented in original
if x > 10 :
    print("Hello")
else:
    print("Hi")
# Section 2: Nested If-Else and Shorthand Equivalent
print("Section 2: Nested If-Else and Shorthand")
if x > 10:
    print("Entered number is greater than 10")
else:
    if x < 5 :
        print("Entered number is less than 5")
    else:
        print("Entered number is not in the range")

# Nested shorthand conditional
# result = "Large" if x > 10 else "Small" if x < 5 else "Medium"
# print(result)
# Nested If-Else (Complex Conditions)
print("Section 3: Nested If-Else")
age = int(input("Enter your age: "))
citizen = str(input("Enter your citizen's name: "))
if age >= 18:
    if citizen == "BD":
     print("Eligible for vote")
    else:
     print("Not Eligible due to Citizen")
else:
   print("not Eligible due to age")
# Shorthand
result = "Eligible to vote" if age >= 18 and citizen == "BD" else "Ineligible due to citizenship" if age >= 18 else "Ineligible due to age"
print(result)  # Output: Eligible to vote


