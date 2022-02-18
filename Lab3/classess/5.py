class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        return self.balance

    def withdraw(self, withdrawal):
        if self.balance < withdrawal:
            return False
        else: return True

A = Account('Saule', 50000)
withdrawal = 40000
print(A.deposit())
print(A.withdraw(withdrawal))