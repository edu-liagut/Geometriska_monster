"""
Projekt 3b: Geometriska mönster med ASCII
Ett menybaserat program som ritar textbaserade geometriska figurer.
Funktioner som ska implementeras:
- rita_kvadrat(sida, tecken)
- rita_triangel(hojd, tecken)
- rita_cirkel(radie, tecken)
- rita_blomma(kronblad, storlek, tecken)
- huvudprogram() med meny
"""


# === FIGURER ===

def rita_kvadrat(sida, tecken):
    for i in range(sida):
        print(tecken*sida)

    """
    Ritar en fylld kvadrat.

    Parametrar:
        sida (int): Längden på sidan (antal tecken)
        tecken (str): Tecknet som används för att rita
    """
    # TODO: Implementera funktionen
    # Tips: for i in range(sida): print(tecken * sida)
    pass


def rita_triangel(hojd, tecken):
    for i in range(1, hojd+1):
        print(tecken*1)
    """
    Ritar en rätvinklig triangel.

    Parametrar:
        hojd (int): Triangelns höjd (antal rader)
        tecken (str): Tecknet som används för att rita
    """
    # TODO: Implementera funktionen
    # Tips: for i in range(1, hojd + 1): print(tecken * i)
    pass


def rita_cirkel(radie, tecken):
    for y in range(-radie, radie):
        for x in range(-radie, radie):
            if x*x +y*y <= radie*radie:
                print(tecken, end=" ")
            else:
                print("  ", end=" ")
            print()
    """
    Ritar en cirkel med ASCII-tecken.
    Använder Pythagoras sats (x² + y² ≤ r²) för att avgöra om en punkt är innanför.

    Parametrar:
        radie (int): Cirkelns radie
        tecken (str): Tecknet som används för att rita
    """
    # TODO: Implementera funktionen
    # Tips: Loopa y från -radie till radie
    #       Loopa x från -radie till radie
    #       Kolla om x*x + y*y <= radie*radie
    #       Skriv ut tecken + mellanslag eller två mellanslag
    #       Använd end=" " för att slippa radbrytning
    #       Glöm inte print() efter varje y-varv
    pass


def rita_blomma(kronblad, storlek, tecken):
    for k in range(kronblad):
        print(f"Kronblad{k+1}")
        rita_kvadrat(storlek,tecken)
        print()
    """
    Ritar en enkel blomma genom att kombinera flera kvadrater.

    Parametrar:
        kronblad (int): Antal kronblad
        storlek (int): Storleken på varje kronblad
        tecken (str): Tecknet som används för att rita
    """
    # TODO: Implementera funktionen
    # Tips: En enkel blomma kan vara flera kvadrater bredvid varandra
    # Exempel: rita_kvadrat(storlek, tecken) flera gånger
    pass


# === HUVUDPROGRAM ===

def huvudprogram():
    while True:
        val = input("Välj:")
        print("\n --- ASCII MÖNSTER ---")
        print("1. Rita kvadrat")
        print("2. Rita triangel")
        print("3. Rita cirkel")
        print("4. Rita blomma")
        print("5. Avsluta")
        if val == "1":
            sida= int(input("Sida: "))
            tecken = input("Tecken: (t.ex *): ")
            rita_kvadrat(sida,tecken)
            pass
        elif val == "2":
            hojd = int(input("Höjd: "))
            tecken = input("Vilket tecken?: ")
            rita_triangel(hojd,tecken)
            pass
        elif val == "3":
            radie = int(input("Radien: "))
            tecken = input("Ange tecken: ")
            rita_cirkel(radie,tecken)
            pass
        elif val == "4":
            kronblad = int(input("Hur många kronblad: "))
            storlek  = int(input("Storlek: "))
            tecken = input("Ange ett tecken: ")
            rita_blomma(kronblad,storlek,tecken)
            pass
        elif val == "5":
            print("Hejdå")
        break
    else:
        print("Ogiltigt svar")

# === EXTRA FUNKTIONER FÖR UTMANINGAR ===

def rita_ihalig_kvadrat(sida, tecken):
    """
    Ritar en ihålig kvadrat (endast kantlinjen).
    """
    # TODO: Implementera funktionen
    # Tips: Första och sista raden: tecken * sida
    #       Mellanrader: tecken + " "*(sida-2) + tecken
    pass


def rita_omvand_triangel(hojd, tecken):
    """
    Ritar en omvänd triangel (basen upp, spetsen ner).
    """
    # TODO: Implementera funktionen
    # Tips: for i in range(hojd, 0, -1): print(tecken * i)
    pass


def rita_diamant(hojd, tecken):
    """
    Ritar en diamant (två trianglar som möts).
    """
    # TODO: Implementera funktionen
    # Tips: Först en triangel uppåt, sedan en nedåt (utan mittenraden två gånger)
    pass


def spara_till_fil(figur_namn, innehall, filnamn="figur.txt"):
    """
    Sparar en ASCII-figur till en textfil.

    Parametrar:
        figur_namn (str): Namn på figuren
        innehall (str): Figurens textinnehåll
        filnamn (str): Namn på filen att spara till
    """
    # TODO: Implementera funktionen
    # Tips: Använd filhantering från projekt 1
    pass


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()