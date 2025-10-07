#Huvudprogram

import psutil

def show_menu():
    running = True
    while running:
        print("\nMeny:")
        print("1. Starta övervakning")
        print("2. Lista aktiv övervakning")
        print("3. Skapa larm")
        print("4. Visa larm")
        print("5. Starta övervakningsläge")
        print("0. Avsluta")
        choice = input("Välj ett alternativ: ")
        if choice == "1":
            print("Startar övervakning...")
        elif choice == "2":
            print("Listar aktiv övervakning...")
        elif choice == "3":
            print("Skapar larm")
        elif choice == "4":
            print("Visar larm")
        elif choice == "5":
            print("Startar övervakningsläge")
        elif choice == "0":
            print("Avslutar programmet")
            running = False
        else:
            print("Ogiltigt val. Försök igen.")
        if not choice.isdigit():
            print("Skriv ett nummer, tack!")
            continue

print("Välkommen till övervakningsapplikationen!")
show_menu()
