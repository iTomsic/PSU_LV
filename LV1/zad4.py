# Napišite program koji  od  korisnika  zahtijeva  unos  imena  tekstualne  datoteke.  Program  nakon  toga  treba tražiti  linije 
# oblika: 
# Primijenjeno strojno učenje – laboratorijske vježbe – VJEŽBA 1  7 
# X-DSPAM-Confidence: <neki_broj> 
# koje  predstavljaju  pouzdanost  korištenog spam filtra. Potrebno je izračunati  srednju  vrijednost  pouzdanosti.  Koristite 
# datoteke mbox.txt i mbox-short.txt 
#
# Primjer  
# Ime datoteke: mbox.txt 
# Average X-DSPAM-Confidence: 0.894128046745 
# Ime datoteke: mbox-short.txt 
# Average X-DSPAM-Confidence: 0.750718518519


imeDatoteke = input("Unesite ime datoteke: ")
br = 0
suma = 0.0

try:
    datoteka = open(imeDatoteke, "r")
except:
    print("Datoteka ne postoji!")

for line in datoteka:
    line = line.rsplit()
    if ("X-DSPAM-Confidence:" in line):
        br += 1
        suma += float(line[1])
    
print("Average X-DSPAM-Confidence: ", suma / br)

datoteka.close()
