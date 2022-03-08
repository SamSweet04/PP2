import re
pattern = r'^[a-z]+_[a-z]+$'
[print('MATCH') if re.findall(pattern,input()) else print("Don't match")]