# Napišite program koji od korisnika zahtijeva unos brojeva u beskonačnoj petlji sve dok korisnik ne upiše „Done“ (bez
# navodnika). Pri tome brojeve spremajte u listu. Nakon toga potrebno je ispisati koliko brojeva je korisnik unio, njihovu
# srednju, minimalnu i maksimalnu vrijednost. Sortirajte listu i ispišite je na ekran.
# Dodatno: osigurajte program od pogrešnog unosa (npr. slovo umjesto brojke) na način da program zanemari taj unos i
# ispiše odgovarajuću poruku.


listaBrojeva = []
unos = 0

while (unos != "Done"):
    unos = input("Unesite broj ili 'Done': ")
    try:
        broj = float(unos)
        listaBrojeva.append(broj)
    except ValueError:
        if(unos != "Done"):
            print("Greška! Unesite broj ili 'Done': ")

print("")
print("Broj unesenih brojeva: ", len(listaBrojeva))
print("Nesortirana lista: ", listaBrojeva)
print("Sortirana lista:", sorted(listaBrojeva))
print("Minimalna vrijednost: ", min(listaBrojeva))
print("Maksimalna vrijednost: ", max(listaBrojeva))
print("Srednja vrijednost: ", sum(listaBrojeva) / len(listaBrojeva))
