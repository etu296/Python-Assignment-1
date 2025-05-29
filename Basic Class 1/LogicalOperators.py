# Section 1: Logical AND Operator
print("Section 1: Logical AND")
x = True
y = False
print("x and y:", x and y)  # False

a = 20
b = 10
print("a > 15 and b < 12:", a > 15 and b < 12)  # True
print()

# Section 2: Logical OR Operator
print("Section 2: Logical OR")
x = True
y = False
print("x or y:", x or y)  # True

a = 20
b = 10
print("a > 25 or b < 10:", a > 25 or b < 10)  # False
print()

# Section 3: Logical NOT Operator
print("Section 3: Logical NOT")
x = False
print("not x:", not x)  # True
print()

# Section 4: Combined Logical Conditions
print("Section 4: Combined Logical Conditions")
age = 20
has_ticker = True  # Note: Corrected typo from 'has_ticker' to maintain consistency
is_adult = True

if (age >= 22 and has_ticker) or (has_ticker and is_adult):
    print("Access granted")
else:
    print("Access denied")