from .account import BankAccount

def main():
    accounts = {}
    acc = 1
    while True:
        choice = input("1.Open Account\n2.Deposit\n3.Withdraw\n4.transfer\n5.list\n6.Quit:")
        print(choice)
        if choice == "1":
            owner = input("Enter your name : ")
            try:
                balance = int(input("Enter your initial balance: "))
            except:
                print("Enter valid amount")
                continue
            acc_name = "acc"+str(acc)
            # print(acc_name)
            if BankAccount.is_valid_owner(owner) and BankAccount.validate_amount(balance):
                acc_name = BankAccount(owner,balance)
                accounts["acc"+str(acc)]=acc_name
                acc+=1   
                print(accounts)
            else:
                print("Account Not Created!") 
                                #i changed here bcoz name 
        elif choice== "2":
            acc_name = input("Enter your account name : ")
            try:
                balance = int(input("Enter amount: "))
            except:
                print("Enter valid amount")
                continue

            if acc_name in accounts:
                accounts[acc_name].deposit(balance)
            else:
                print("You Don't have account")

        elif choice == "3":
            acc_name = input("Enter your account : ")
            balance = input("Enter amount : ")
            if acc_name in accounts:
                accounts[acc_name].withdraw(balance)
            else:
                print("You Don't have account")

        elif choice == "4":
            acc_name = input("Enter your account : ")
            toacc_name = input("Enter to account : ")
            balance = int(input("Enter your amount : "))
            if acc_name in accounts and toacc_name in accounts:
                accounts[acc_name].transfer_to(accounts[toacc_name],balance)
            else:
                if acc_name in acc_name:
                    print("second acc is not valid")
                else:
                    print("first acc is not valid")

        elif choice=="5" :
            print("--------ALL ACCOUNTS--------")
            for i,j in accounts.items():
                print(f"account name : {i} | account owner : {j.owner} | account balance : {j.balance}")
        else:
            break


if __name__ == "__main__":
    main()

# acc1 = BankAccount("abc",1000)
# acc2 = BankAccount("Rahul",15000)
# acc3 = BankAccount("Ravi",18000)

# print(f"{acc1.owner} - {acc1.balance}")
# print(f"{acc2.owner} - {acc2.balance}")
# print(f"{acc3.owner} - {acc3.balance}")

# acc1.balance = 9000000

# print(f"{acc1.owner} - {acc1.balance}")
# print(f"{acc2.owner} - {acc2.balance}")
# print(f"{acc3.owner} - {acc3.balance}")

# acc1.summary()

# acc1.deposit(500)               # it will deposit amout into acc1 user 
# BankAccount.deposit(acc1, 500)   # it will also to same thing just we are calling instance method using class so we have to pass object manually 
# # acc1.withdraw(100000000)

# print(f"{acc1.owner} - {acc1.balance}")


# print(BankAccount.validate_amount(-900))

