import datetime

print("**********************")
print("Welcome to ATM")
print("**********************\n")

accounts = {
    1001: {"name": "User 1", "dob": "24-08-2024", "balance": 10000, "pin": 2408, "transactions": []},
    1002: {"name": "User 2", "dob": "16-07-2024", "balance": 20000, "pin": 1234, "transactions": []},
    1003: {"name": "User 3", "dob": "20-01-2024", "balance": 5000, "pin": None, "transactions": []},
}

def add_transaction(accno, type, amount):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    accounts[accno]["transactions"].append(f"{date} - {type}: Rs.{amount}")
    if len(accounts[accno]["transactions"]) > 5:
        accounts[accno]["transactions"].pop(0)

def validate_account(accno):
    if accno not in accounts:
        print("Account does not exist!")
        return False
    return True

def validate_pin(accno):
    if accounts[accno]["pin"] is None:
        print("Generate a PIN first!")
        return False
    pin = int(input("Enter PIN: "))
    if accounts[accno]["pin"] != pin:
        print("Invalid PIN!")
        return False
    return True

while True:
    print("Choose Your Option")
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. Pin Generation")
    print("4. Mini Statement")
    print("5. Balance Inquiry")
    print("6. Create New Account")
    print("7. Exit")
    option = int(input("Enter Your Option: "))
    print()
    
    if option == 1:  # Withdrawal
        accno = int(input("Enter Account Number: "))
        if validate_account(accno) and validate_pin(accno):
            amt = int(input("Enter Amount to Withdraw: "))
            if amt > accounts[accno]["balance"]:
                print("Insufficient Funds!")
            else:
                accounts[accno]["balance"] -= amt
                add_transaction(accno, "Withdrawal", amt)
                print("Withdrawal Successful!")

    elif option == 2:  # Deposit
        accno = int(input("Enter Account Number: "))
        if validate_account(accno):
            amt = int(input("Enter Amount to Deposit: "))
            accounts[accno]["balance"] += amt
            add_transaction(accno, "Deposit", amt)
            print("Deposit Successful!")
    
    elif option == 3:  # Pin Generation
        accno = int(input("Enter Account Number: "))
        if validate_account(accno):
            if accounts[accno]["pin"] is None:
                pin = int(input("Enter New PIN: "))
                cpin = int(input("Confirm PIN: "))
                if pin == cpin:
                    accounts[accno]["pin"] = pin
                    print("PIN Generated Successfully!")
                else:
                    print("PIN Mismatch!")
            else:
                print("PIN Already Exists!")

    elif option == 4:  # Mini Statement
        accno = int(input("Enter Account Number: "))
        if validate_account(accno) and validate_pin(accno):
            print(f"Name: {accounts[accno]['name']}")
            print(f"Account Number: {accno}")
            print(f"Account Balance: Rs.{accounts[accno]['balance']}")
            print("Recent Transactions:")
            for t in accounts[accno]['transactions']:
                print(t)

    elif option == 5:  # Balance Inquiry
        accno = int(input("Enter Account Number: "))
        if validate_account(accno) and validate_pin(accno):
            print(f"Account Balance: Rs.{accounts[accno]['balance']}")

    elif option == 6:  # Create New Account
        accno = max(accounts.keys()) + 1
        name = input("Enter Name: ")
        dob = input("Enter DOB (DD-MM-YYYY): ")
        balance = int(input("Enter Initial Deposit Amount: "))
        accounts[accno] = {"name": name, "dob": dob, "balance": balance, "pin": None, "transactions": []}
        print(f"Account Created Successfully! Your Account Number is {accno}")
    
    elif option == 7:  # Exit
        print("Thank you for using our ATM! Goodbye.")
        break
    
    print("**********************\n")
