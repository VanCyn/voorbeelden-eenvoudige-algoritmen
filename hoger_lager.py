import random

ronde = 0  # huidige ronde
totaal_raad = 0  # totaal aantal gokken over alle rondes
ronde_raad = 0  # totaal aantal gokken in deze ronde
beste = 1000  # beste rondescore tot nu toe


print()
print("------------------------------------------------")
print("*    Welkom bij Wt's Hoger-lager spelletje     *")
print("*                                              *")
print("* De computer kiest zometeen een getal tussen  *")
print("* de 1 en de 100. Je mag een getal raden en de *")
print("* computer zal je vertellen of het te hoog,    *")
print("* te laag of precies goed is.                  *")
print("*                                              *")
print("* Probeer in zo min mogelijk stappen het getal *")
print("* te raden. Wat is een goede strategie?        *")
print("------------------------------------------------")
print()

input("Druk op <enter> om het hoger-lager spel te starten")


nog_een_keer = "j"

# ronde
while nog_een_keer == "j":
    ronde += 1
    print()
    print("----------------------------------")
    print("Ronde ", ronde)
    print("----------")
    computer_getal = random.randint(1, 100)
    print("De computer heeft een getal tussen de 1 en 100 gekozen.")
    print()
    getal = -1
    raad = 0

    # raden
    while getal != computer_getal:

        print()

        # raden met error handling
        getal = -1
        while getal < 1 or getal > 100:
            try:
                getal = int(input("Welk getal raad je? "))
                if getal < 1 or getal > 100:
                    print("tussen de 1 en de 100 graag...")
            except:
                print("Kies een geldig getal...")

        raad += 1

        if getal > computer_getal:
            print("Dat is te hoog")
            print("Je hebt nu", raad, "keer geraden")

        elif getal < computer_getal:
            print("Dat is te laag")
            print("Je hebt nu", raad, "keer geraden")

        else:
            # Geraden. Werk de administratie bij
            print("Geraden! Het was inderdaad:", computer_getal)
            print()

            print("******")
            print("Je hebt het geraden in", raad, "keer")
            totaal_raad += raad
            print("Je gemiddelde over alle rondes is:", totaal_raad / ronde)
            if raad < beste:
                beste = raad
            print("Je beste score tot nu toe is:", beste, "keer raden")
            print("******")
            print()

            nog_een_keer = input("Wil je nog een ronde (j/n)? ")


print()
print("Adios! Moge vele appeltaarten uw pad kruisen vandaag.")
