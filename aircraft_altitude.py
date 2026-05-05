from aircraft import Aircraft

model = input("Enter aircraft model: ")
aircraft = Aircraft(model)

while True:
    command = input("Enter command (A for ascent, D for descent, X to exit): ")

    parts = command.split()

    if parts[0] == "X":
        break

    feet = int(parts[1])

    if parts[0] == "A":
        aircraft.ascend(feet)
    elif parts[0] == "D":
        aircraft.descend(feet)

print(f"Final altitude: {aircraft.altitude} feet")