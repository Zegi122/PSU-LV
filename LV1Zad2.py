'''
2.
Napišite program koji od korisnika zahtijeva upis jednog broja koji predstavlja nekakvu ocjenu i nalazi se između 0.0 i
1.0. Ispišite kojoj kategoriji pripada ocjena na temelju sljedećih uvjeta:
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
Ako korisnik nije utipkao broj, ispišite na ekran poruku o grešci (koristite try i except naredbe). Također, ako je
broj izvan intervala [0.0 i 1.0] potrebno je ispisati odgovarajuću poruku
'''

while True:
    try:
        ocjena = float(input("Unesite ocjenu (između 0.0 i 1.0): "))
        if 0.0 <= ocjena <= 1.0:
            break
        else:
            print("Pogrešan unos. Ocjena mora biti između 0.0 i 1.0.")
    except ValueError:
        print("Pogrešan unos. Molimo unesite broj.")

if ocjena >= 0.9:
    print("Vaša ocjena: A")
elif ocjena >= 0.8:
    print("Vaša ocjena: B")
elif ocjena >= 0.7:
    print("Vaša ocjena: C")
elif ocjena >= 0.6:
    print("Vaša ocjena: D")
else:
    print("Vaša ocjena: F")
