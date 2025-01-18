class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit

    def withdraw(self, withdrawal):
        self.balance -= withdrawal

    def display_balance(self):
        print(self.balance)


AdamBank = BankAccount("Adam", "Smith", "123456", "Checking", "1234", 1000.0)
AdamBank.deposit(96)
AdamBank.withdraw(25)
AdamBank.display_balance()
