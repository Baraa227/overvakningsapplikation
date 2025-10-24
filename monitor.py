import psutil
import time 

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

def monitoring_mode(alarms_lsit):
    print("\nÖvervakningsläge startat!")
    input("Tryck Enter för att avsluta övervakning. ")
    

    
    try:
         
         while True:
          cpu = psutil.cpu_percent(interval=1)
          memory = psutil.virtual_memory()
          disk = psutil.disk_usage('/')

         print(f"CPU: {cpu}% | Minne: {memory.percent}% | Disk: {disk.percent}%" )

         for alarm in alarms_lsit:
            if alarm["typ"]== "CPU" and cpu > alarm["nivå"]:
                print(f"VARNING: CPU-användning över {alarm['nivå']}")
            elif alarm["typ"] == "Minne" and memory.percent > alarm['nivå']:
                print(f"VARNING: Minnesanvändning över {alarm['nivå']}%")
            elif alarm["typ"] == "Disk" and disk.percent > alarm['nivå']:
                print(f"Varning: Diskanvändning över {alarm['nivå']}%")

         time.sleep(3)

    except KeyboardInterrupt:
        print("\nÅtergår till huvudmenyn. ")