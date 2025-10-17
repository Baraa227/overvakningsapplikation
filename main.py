#Huvudprogram

import psutil
from monitor import list_active_monitoring

monitor_active = False
menu_is_running = True

while menu_is_running:
        print("\nMeny:")
        print("1. Starta övervakning")
        print("2. Lista aktiv övervakning")
        print("3. Skapa larm")
        print("4. Visa larm")
        print("5. Starta övervakningsläge")
        print("0. Avsluta")

        menu_choice = input("Välj ett alternativ: ")

        if menu_choice == "1":
            monitor_active = True
            print("Startar övervakning...")
            input("Tryck på Enter för att återgå till menyn.")

        elif menu_choice == "2":
            list_active_monitoring(monitor_active)

        elif menu_choice == "3":
            print("Skapar larm")
            input("Tryck på Enter för att återgå till menyn.")

        elif menu_choice == "4":
            print("Visar larm")

        elif menu_choice == "5":
            print("Startar övervakningsläge")
            input("Tryck på Enter för att återgå till menyn.")

        elif menu_choice == "0":
            print("Avslutar programmet")
            menu_is_running = False
            input("Tryck på Enter för att avsluta.")

        else:
            print("Ogiltigt val. Försök igen.")
        if not menu_choice.isdigit():
            print("Skriv ett nummer, tack!")
            continue

print("Välkommen till övervakningsapplikationen!")
