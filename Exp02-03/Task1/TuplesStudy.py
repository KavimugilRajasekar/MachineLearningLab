# Study of Tuples in Python

# Creating a tuple
student = ("Kavi", 21, "CSE", 8.7)

print("Student Details:", student)

# Accessing elements
print("Name:", student[0])
print("Age:", student[1])

# Tuple is immutable
# student[1] = 22  # This will cause an error

# Tuple operations
print("Length:", len(student))
print("Count of 21:", student.count(21))
print("Index of 'CSE':", student.index("CSE"))
