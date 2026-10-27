
consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

# Validate charges
if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid charges!")
else:
    total = consultation + diagnostic + treatment

    # Apply concession
    if total >= 5000:
        concession = total * 0.10
    else:
        concession = 0

    bill = total - concession

    print("Total Charges:", total)
    print("Concession:", concession)
    print("Final Bill:", bill)

    paid = float(input("Enter amount paid: "))

    # Validate payment
    if paid < 0 or paid > bill:
        print("Invalid payment amount!")
    elif paid == bill:
        print("Patient Classification: Fully Paid")
    elif paid > 0:
        print("Patient Classification: Partially Paid")
    else:
        print("Patient Classification: Unpaid")
