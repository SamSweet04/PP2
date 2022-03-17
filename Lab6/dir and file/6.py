# import os,string
# if not os.path.exists("file"):
#     os.makedirs("file")
# for i in string.ascii_uppercase:
#     with open(i + ".txt","w") as f1:
#         f1.writelines(i)

for i in range(26):
    open(chr(i+65) + '.txt', 'w')