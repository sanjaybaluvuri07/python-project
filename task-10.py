
# Hostel rooms: [room name, capacity, eligible group]
rooms = [
    ["Room A", 2, "Boys"],
    ["             "
     "Room B", 2, "Girls"],
    ["Room C", 3, "Boys"]
]

# Students: [name, group]
students = [
    ["Ravi", "Boys"],
    ["Arun", "Boys"],
    ["Sita", "Girls"],
    ["Kiran", "Boys"],
    ["Ravi", "Boys"],
    ["Priya", "Girls"]
]

allocated = []
assigned_names = []
duplicates = []

for student in students:
    name, group = student

    # Check duplicate assignment
    if name in assigned_names:
        duplicates.append(name)
        print(name, "- Duplicate assignment rejected")
        continue

    assigned_names.append(name)
    assigned = False

    # Find a suitable room
    for room in rooms:
        room_name, capacity, eligible_group = room

        # Count students already in the room
        count = sum(1 for a in allocated if a[1] == room_name)

        if group == eligible_group and count < capacity:
            allocated.append([name, room_name])
            print(name, "allocated to", room_name)
            assigned = True
            break

    if not assigned:
        print(name, "- No suitable room available")

# Display allocation
print("\n--- HOSTEL ALLOCATION REPORT ---")

for room in rooms:
    room_name, capacity, eligible_group = room
    occupants = [a[0] for a in allocated if a[1] == room_name]

    print(room_name, ":", occupants)
    print("Occupied:", len(occupants), "/", capacity)
    print("Vacant beds:", capacity - len(occupants))

print("\nTotal students:", len(students))
print("Successfully allocated:", len(allocated))
print("Unallocated demand:", len(students) - len(allocated) - len(duplicates))
print("Duplicate assignments:", duplicates)
++++++++++++++++++++++