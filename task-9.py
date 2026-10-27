
n = int(input("Enter number of students: "))
quota = int(input("Enter scholarship quota: "))

eligible = []

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    marks = float(input("Enter academic marks (%): "))
    attendance = float(input("Enter attendance (%): "))
    income = float(input("Enter family income (Rs.): "))

    # Stage 1: Validate inputs
    if not (0 <= marks <= 100 and
            0 <= attendance <= 100 and income >= 0):
        print("Invalid details!")
        continue

    # Stage 2: Check eligibility
    if marks >= 75 and attendance >= 80 and income <= 200000:
        eligible.append([name, marks, attendance, income])
        print("Eligible for scholarship")
    else:
        print("Not eligible")

# Stage 3: Rank eligible students by marks
eligible.sort(key=lambda student: student[1], reverse=True)

# Stage 4: Select candidates within quota
if quota < 0:
    print("Invalid scholarship quota!")
else:
    selected = eligible[:quota]

    print("\n--- SCHOLARSHIP SHORTLIST ---")
    print("Total eligible students:", len(eligible))
    print("Scholarship quota:", quota)

    if selected:
        for rank, student in enumerate(selected, start=1):
            print(rank, student[0], "- Marks:", student[1], "%")
    else:
        print("No students selected")

    print("Total selected:", len(selected))
