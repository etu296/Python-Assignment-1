# Function to print a welcome message
def say_hello():
    print("Welcome to Automation Course")

# Call say_hello function
say_hello()

# Function to print a welcome message with a name
def welcome(name):
    print("Welcome to Automation Course " + name)

# Call welcome function with a name
welcome("Ebrahim")

def call_etu(age) :
    print("You are " + str(age) + " years old")
call_etu("26")

# Function with default parameter for welcome message

def number(a = 1, b = 2):
    return a + b
print(number(1, 2))