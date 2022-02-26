from datetime import datetime 
a = datetime(2023,12,24,14,24,24)
b = datetime(2023,12,23,14,24,24)
t = a - b
print(t.days*24*3600 + t.seconds)

