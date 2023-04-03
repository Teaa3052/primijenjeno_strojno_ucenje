"""
Napišite program koji od korisnika zahtijeva unos radnih sati te koliko je plaćen po radnom satu. Koristite ugrađenu
Python metodu input(). Nakon toga izračunajte koliko je korisnik zaradio i ispišite na ekran. Na kraju prepravite
rješenje na način da ukupni iznos izračunavate u zasebnoj funkciji naziva total_euro.
"""

def total_euro(radni_sati, placa_po_satu): 
    return radni_sati * placa_po_satu

radni_sati = float (input("Radni sati: "))
placa_po_satu = float (input ("Eur/h: "))

print("Ukupno: %d eura" % total_euro (radni_sati, placa_po_satu))