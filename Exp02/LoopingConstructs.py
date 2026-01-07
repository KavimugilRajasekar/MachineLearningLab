# Study of Looping Constructs in Python

# For loop
print("For Loop Example:")
for i in range(1, 6):
    print(i)

# While loop
print("\nWhile Loop Example:")
count = 1
while count <= 5:
    print(count)
    count += 1

# Loop with list
numbers = [10, 20, 30, 40]

for num in numbers:
    print("Number:", num)

# Break and Continue
for i in range(1, 10):
    if i == 5:
        break
    print("Break Example:", i)

for i in range(1, 6):
    if i == 3:
        continue
    print("Continue Example:", i)
