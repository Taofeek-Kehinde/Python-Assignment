from pybank import *

message = """1. Register
2. Login
3. Calculate Balance
4. Apply Interest
5. Summary
6. Exit : """

while True:
    user_input = input(message)
    match user_input:
        case "1":
            email = input("Enter email: ")
            password = input("Enter password: ")
            if validate_email(email) and is_strong_password(password):
                print("Registration successful")
            else:
                print("Registration failed")
                
        case "2":
            email = input("Enter email: ")
            password = input("Enter password: ")
            if validate_email(email) and is_strong_password(password):
                print("Login successful")
            else:
                print("Login failed")
                
        case "3":
            transactions = []
            amount = float(input("Enter amount or 0 to stop: "))
            while amount != 0:
                transactions.append(amount)
                amount = float(input("Enter amount or 0 to stop: "))
            total_transactions = calculate_balance(transactions)
            print("Your balance is ", total_transactions)
            
        case "4":
            try:
                balance = float(input("Enter current balance: "))
                rate = float(input("Enter interest rate (as decimal, e.g., 0.05 for 5%): "))
                years = int(input("Enter number of years: "))
                new_balance = apply_interest(balance, rate, years)
                print(f"Balance after {years} years: {new_balance}")
            except ValueError as error:
                print(f"Error: {error}")
                
        case "5":
            transactions = []
            print("Enter transactions (type 'credit' or 'debit' followed by amount)")
            print("Enter 'stop' to finish")
            
            while True:
                trans_type = input("Transaction type (credit/debit/stop): ").lower()
                if trans_type == "stop":
                    break
                if trans_type not in ["credit", "debit"]:
                    print("Invalid type. Please enter 'credit' or 'debit'")
                    continue
                    
                try:
                    amount = float(input("Enter amount: "))
                    if amount < 0:
                        print("Amount cannot be negative. Please enter a positive amount.")
                        continue
                    transactions.append([trans_type, amount])
                except ValueError:
                    print("Invalid amount. Please enter a number.")
                    continue
            
            if transactions:
                summary = get_transaction_summary(transactions)
                print("\n=== The transaction Summary ===")
                for item in summary:
                    print(f"{item[0]}: {item[1]}")
            else:
                print("No transactions entered")
                
        case "6":
            print("Thank you for using PyBank. Goodbye!")
            break
            
        case _:
            print("Invalid option. Please choose 1-6")
