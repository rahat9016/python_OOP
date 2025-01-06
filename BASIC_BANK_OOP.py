class Account:
    def __init__(self, name, acc_no):
        self.balance = 0
        self.acc_no = acc_no
        self.name = name

    def deposit(self, name, acc_no, amount):
        self.balance += amount
        print(f"Deposited {amount} to account {acc_no} of {name}")
        self.get_balance(name, acc_no)
    
    def withdraw(self, name, acc_no, amount):
        if(self.balance < amount):
            print("Insufficient balance")
            self.get_balance(name, acc_no)
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from account {acc_no} of {name}")
            self.get_balance(name, acc_no)

    def get_balance(self, name, acc_no):
        print(f"Balance in account {acc_no} of {name} is {self.balance}")



rahat = Account("Rahat", 1234)

rahat.deposit("Rahat", 1234, 1000)
rahat.withdraw("Rahat", 1234, 490)
rahat.deposit("Rahat", 1234, 1000)