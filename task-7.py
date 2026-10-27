
# Classroom seating: None means vacant
classrooms = [
    [None, "RESERVED", None, None],
    [None, None, "RESERVED", None]
]

students = ["Ravi", "Sita", "Ravi", "Arun"]

assigned = []
duplicates = []

for student in students:
    if student in assigned:
        duplicates.append(student)
        print(student, "is a duplicate assignment!")
        continue

    found = False

    for room in classrooms:
        for i in range(len(room)):
            if room[i] is None:
                room[i] = student
                assigned.append(student)
                print(student, "allocated successfully!")
                found = True
                break

        if found:
            break

    if not found:
        print("No vacant seat for", student)

# Display classrooms
print("\n--- CLASSROOM SEATING ---")

for i, room in enumerate(classrooms):
    print("Classroom", i + 1, ":", room)

# Calculate capacity
total_seats = 0
reserved = 0
occupied = 0

for room in classrooms:
    total_seats += len(room)

    for seat in room:
        if seat == "RESERVED":
            reserved += 1
        elif seat is not None:
            occupied += 1

vacant = total_seats - reserved - occupied

print("\nTotal seats:", total_seats)
print("Reserved seats:", reserved)
print("Occupied seats:", occupied)
print("Vacant seats:", vacant)
print("Duplicate assignments:", duplicates)
