"""
Napišite Python skriptu koja će učitati tekstualnu datoteku naziva SMSSpamCollection.txt [1]. Ova datoteka 
sadrži 425 SMS poruka pri čemu su neke označene kao spam, a neke kao ham. Primjer dijela datoteke:
ham Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat...
ham Ok lar... Joking wif u oni...
spam Did you hear about the new "Divorce Barbie"? It comes with all of Ken's stuff!
ham Yup next stop.
a) Izračunajte koliki je prosječan broj riječi u SMS porukama koje su tipa ham, a koliko je prosječan broj riječi u 
porukama koje su tipa spam.
b) Koliko SMS poruka koje su tipa spam završava uskličnikom ?
"""

file_path = "SMSSpamCollection.txt"
ham_word_count = []
spam_word_count = []
spam_exclamation_count = 0

with open (file_path, "r") as file: 
    for line in file: 
        label, text = line.strip().split("\t")
        words = text.split()
        if label == "ham":
            ham_word_count.append(len(words))
        elif label == "spam":
            spam_word_count.append(len(words))
            if text.endswith("!"): 
                spam_exclamation_count += 1

ham_word_count = sum(ham_word_count) / len(ham_word_count)
spam_avg_word_count = sum(spam_word_count) / len(spam_word_count)

print("Prosjecan broj rijeci u ham porukama: ", ham_word_count)
print("Prosjecan broj rijeci u spam porukama: ", spam_avg_word_count)
print("Broj spam poruka koje zavrsavaju usklicnikom: ", spam_exclamation_count)