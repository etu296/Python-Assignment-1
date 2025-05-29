# Section 1: Simple If-Else
print("Section 1: Simple If-Else")
age = 18
if age >= 20:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
print()  # Blank line for separation

# Section 2: If-Elif-Else
print("Section 2: If-Elif-Else")
number1 = 10
number2 = 10
if number1 > number2:
    print(f"{number1} is greater than {number2}")
elif number1 == number2:
    print(f"{number1} is equal to {number2}")
else:
    print(f"{number2} is greater than {number1}")
print()

# Section 3: Nested If-Else
print("Section 3: Nested If-Else")
age = 20
citizenship = "BD"
if age >= 18:
    if citizenship == "BD":
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote due to your citizenship")
else:
    print("You are not eligible to vote due to your age")
print()

# Section 4: Triple Nested If-Else
print("Section 4: Triple Nested If-Else")
age = 20
citizenship = "BD"
area = "Dhaka"
if age >= 18:
    if citizenship == "BD":
        if area == "Dhaka":
            print("You are eligible to vote")
        else:
            print("You are not eligible to vote due to your area")
    else:
        print("You are not eligible to vote due to your citizenship")
else:
    print("You are not eligible to vote due to your age")