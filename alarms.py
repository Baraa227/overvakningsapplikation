def create_alarms(alarms_list):
    while True:
        print("\n-- Skapa larm--")
        print("1. CPU användning")
        print("2. Minnesanvändning")
        print("3. Diskanvändning")
        print("0. Tillbaka till huvudmenyn")

        choice = input("Välj ett alternativ: ")

        if choice == "0":
            print("Återgår till huvudmenyn ")
            break

        alarm_type = None
        if choice == "1":
            alarm_type = "CPU"
        elif choice == "2":
            alarm_type = "Minne"
        elif choice == "3":
            alarm_type == "Disk"
        else:
            print("Fel val, försök igen! ")
            continue

        level = input(f"Ställ in nivå för {alarm_type}-larm (0-100): ")

        if not level.isdigit():
            print("Fel: Du måste ange en siffra! ")
            continue

        level = int(level)
        if level < 1 or level > 100:
            print("Fel: Nivån måste vara mellan 0 och 100! ")
            continue

        alarms_list.append({"typ": alarm_type, "nivå": level})
        print(f"Larm för {alarm_type} användning satt till {level}%")

        break
print()

    
