import re

# A valid credit card from ABCD Bank has the following characteristics:

# ► It must start with a 4, 5 or 6.
# ► It must contain exactly  16 digits.
# ► It must only consist of digits (0-9).
# ► It may have digits in groups of 4, separated by one hyphen "-".
# ► It must NOT use any other separator like ' ' , '_', etc.
# ► It must NOT have  4 or more consecutive repeated digits.

total = int(input())
text = []
pattern = r'^(?=[456])(?!.*(\d)(-?\1){3})\d{4}(-?\d{4}){3}$'

for _ in range(total):
    value = input()
    text.append(value)
    
for num in text:
    result = re.match(pattern, num)
    if result:
        print("Valid")
    else:
        print("Invalid")   