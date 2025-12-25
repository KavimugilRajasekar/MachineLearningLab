# Study of Dictionaries in Python

# Creating a dictionary
employee = {
    "id": 101,
    "name": "Kavi",
    "role": "Developer",
    "salary": 45000
}

print("Employee Details:", employee)

# Accessing values
print("Name:", employee["name"])
print("Role:", employee.get("role"))

# Modifying dictionary
employee["salary"] = 50000
employee["location"] = "Chennai"

print("Updated Employee:", employee)

# Looping through dictionary
for key, value in employee.items():
    print(key, ":", value)
