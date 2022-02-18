class String:
    def __init__(self, stringg):
        self.string = stringg

    def getString(self):
        return self.string

    def printString(self):
        return self.string.upper()

s = String(input())
print(s.getString(), s.printString())
