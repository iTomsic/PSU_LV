# Napišite Python skriptu koja će učitati tekstualnu datoteku naziva SMSSpamCollection.txt [1]. Ova datoteka
# sadrži 425 SMS poruka pri čemu su neke označene kao spam, a neke kao ham. Primjer dijela datoteke:
# ham Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat...
# ham Ok lar... Joking wif u oni...
# spam Did you hear about the new "Divorce Barbie"? It comes with all of Ken's stuff!
# ham Yup next stop.
# a) Izračunajte koliki je prosječan broj riječi u SMS porukama koje su tipa ham, a koliko je prosječan broj riječi u
# porukama koje su tipa spam.
# b) Koliko SMS poruka koje su tipa spam završava uskličnikom ?


datoteka = open("SMSSpamCollection.txt", "r", errors = "ignore")

brHam = 0
brSpam = 0
sumaHam = 0
sumaSpam = 0
brUsklicnik = 0

for line in datoteka:
    line = line.rsplit()
    if (line[0] == "ham"):
        brHam += 1
        sumaHam += (len(line)-1)
    if (line[0] == "spam"):
        brSpam += 1
        sumaSpam += (len(line)-1)
        if ("!" in line[-1]):
            brUsklicnik += 1

print("Prosjecan broj rijeci u ham porukama: ", sumaHam / brHam)
print("Prosjecan broj rijeci u spam porukama: ", sumaSpam / brSpam)
print("Broj poruka koje su spam i zavrsavaju s usklicnikom: ", brUsklicnik)

datoteka.close()
