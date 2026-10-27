
balance = float(input("Enter initial balance: "))
limit = float(input("Enter maximum withdrawal limit: "))
n = int(input("Enter number of transactions: "))

deposits = 0
withdrawals = 0
successful = 0
rejected = 0

if balance < 0 or limit <= 0 or n < 0:
    print("Invalid initial balance, limit, or transaction count!")
else:
    for i in range(n):
        print("\n1. Deposit")
        print("2. Withdraw")

        choice = input("Enter your choice (1 or 2): ")
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Invalid amount!")
            rejected += 1

        elif choice == "1":
            balance += amount
            deposits += amount
            successful += 1
            print("Deposit successful!")

        elif choice == "2":
            if amount > limit:
                print("Withdrawal limit exceeded!")
                rejected += 1
            elif amount > balance:
                print("Insufficient balance!")
                rejected += 1
            else:
                balance -= amount
                withdrawals += amount
                successful += 1
                print("Withdrawal successful!")

        else:
            print("Invalid transaction type!")
            rejected += 1

    print("\n--- ATM TRANSACTION SUMMARY ---")
    print("Total deposits: Rs.", round(deposits, 2))
    print("Total withdrawals: Rs.", round(withdrawals, 2))
    print("Successful transactions:", successful)
    print("Rejected transactions:", rejected)
    print("Final balance: Rs.", round(balance, 2))
