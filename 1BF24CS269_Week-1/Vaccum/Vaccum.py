# Vacuum Cleaner Agent

rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

position = "A"

while True:
    print("\nRoom status:", rooms)
    print("Vacuum is in room:", position)

    if rooms[position] == "Dirty":
        print("Cleaning room", position)
        rooms[position] = "Clean"
    else:
        print("Room is already clean.")

    # Move to the other room
    if position == "A":
        position = "B"
    else:
        position = "A"

    # Stop when both rooms are clean
    if rooms["A"] == "Clean" and rooms["B"] == "Clean":
        print("\nBoth rooms are clean!")
        break
    
print("Name: Samriddha Bhattarai," \
    "USN: 1BF24CS269")
