"""
Napišite program koji od korisnika zahtijeva unos imena tekstualne datoteke. Program nakon toga treba tražiti linije
oblika:
X-DSPAM-Confidence: <neki_broj>

koje predstavljaju pouzdanost korištenog spam filtra. Potrebno je izračunati srednju vrijednost pouzdanosti. Koristite
datoteke mbox.txt i mbox-short.txt
"""

ime = input ("Unesite ime tekstualne datoteke: ")
spam_confidence_sum=0
spam_count=0

with open (ime, "r") as file:
    for line in file:
        if line.startswith("X-DSPAM-Confidence:"):
            spam_confidence = float (line.split(":") [1])
            spam_confidence_sum += spam_confidence
            spam_count += 1

if spam_count > 0:
    spam_confidence_avg = spam_confidence_sum / spam_count
    print("Srednja vrijednost pouzdanosti spam filtera je: ", spam_confidence_avg)
else:
    print("Nije pronadenan niti jedna linija pouzdanosti spam filtera u datoteci")