# Napišite Python skriptu koja će učitati tekstualnu datoteku naziva song.txt. Potrebno je napraviti rječnik koji kao
# ključeve koristi sve različite riječi koje se pojavljuju u datoteci, dok su vrijednosti jednake broju puta koliko se svaka
# riječ (ključ) pojavljuje u datoteci. Koliko je riječi koje se pojavljuju samo jednom u datoteci? Ispišite ih.


datoteka = open("song.txt", "r")

rijecnik = {}
jedinstveneRijeci = []

for line in datoteka:
    line = line.rsplit()
    for rijec in line:
        if rijec in rijecnik:
            rijecnik[rijec] += 1
        else:
            rijecnik[rijec] = 1

for rijec in rijecnik:
    if (rijecnik[rijec] == 1):
        jedinstveneRijeci.append(rijec)

print("")
print("Sve rijeci i njihov broj ponavljanja: ", rijecnik)
print("")
print("Broj jedinstvenih rijeci: ", len(jedinstveneRijeci))
print("")
print("Jedinstvene rijeci: ", jedinstveneRijeci)
