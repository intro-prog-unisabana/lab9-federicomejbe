from aircraft import Aircraft

model = input("Enter aircraft model: ")
aircraft = Aircraft(model)

while True:
    command = input("Enter command (A for ascent, D for descent, X to exit): ")

    if command == "X":
        break

    parts = command.split()
    action = parts[0]
    feet = int(parts[1])

    if action == "A":
        aircraft.ascend(feet)
    elif action == "D":
        aircraft.descend(feet)

print(f"Final altitude: {aircraft.altitude} feet")