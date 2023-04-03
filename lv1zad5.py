"""
Napišite Python skriptu koja će učitati tekstualnu datoteku naziva song.txt. Potrebno je napraviti rječnik koji kao 
ključeve koristi sve različite riječi koje se pojavljuju u datoteci, dok su vrijednosti jednake broju puta koliko se svaka 
riječ (ključ) pojavljuje u datoteci. Koliko je riječi koje se pojavljuju samo jednom u datoteci? Ispišite ih.
"""

file_path = "song.txt"
word_counts = {} 

with open(file_path, "r") as file: 
    for line in file:
        words = line.strip().split(" ")
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else: 
                word_counts[word] = 1


# Broj rijeci koje se pojavljuju samo jednom
unique_words = 0
for count in word_counts.values():
    if count == 1:
        unique_words += 1


# Ispite rijeci koje se pojavljuju samo jednom
print("Broj rijeci koje se pojavljuju samo jednom: ", unique_words)
print("Rijeci koje se pojavljuju samo jednom: ")
for word, count in word_counts.items():
    if count == 1:
        print(word) 