room_A = input("Enter status of Room A (DIRTY/CLEAN): ").upper()
room_B = input("Enter status of Room B (DIRTY/CLEAN): ").upper()
position = input("Enter vacuum position (A/B): ").upper()

print("\n--- Vacuum Cleaner Actions ---")

if position == "A":

    if room_A == "DIRTY":
        print("Suck Room A")
        room_A = "CLEAN"
    else:
        print("Room A is already clean")

    print("Move Right to Room B")
    position = "B"

    if room_B == "DIRTY":
        print("Suck Room B")
        room_B = "CLEAN"
    else:
        print("Room B is already clean")

elif position == "B":

    if room_B == "DIRTY":
        print("Suck Room B")
        room_B = "CLEAN"
    else:
        print("Room B is already clean")

    print("Move Left to Room A")
    position = "A"

    if room_A == "DIRTY":
        print("Suck Room A")
        room_A = "CLEAN"
    else:
        print("Room A is already clean")

else:
    print("Invalid vacuum position!")

print("\n--- Final State ---")
print("Room A:", room_A)
print("Room B:", room_B)
print("Vacuum Position:", position)

if room_A == "CLEAN" and room_B == "CLEAN":
    print("Both rooms are CLEAN. STOP.")
