# Study of File Input and Output in Python

# Writing to a file
with open("sample.txt", "w") as file:
    file.write("This is a sample file.\n")
    file.write("Python File Handling Example.\n")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()

print("File Content:")
print(content)

# Appending to a file
with open("sample.txt", "a") as file:
    file.write("Appending new content.\n")
