class BankAccount:
    bank_name = "PyBank"
    balance= 0.0
    total_accounts = 0

    class ValueError(BaseException):         #create exception 
        pass

    @staticmethod
    def validate_amount(amount):
        try:
            if float(amount)<=0:
                print("Please enter amount more than 0.0!")
                return False
            return True
        except:
            print("Please enter amount (Numbers)!")
            return False
        
    @staticmethod
    def format_money(amount):
        return f"{amount:,.2f}"

    @staticmethod
    def is_valid_owner(name):
        if "".join(name.split()).isalpha() and len(name)>2:
            return True
        else:
            print("Enter valid name only Characters")
            return False
        
    def __init__(self,owner,balance):
            if self.validate_amount(balance) and self.is_valid_owner(owner):
                self.owner = owner
                self.balance = balance
                self.transaction = []
                BankAccount.total_accounts+=1
                print("Account Created SuccessFully!")

    def deposit(self, amount):
            if self.validate_amount(amount):
                self.balance+=amount
                self.transaction.append(("Deposit",amount,self.balance))
                print("Deposit SuccessFully")
                return self.balance
            else:
                 return 0

    def withdraw(self, amount):
            if self.validate_amount(amount) and self.balance>float(amount):
                self.balance-=float(amount)
                self.transaction.append(("Withdraw",amount,self.balance))
                print("Withdraw SuccessFully")
                return self.balance
            else:
                 print("Insufficient Balance")

    def summary(self):
        print(f"{self.owner} . {self.format_money(self.balance)}")

    def transfer_to(self, other, amount):
            if self.validate_amount(amount) and self.balance<amount:
                raise ValueError
            self.withdraw(amount)
            other.deposit(amount) 
            print("Transfer SuccessFully")
            return True

    def statement(self):
         print(f"--------{self.owner} Statements------")
         for i in self.transaction:
              print(f"{i[0]} - {self.format_money(i[1])} - {self.format_money(i[2])}")

