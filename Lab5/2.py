import re
pattern = r'ab{2,3}'
[print('MATCH') if re.findall(pattern,input()) else print("Don't match")]