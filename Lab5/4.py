import re
pattern = '[A-Z]+[a-z]+$'
[print('MATCH') if re.findall(pattern,input()) else print("Don't match")]