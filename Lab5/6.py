import re
s = input()
print(re.sub("[ ,.]", ":", s))