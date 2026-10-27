
budget = float(input("Enter travel budget in INR: "))
rate = float(input("Enter exchange rate (1 foreign unit in INR): "))
fee_percent = float(input("Enter conversion fee percentage: "))

n = int(input("Enter number of expense categories: "))

total = 0
largest_amount = 0
largest_category = ""

for i in range(n):
    print("\nExpense", i + 1)

    category = input("Enter category: ")
    amount = float(input("Enter expense in foreign currency: "))

    if amount < 0:
        print("Invalid expense!")
        continue

    converted = amount * rate
    fee = converted * fee_percent / 100
    final_amount = converted + fee

    print("Converted amount: Rs.", round(converted, 2))
    print("Conversion fee: Rs.", round(fee, 2))
    print("Total expense: Rs.", round(final_amount, 2))

    total += final_amount

    if final_amount > largest_amount:
        largest_amount = final_amount
        largest_category = category

print("\n--- TRAVEL BUDGET REPORT ---")
print("Total spending: Rs.", round(total, 2))
print("Travel budget: Rs.", round(budget, 2))

if total > budget:
    print("Status: Budget Exceeded")
elif total < budget:
    print("Status: Within Budget")
else:
    print("Status: Budget Fully Used")

print("Largest expense category:", largest_category)
print("Largest expense: Rs.", round(largest_amount, 2))
print("Remaining budget: Rs.", round(budget - total, 2))
