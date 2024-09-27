# Grundprinzip:
# Werte: Menge an gefahrenen Kilometern, Geschwindigkeit des Autos (durchschnittlich), Liter an verbrauchtem Benzin
# Ein Auto verbraucht auf 1km Strecke 0.055 Liter Benzin bei einer Geschwindigkeit von 100kmh
for _ in range(10000000000000):
    print("Hinweis: Die durchschnittsgeschwindigkeit des Autos beträgt bei diesem Rechner immer 100kmh\n")
    strecke = float(input("Wie lang ist die Strecke die gefahren werden soll?(in km)\n"))
    verbrauchProKilometer = 0.055 
    LiterVerbrauch = strecke * verbrauchProKilometer
    print (f"{LiterVerbrauch} Liter Benzin werden verbraucht")

input("Hier muss was stehen das es sich nd instant schließt. D:")