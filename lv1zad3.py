"""
Napišite program koji od korisnika zahtijeva unos brojeva u beskonačnoj petlji sve dok korisnik ne upiše „Done“ (bez
navodnika). Pri tome brojeve spremajte u listu. Nakon toga potrebno je ispisati koliko brojeva je korisnik unio, njihovu
srednju, minimalnu i maksimalnu vrijednost. Sortirajte listu i ispišite je na ekran.
Dodatno: osigurajte program od pogrešnog unosa (npr. slovo umjesto brojke) na način da program zanemari taj unos i
ispiše odgovarajuću poruku.

"""

brojevi = []

while True:
    broj = input("Upisi broj: ")
    try: 
        brojevi.append(float(broj))
    except ValueError:
        if(broj == "Done"): 
            break

        print("%s greška!" % broj)
        continue

print("Korisnik je unjeo %d brojeva" % len(brojevi))
print("Srednja vrijednost je %d" % (sum(brojevi) / len(brojevi)))
print("Minimalna vrijednost %d"  % min(brojevi))
print("Max %d" % max(brojevi))

print(sorted(brojevi))
