# ATM Console-Based Application

## Overview
This is a simple console-based ATM system implemented in Python. It allows users to perform various banking operations such as withdrawals, deposits, PIN generation, mini statements, balance inquiries, and account creation.

## Features
- **Withdrawal**: Withdraw money from an account after entering a valid PIN.
- **Deposit**: Deposit money into an existing account.
- **PIN Generation**: Set up a new PIN for accounts that do not have one.
- **Mini Statement**: View the last five transactions along with account details.
- **Balance Inquiry**: Check the current account balance.
- **Account Creation**: Open a new account with a name, date of birth, and initial deposit.
- **Secure Transactions**: PIN verification for sensitive operations.
- **Transaction History**: Stores recent transactions for each account.

## Requirements
- Python 3.x

## Usage
1. Run the script using Python:
   ```sh
   python atm.py
   ```
2. Follow the on-screen instructions to select an operation.
3. Enter account details and PIN as prompted.

## Possible User Interactions
### 1. Withdrawal
- Enter account number and PIN.
- Enter the withdrawal amount.
- If sufficient balance is available, the withdrawal is processed.

### 2. Deposit
- Enter account number.
- Enter the amount to deposit.
- The balance is updated accordingly.

### 3. PIN Generation
- Set up a PIN for accounts that do not have one.
- PIN confirmation is required.

### 4. Mini Statement
- Displays the account holder’s name, balance, and the last five transactions.

### 5. Balance Inquiry
- Displays the current balance after PIN authentication.

### 6. Account Creation
- Enter name, date of birth, and initial deposit.
- A new account number is assigned.

### 7. Exit
- Ends the ATM session.

## Example Run
```
**********************
Welcome to ATM
**********************
Choose Your Option
1. Withdrawal
2. Deposit
3. Pin Generation
4. Mini Statement
5. Balance Inquiry
6. Create New Account
7. Exit
```

## Future Enhancements
- Implement database storage for accounts instead of using in-memory storage.
- Introduce authentication using a card number system.
- Add multi-user access with login credentials.
- Improve UI with a graphical interface.

## License
This project is open-source and can be modified or distributed freely.

---


