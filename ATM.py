savings_balance = 1000.00
current_balance = 500.00
print("Welcome to the ATM!")
print("Please choose the account type:")
print("1. Savings")
print("2. Current")
account_choice = input("Enter the number corresponding to the account: ")
if account_choice == '1':
    account_type = "Savings"
    balance = savings_balance
    amount_str = input(f"Enter the amount to withdraw from your {account_type} account: $")
    if amount_str.replace('.', '', 1).isdigit():
        amount = float(amount_str)
        if amount > 0:
            if amount > balance:
                print("Insufficient funds!")
            else:
                balance -= amount
                print(f"Withdrawal successful! New balance: ${balance:.2f}")
        else:
            print("Invalid amount entered.")
    else:
        print("Invalid amount!")
elif account_choice == '2':
    account_type = "Current"
    balance = current_balance
    amount_str = input(f"Enter the amount to withdraw from your {account_type} account: $")
    if amount_str.replace('.', '', 1).isdigit():
        amount = float(amount_str)
        if amount > 0:
            if amount > balance:
                print("Insufficient funds!")
            else:
                balance -= amount
                print(f"Withdrawal successful! New balance: ${balance:.2f}")
        else:
            print("Invalid amount entered.")
    else:
        print("Invalid amount!")
else:
    print("Invalid choice!")
if account_choice == '1' or account_choice == '2':
    if account_choice == '1':
        savings_balance = balance
    elif account_choice == '2':
        current_balance = balance
    print(f"Your {account_type} account balance is now: ${balance:.2f}")
