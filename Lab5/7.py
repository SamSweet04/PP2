import re
snake_case = input()
pattern = r"(.*?)_([a-zA-z])"
def Cam(txt):
    return txt.group(1)+txt.group(2).upper()
print(re.sub(pattern,Cam,snake_case))
