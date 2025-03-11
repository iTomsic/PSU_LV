try:
    broj = float(input("Unesite ocjenu od 0.0 do 1.0: "))
except:
    print("Greška pri unosu!")

if(broj < 0 or broj > 1):
    print("Unesena kriva ocjena!")
elif(broj >= 0.9):
    print("Ocjena je A.")
elif(broj >= 0.8): 
    print("Ocjena je B.")
elif(broj >= 0.7):
    print("Ocjena je C.")
elif(broj >= 0.6):
    print("Ocjena je D.")
elif(broj < 0.6):
    print("Ocjena je F.")

