# 1. Funkcja obliczająca statystyki dostaw

def raport_dostaw(dostawy, prog):
    suma = 0
    najwieksza = None
    najwiekszy_dostawca = None
    licznik_prog = 0
    suma_prog = 0

    for dostawca in dostawy:
        ilosc = dostawy[dostawca]
        suma = suma + ilosc

        if najwieksza is None:
            najwieksza = ilosc
            najwiekszy_dostawca = dostawca
        elif ilosc > najwieksza:
            najwieksza = ilosc
            najwiekszy_dostawca = dostawca

        if ilosc > prog:
            licznik_prog = licznik_prog + 1
            suma_prog = suma_prog + ilosc

    if licznik_prog == 0:
        srednia_prog = None
    else:
        srednia_prog = suma_prog / licznik_prog

    return {
        "suma": suma,
        "najwieksza dostawa": najwieksza,
        "najwiekszy dostawca": najwiekszy_dostawca,
        "powyzej progu": licznik_prog,
        "srednia powyzej progu": srednia_prog
    }


# 2. Dane wejściowe - dostawy palet

dostawy = {
    "DHL": 200,
    "DB Schenker": 85,
    "Dachser": 150,
    "Raben": 60,
    "DSV": 95
}


# 3. Automatyczne obliczenie raportu

wynik = raport_dostaw(dostawy, 200)


# 4. Zapisanie raportu do pliku CSV

plik = open("raport.csv", "w", encoding="utf-8")

plik.write("opis,wartosc\n")

for klucz in wynik:
    # jeśli wartość jest None, to do pliku zapisz: Brak dostaw powyzej progu
    wartosc = wynik[klucz]
    if wartosc is None:
        plik.write(klucz + "," + "Brak dostaw powyzej progu" + "\n")
    else:    
    # w przeciwnym razie do pliku zapisz: wartość
        plik.write(klucz + "," + str(wartosc) + "\n")

plik.close()


# 5. Odczytanie zapisanego pliku

plik = open("raport.csv", "r", encoding="utf-8")

print(plik.read())

plik.close()

# 6. Testy

# Test A: wszyscy ponizej 200
# dane: {"DHL": 120, "INPOST": 100, "UPS": 111}
# oczekuje: powyzej progu = 0, srednia powyzej progu = None

test_a = {"DHL": 120, "INPOST": 100, "UPS": 111}
wynik_a = raport_dostaw(test_a, 200)
print(wynik_a)

# Test B: jeden dostawca ma dokladnie 200
# dane: {"DHL": 200, "INPOST": 100, "UPS": 111}
# oczekuje: powyzej progu = 0, srednia powyzej progu = None
test_b = {"DHL": 200, "INPOST": 100, "UPS": 111}
wynik_b = raport_dostaw(test_b, 200)
print(wynik_b)


















