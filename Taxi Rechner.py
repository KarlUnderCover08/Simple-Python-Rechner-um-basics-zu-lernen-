#Taxi Rechner 
def print_taxi_banner():
    banner = """
     _____________________________________________________
    |                                                     |
    |        _____     _____     _______________          |
    |       |     |   |     |   |  _____________|         |
    |_______|     |___|     |___| |  |    |               |
    |       |     |   |     |   | |  |    |               |
    |_______|     |___|     |___|_|  |____|               |
    |      ________________        _______                |
    |     /              /\\       |     |                 | 
    |____/______________/  \\______|_____|_________________|
    |_____________________________________________________|
    |                                                     |
    |          WILKOMMEN BEIM TAXI SERVICE                |
    |_____________________________________________________|
    """
    
    print(banner)

print_taxi_banner()
print("Wilkommen beim Taxi service Gießen\n")
ziel = input("Wo soll es denn hingehen?\n")
km = float(input(f"Okay nach {ziel} und wie viele Kilometer ist das entfernt?\n"))
grundgebühr = float(5.99)
PproKm = float(2.50)
preis = PproKm * km + grundgebühr 
print(f"Okay das macht dann {preis}€")
input("Einen schönen Tag noch!")
hfdhdfh