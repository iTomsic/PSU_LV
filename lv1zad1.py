def total_euro(radniSati, placaPoSatu):

    ukupno = radniSati * placaPoSatu
    print("Ukupno: ",ukupno)


radniSati = float(input("Unesite broj radnih sati: "))
placaPoSatu = float(input("Unesite broj eura po satu: "))


print("Radni sati: ",radniSati)
print("Placa po satu: ",placaPoSatu)
total_euro(radniSati, placaPoSatu)
