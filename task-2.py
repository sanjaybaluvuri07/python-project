
n = int(input("Enter number of products: "))

subtotal = 0
total_tax = 0

print("\n--- Enter Product Details ---")

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    category = input("Enter category (food/electronics/other): ").lower()

    if price < 0 or quantity <= 0:
        print("Invalid price or quantity!")
        continue

    amount = price * quantity

    # Category-specific tax
    if category == "food":
        tax_rate = 5
    elif category == "electronics":
        tax_rate = 18
    else:
        tax_rate = 12

    tax = amount * tax_rate / 100

    print(name, "Amount:", amount, "Tax:", tax)

    subtotal += amount
    total_tax += tax

# Threshold discount
if subtotal >= 5000:
    discount = subtotal * 0.10
elif subtotal >= 2000:
    discount = subtotal * 0.05
else:
    discount = 0

# Maximum discount limit
if discount > 1000:
    discount = 1000

final_bill = subtotal + total_tax - discount

print("\n====== RETAIL INVOICE ======")
print("Subtotal: Rs.", round(subtotal, 2))
print("Total Tax: Rs.", round(total_tax, 2))
print("Discount: Rs.", round(discount, 2))
print("Final Bill: Rs.", round(final_bill, 2))
