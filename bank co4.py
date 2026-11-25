class bank:
    def __init__(self):
        self.accountno = int(input("Enter account number: "))
        self.name = input("Enter name: ")
        self.type = input("Enter type : ")
        self.balance = 0
    def deposit(self):
        amount = int(input("Enter amount to be deposited: "))
        self.balance += amount
        print("Balance after deposit :", self.balance)
    def withdraw(self):
        amount = int(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("Balance after withdrawal :", self.balance)
        else:
            print("Insufficient balance")
    def display(self):
        print("Balance :", self.balance)
b = bank()
while True:
    print("\n1. Deposit \n2. Withdraw \n3. Balance \n4. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        b.deposit()
    elif ch == 2:
        b.withdraw()
    elif ch == 3:
        b.display()
    elif ch == 4:
        print("Thank you")
        break
    else:
        print("Invalid")

    
    