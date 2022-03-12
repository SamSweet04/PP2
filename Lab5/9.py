import re
txt = input()
print(re.findall("[A-Z][^A-Z]*",txt))