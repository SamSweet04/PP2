brackets = input()
stack = []
for i in range(len(brackets)):
    if brackets[i] == '[' or brackets[i] == '(' or  brackets[i] == '{':
        stack.append(brackets[i])
    elif brackets[i] == ']'or brackets[i] == ')'or brackets[i] == "}":
        if (len(stack) > 0):
            if (stack[-1] == '[' and brackets[i] == ']') or (stack[-1] == '(' and brackets[i] == ')') or (stack[-1] == '{' and brackets[i] == '}'):
                stack.pop(-1)
            else:
                stack.append(brackets[i])
if len(stack) > 0:
    print("No")
else:
    print("Yes") 
