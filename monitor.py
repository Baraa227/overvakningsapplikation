import psutil

def list_active_monitoring(monitoring_active):
    if not monitoring_active:
        print("\nIngen övervakning är aktiv just nu.")
    else:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        print("\nAktiv övervakning:")
        print(f"CPU-användning: {cpu}%")
        print(f"Minnesanvändning: {memory.percent}%")
        print(f"Diskanvändning: {disk.percent}%")

    input("Tryck på Enter för att bekräfta ")
    print("Du har bekräftat ")
    input("Tryck på Enter för att återgå till meny ")