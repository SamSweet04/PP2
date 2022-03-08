import re
print(re.sub(r"(\w)([A-Z])", r"\1 \2", input()))