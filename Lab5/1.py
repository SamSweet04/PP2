import re
pattern = r'^a(b*)$'
[print('MATCH') if re.findall(pattern,input()) else print("Don't match")]
