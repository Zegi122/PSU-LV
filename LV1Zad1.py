'''  Napišite program koji od korisnika zahtijeva unos radnih sati te koliko je plaćen po radnom satu. Koristite ugrađenu
Python metodu input(). Nakon toga izračunajte koliko je korisnik zaradio i ispišite na ekran. Na kraju prepravite
rješenje na način da ukupni iznos izračunavate u zasebnoj funkciji naziva total_euro.
Primjer:
Radni sati: 35 h
eura/h: 8.5
Ukupno: 297.5 eura'''

def total_euro(Sat, Satnica):
    return Sat * Satnica

radni_sati = float(input("Unesite broj radnih sati: "))
cijena_po_satu = float(input("Unesite cijenu po satu (u eurima): "))

# Izračun i ispis rezultata
ukupno = total_euro(radni_sati, cijena_po_satu)
print(f"Ukupno: {ukupno:.2f} eura")