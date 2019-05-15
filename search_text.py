import re

# . gives all characters except the new line
# \d gives all digits 0-9
# \D gives everything except digits 0-9
# \w gives word characters a-z A-Z 0-9 _
# \W gives everything except word characters a-z A-Z 0-9 _
# \s gives space, tab and new line
# \S except space, tab and new line

# \b Word boundary  ( word after space or on a new line )
# \B Not Word boundary
# ^ Start of a string
# $ End of a string

# Quantifiers
# * -->      0 or More
# + -->      1 or More
# ? -->      0 or 1
# {3} -->    Can give exact number
# {1, 5}-->  Min 1 & Max 5

text = """ABCJKLDEFGHIJKL

0342-88-22-629
0332-62-43-662
"""

#pattern = re.compile(r"\d\d\d\d.\d\d.\d\d.\d\d\d")
#matches = pattern.finditer(text)

#for match in matches:
#    print(match)

with open("data.txt", "r") as f:
    all_text = f.read()

# Using Character Set in between for specific character
pattern = re.compile(r"hello", re.IGNORECASE)
matches = pattern.finditer(all_text)
for match in matches:
    print(match.group(0))

