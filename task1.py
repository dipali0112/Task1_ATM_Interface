class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("This is Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("This is Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def transfer(self, target_account, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            print(f"Transferred ${amount} to target account. New balance: ${self.balance}")
        else:
            print("This is Invalid transfer amount or insufficient funds.")

def main():
    atm = ATM()
    while True:
        print("\nATM Interface")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transfer")
        print("5. Exit")
        choice = input("Choose an one option: ")

        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            atm.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            atm.withdraw(amount)
        elif choice == '3':
            atm.check_balance()
        elif choice == '4':
            target_balance = float(input("Enter target account balance: "))
            target_account = ATM(target_balance)
            amount = float(input("Enter transfer amount: "))
            atm.transfer(target_account, amount)
            print(f"Target account new balance: ${target_account.balance}")
        elif choice == '5':
            print("Thank you for using the ATM. Please!! collect Your card")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


