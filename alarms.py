
import json
import os

ALARMS_FILE = "alarms.json"

def create_alarms(alarms_list):
    while True:
        print("\n Skapa larm ")
        print("1. CPU användning ")
        print("2. Minnesanvändning ")
        print("3. Diskanvändning ")
        print("4. Tillbaka till huvudmenyn ")

        choice = input("Välj ett alternativ: ")

        if choice == "4":
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
            print("OPS! Nivån måste vara mellan 1 och 100! ")
            continue

        alarms_list.append({"typ": alarm_type, "nivå": level})
        print(f"Larm för {alarm_type} användning satt till {level}%")

        break
print()

def load_alarms():
    if os.path.exists(ALARMS_FILE):
        with open(ALARMS_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def wait_for_key():
    import os
    if os.name == "nt":
        import msvcrt
        print("\nTryck valfri tangent för att gå tillbaka till huvudmenyn")
        msvcrt.getech()
    else:
        input("\nTryck Enter för att gå tillbaka till huvudmenyn ")

def show_alarms(alarms_list):
    print("\nAktiva alarm ")
    valid_alarms = [alarm for alarm in alarms_list if alarm.get("typ")]

    if not valid_alarms:
        print("Inga larm är konfiguerade ännu. ")
        input("\nTryck Enter för att återgå till huvudmenyn ")
        return

    sorted_alarms = sorted(valid_alarms, key=lambda x: x["typ"])
    
    print("\nKonfiguerade larm: ")
    for alarm in sorted_alarms:
        print(f"{alarm['typ']} larm {alarm['nivå']}%")

    input("\nTryck Enter för att bekräfta. ")
    input("Tryck Enter för att återgå till meny. ")
    

