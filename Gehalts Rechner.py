for _ in range(100000):
    print("Willkommen im Gehaltsrechner!")
    week = 5
    wochen = 4
    stunden = 8
    tage = 20 
    Monate = 12 
    stundenlohn = input("Bitte gib deinen Stundnelohn ein\n")
    tag = stunden * float(stundenlohn)
    woche = week * float(tag)
    monat = woche * float(wochen)
    jahr = monat * float(Monate)
    tag = round(tag, 2)
    woche = round(tag, 2)
    wochen = round(woche, 2)
    Monat = round(monat, 2)
    jahr = round(jahr, 2)
    print(f"{stundenlohn}€ verdienst du in der Stunde.")
    print(f"{tag}€ verdienst du am Tag.")
    print(f"{woche}€ verdienst du in der Woche.")
    print(f"{monat}€ verdienst du im Monat.")
    print(f"{jahr}€ verdienst du im Jahr.")
    print("")
    print("")
input("Drücke die enter Taste zum beenden...")



