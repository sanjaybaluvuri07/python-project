
n = int(input("Enter number of subjects: "))
pass_mark = float(input("Enter minimum pass marks: "))
grace_limit = float(input("Enter maximum grace marks allowed: "))

total = 0
grace_used = 0
failed = 0

for i in range(n):
    print("\nSubject", i + 1)

    name = input("Enter subject name: ")
    marks = float(input("Enter marks out of 100: "))

    if marks < 0 or marks > 100:
        print("Invalid marks! Enter marks from 0 to 100.")
        failed += 1
        continue

    # Apply grace marks if needed
    if marks < pass_mark:
        needed = pass_mark - marks

        if needed <= grace_limit - grace_used:
            marks += needed
            grace_used += needed
            print("Grace marks awarded:", needed)
        else:
            print("Result: Fail")
            failed += 1
            continue

    print("Final marks:", marks)
    print("Result: Pass")
    total += marks

print("\n--- EXAMINATION RESULT ---")
print("Total marks:", total, "out of", n * 100)
print("Grace marks used:", grace_used)

if failed == 0:
    percentage = (total / (n * 100)) * 100
    print("Percentage:", round(percentage, 2), "%")

    if percentage >= 75:
        print("Classification: Distinction")
    elif percentage >= 60:
        print("Classification: First Class")
    elif percentage >= 50:
        print("Classification: Second Class")
    else:
        print("Classification: Pass")
else:
    print("Classification: Fail")
