# Study of Functions in Python

# Function without arguments
def greet():
    print("Welcome to Python Programming")

greet()

# Function with arguments
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)

# Function with default argument
def student_info(name, dept="CSE"):
    print("Name:", name)
    print("Department:", dept)

student_info("Kavi")
student_info("Arun", "ECE")
