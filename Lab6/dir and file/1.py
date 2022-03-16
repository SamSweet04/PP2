import os
my_url = os.getcwd()
print("Only dir:")
print([target for target in os.listdir('.') if os.path.isdir(target)])
print("File and dir:")
for target in os.listdir('.'):
    print(target)
print("Files in a specified path:")
print([ target for target in os.listdir('.') if not os.path.isdir(target)])