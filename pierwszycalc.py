from math import *

# Wprowadzanie liczb
l1 = input("\n\nWprowadź pierwszą liczbę: ")
l2 = input("Wprowadź drugą liczbę: ")

l1 = float(l1)
l2 = float(l2)

# Obliczenia matematyczne
suma = l1 + l2
print("Suma wynosi:", suma)

roznica = l1 - l2
print("Różnica wynosi:", roznica)

iloczyn = l1 * l2
print("Iloczyn wynosi:", iloczyn)

if l2 != 0:
    iloraz = l1 / l2
    print("Iloraz wynosi:", iloraz)
else:
    iloraz = None
    print("Nie można dzielić przez zero.")

potega = suma ** 2
print("Kwadrat sumy wynosi:", potega)

# Pierwiastek
if suma > 0:
    pierwiastek = sqrt(suma)
    print("Pierwiastek sumy wynosi:", pierwiastek)
else:
    pierwiastek = None
    print("Suma musi być dodatnia, aby policzyć pierwiastek.")

# Największy i najmniejszy wynik (pomijamy None)
liczby = [suma, roznica, iloczyn, potega]
if iloraz is not None:
    liczby.append(iloraz)
if pierwiastek is not None:
    liczby.append(pierwiastek)

print("\nNajwiększy wynik to:", max(liczby))
print("Najmniejszy wynik to:", min(liczby))

# Porównanie liczb
if l1 > l2:
    print("\nPierwsza podana liczba była większa od drugiej!")

    dzienniczek = {
        "Mateusz": [5, 4, 5, 6, 6],
        "Daniel": [1, 2, 3, 4, 3, 2, 1]
    }

    for imie, oceny in dzienniczek.items():
        if 6 in oceny:
            print("\nTen uczeń jest genialny, ponieważ ma 6 w dzienniku! Jego imię to:", imie)
        if 1 in oceny:
            print("Ten uczeń nie zda do następnej klasy, ponieważ ma 1! Jego imię to:", imie)

elif l1 < l2: 
    print("\nDruga podana liczba była większa od pierwszej!")
    
    zakupy = {
        "jabłko": [1.25],
        "coca-cola": [6.99],
        "milchrice": [1.69],
        "pstrąg 1kg": [14.99],
        "makaron": [7.99],
    }

    print("\nNasze zakupy to:")
    for produkt, cena in zakupy.items():
        print(f"{produkt}: {cena[0]:.2f} zł")

    koszt = sum(cena[0] for cena in zakupy.values())
    print("\nŁączny koszt zakupów wynosi:", round(koszt, 2), "zł")

    czestotliwosc = input("\nIle razy w miesiącu robimy takie zakupy? ")
    czestotliwosc = int(czestotliwosc)

    m_koszt = koszt * czestotliwosc
    print(f"\nBiorąc pod uwagę, że na takie zakupy chodzisz {czestotliwosc} razy w miesiącu, będziesz musiał za nie płacić miesięcznie {round(m_koszt, 2)} zł.")



# Zakupy
