running = True
unsavedLogs = []

try:
    f = open("loggar.txt", "r")
except:
    f = open("loggar.txt", "w+")
f.close()



while running == True:
    choice = 0
    
    print("[1] Visa alla loggar")
    print("[2] Ny logg")
    print("[3] Spara loggar till fil")
    print("[4] Avsluta")
    
    try:
        choice = int(input("Vad vill du göra? "))
    except:
        print("Välj ett av alternativen!")
    
    if choice == 1:
        f = open("savedLogs.txt", "r")
        innehåll = f.read()
        print(innehåll)
        f.close
    elif choice == 2:
        print('Skriv din logg här!')
        newLog = input('')
        unsavedLogs.append(newLog)
    elif choice == 3:
        f = open("savedLogs.txt", "a")
        # for saveLog in unsavedLogs:
        for log in unsavedLogs:
            f.write(log + "\n")
        f.close
    elif choice == 4:
        running = False
    else:
        print("Välj ett av alternativen!")


    