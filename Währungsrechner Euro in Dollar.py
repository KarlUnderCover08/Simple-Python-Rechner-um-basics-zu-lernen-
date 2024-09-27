# 1 Euro ist (Stand 24.09.2024) 1.1136 USD wert!
print("Herzlich wilkommen zum Währungsrechner\n")
print("Wir werden hier Euro in Dollar umrechnen")
euro = float(input("Bitte geben sie den Betrag den sie umrechnen wollen an. (In Euro)\n"))
dollar = float(1.1136)
kurs = euro * dollar
kurs = round(kurs, 2)
print(f"{euro} € sind umgerechnet {kurs} $")
input("Drücken sie die Enter Taste zum beenden...")

