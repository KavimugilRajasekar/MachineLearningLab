# Study of Generators in Python

# Generator function
def number_generator(n):
    for i in range(1, n + 1):
        yield i

# Using generator
gen = number_generator(5)

print("Generated Numbers:")
for num in gen:
    print(num)
