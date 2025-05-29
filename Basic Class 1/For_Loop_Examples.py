# Section 1: Simple for loop over a list
fruits = ["Apple", "Orange", "Test"]
print("Section 1: Simple for loop")
for x in fruits:
    print(x)
print()  # Blank line for separation
# Section 2: For loop with range
print("Section 2: Range loop with even/odd check")
for x in range(10, 30, 5):
    print(x)
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")
print()

# Section 3: Nested for loops
colors = ["red", "green", "yellow"]
fruits = ["Apple", "Orange", "Test"]
print("Section 3: Nested loops")
for x in colors:
    for y in fruits:
        print(x, y)
print()

# Section 4: For loop with continue
fruits = ["Apple", "Orange", "Test"]
actual_fruits = []
print("Section 4: Loop with continue")
for x in fruits:
    if x == "Test":
        continue
    print(x)
    actual_fruits.append(x)
print(f"Actual fruits: {actual_fruits}")
print()

# Section 5: For loop with break
fruits = ["Apple", "Orange", "Test"]
print("Section 5: Loop with break")
for x in fruits:
    print(x)
    if x == "Orange":
        break