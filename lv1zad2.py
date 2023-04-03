"""
Napišite program koji od korisnika zahtijeva upis jednog broja koji predstavlja nekakvu ocjenu i nalazi se između 0.0 i
1.0. Ispišite kojoj kategoriji pripada ocjena na temelju sljedećih uvjeta:
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
Ako korisnik nije utipkao broj, ispišite na ekran poruku o grešci (koristite try i except naredbe). Također, ako je
broj izvan intervala [0.0 i 1.0] potrebno je ispisati odgovarajuću poruku.
"""


while True:
    ocjena = input ("Ocjena:")
    try:
        ocjena = float(ocjena)
    except ValueError:
        print("Nije unesen broj")
        continue
    if 0 <= ocjena <= 1:
        if ocjena >= 0.9:
            print("Ocjena A")
        elif ocjena >=0.8:
            print("Ocjena B")
        elif ocjena >= 0.7:
            print("Ocjena C")
        elif ocjena >= 0.6:
            print("Ocjena D")
        elif ocjena < 0.6:
            print("Ocjena F")
        break