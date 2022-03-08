import re
pattern = 'a.*b$'
[print('MATCH') if re.findall(pattern,input()) else print("Don't match")]