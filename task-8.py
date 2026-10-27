
scores = [90, 80, 70, 60, 50, 40]

group_size = int(input("Enter students per group: "))

if group_size <= 0:
    print("Invalid group size!")
else:
    scores.sort(reverse=True)

    number_of_groups = (len(scores) + group_size - 1) // group_size

    groups = [[] for i in range(number_of_groups)]
    totals = [0] * number_of_groups

    # Allocate each student to the lowest-total group
    for score in scores:
        best_group = -1

        for i in range(number_of_groups):
            if len(groups[i]) < group_size:
                if best_group == -1 or totals[i] < totals[best_group]:
                    best_group = i

        groups[best_group].append(score)
        totals[best_group] += score

    print("\n--- STUDENT GROUPS ---")

    for i in range(number_of_groups):
        print("Group", i + 1, ":", groups[i])
        print("Total score:", totals[i])

    difference = max(totals) - min(totals)

    print("\nHighest group total:", max(totals))
    print("Lowest group total:", min(totals))
    print("Difference between totals:", difference)
