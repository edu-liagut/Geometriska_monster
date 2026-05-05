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

def rita_kvadrat(sida, tecken, farg):
    for i in range(sida):
        print(farg + tecken*sida)
    pass

def rita_triangel(hojd, tecken, farg):
    for i in range(1, hojd+1):
        print(farg + tecken*i)
    pass


def rita_cirkel(radie, tecken, farg):
    for y in range(-radie, radie + 1):
        for x in range(-radie, radie + 1):
            if x*x + y*y <= radie*radie:
                print(farg + tecken + " ", end="")
            else:
                print("  ", end="")
        print()
    pass


def rita_blomma(kronblad, storlek, tecken, farg):
    for k in range(kronblad):
        print(farg + f"Kronblad {k+1}")
        rita_kvadrat(storlek,tecken,farg)
        print()
    pass

ROD    = "\033[31m"
GRON   = "\033[32m"
GUL    = "\033[33m"
BLA    = "\033[34m"
RESET  = "\033[0m"

# === HUVUDPROGRAM ===

def huvudprogram():
    while True:
        print("Välj färg: 1=Röd, 2=Blå, 3=Gul, 4=Grön")
        farg_val = input("Färg: ")
        if farg_val == "1":
            farg = ROD
        elif farg_val == "2":
            farg = BLA
        elif farg_val == "3":
            farg = GUL
        elif farg_val == "4":
            farg = GRON
        else:
            farg = RESET
        print("\n --- ASCII MÖNSTER ---")
        print("1. Rita kvadrat")
        print("2. Rita triangel")
        print("3. Rita cirkel")
        print("4. Rita blomma")
        print("5. Rita ihålig kvadrat")
        print("6. Rita omvänd triangel")
        print("7. Rita diamant")
        print("8. Avsluta")

        val = input("Välj:")
        if val == "1":
            sida= int(input("Sida: "))
            tecken = input("Tecken: (t.ex *): ")
            rita_kvadrat(sida,tecken, farg)
            pass
        elif val == "2":
            hojd = int(input("Höjd: "))
            tecken = input("Vilket tecken?: ")
            rita_triangel(hojd,tecken, farg)
            pass
        elif val == "3":
            radie = int(input("Radien: "))
            tecken = input("Ange tecken: ")
            rita_cirkel(radie,tecken, farg)
            pass
        elif val == "4":
            kronblad = int(input("Hur många kronblad: "))
            storlek  = int(input("Storlek: "))
            tecken = input("Ange ett tecken: ")
            rita_blomma(kronblad,storlek,tecken, farg)
            pass
        elif val == "5":
            sida = int(input("Sidan: "))
            tecken = input("Tecken: ")
            rita_ihalig_kvadrat(sida, tecken, farg)
            pass
        elif val == "6":
            hojd = int(input("Höjden "))
            tecken = input("Tecken ")
            rita_omvand_triangel(hojd, tecken, farg)
            pass
        elif val == "7":
            hojd = int(input("Höjden "))
            tecken = input("Tecken ")
            rita_diamant(hojd, tecken, farg)
        elif val == "8":
            print("Hejdå")
        break
    else:
        print("Ogiltigt svar")

# === EXTRA FUNKTIONER FÖR UTMANINGAR ===

def rita_ihalig_kvadrat(sida, tecken, farg):
    for i in range(sida):
        if i == 0 or i == sida-1:
            print(farg + tecken * sida)
        else:
            print(farg + tecken + " " *(sida-2) + tecken)
    """
    Ritar en ihålig kvadrat (endast kantlinjen).
    """
    # TODO: Implementera funktionen
    # Tips: Första och sista raden: tecken * sida
    #       Mellanrader: tecken + " "*(sida-2) + tecken
    pass


def rita_omvand_triangel(hojd, tecken, farg):
    for i in range(hojd, 0, -1):
        print(farg + tecken*i)
    """
    Ritar en omvänd triangel (basen upp, spetsen ner).
    """
    # TODO: Implementera funktionen
    # Tips: for i in range(hojd, 0, -1): print(tecken * i)
    pass


def rita_diamant(hojd, tecken, farg):
    for i in range(1, hojd+1):
        print(farg + tecken*i)
    for i in range(hojd-1, 0, -1):
            print(farg + tecken*i)
    """
    Ritar en diamant (två trianglar som möts).
    """
    # TODO: Implementera funktionen
    # Tips: Först en triangel uppåt, sedan en nedåt (utan mittenraden två gånger)
    pass


def spara_till_fil(figur_namn, innehall, filnamn="figur.txt"):
    fil = open(filnamn, "w", encoding="utf=8")
    fil.write("f==={figur_namn}===\n")
    fil.write(innehall)
    fil.close()
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