# Napišite program koji od korisnika zahtijeva upis jednog broja koji predstavlja nekakvu ocjenu i nalazi se između 0.0 i
# 1.0. Ispišite kojoj kategoriji pripada ocjena na temelju sljedećih uvjeta:
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# Ako korisnik nije utipkao broj, ispišite na ekran poruku o grešci (koristite try i except naredbe). Također, ako je
# broj izvan intervala [0.0 i 1.0] potrebno je ispisati odgovarajuću poruku.


try:
    broj = float(input("Unesite ocjenu od 0.0 do 1.0: "))
except ValueError:
    print("")
    print("Greška pri unosu!")

if(broj < 0 or broj > 1):
    print("")
    print("Unesena kriva ocjena!")
elif(broj >= 0.9):
    print("")
    print("Ocjena je A.")
elif(broj >= 0.8):
    print("") 
    print("Ocjena je B.")
elif(broj >= 0.7):
    print("")
    print("Ocjena je C.")
elif(broj >= 0.6):
    print("")
    print("Ocjena je D.")
elif(broj < 0.6):
    print("")
    print("Ocjena je F.")
