# Study of Regular Expressions in Python

import re

text = "My email is kavi123@gmail.com and my number is 9876543210"

# Find email
email = re.findall(r'\S+@\S+', text)
print("Email Found:", email)

# Find phone number
phone = re.findall(r'\b\d{10}\b', text)
print("Phone Number Found:", phone)

# Replace digits
masked_text = re.sub(r'\d', '*', text)
print("Masked Text:", masked_text)
