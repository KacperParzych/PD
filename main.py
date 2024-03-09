import sys

# Zad 1. Napisz skrypt, który pobiera od użytkownika zdanie i liczy ilość słów. Użyj funkcji input

Zdanie = input("Podaj zdanie:")
IloscSlow = len(Zdanie.split())

print("Ilosc slow w zdanie:", IloscSlow)

# Zad 2. Napisz skrypt gdzie pobierzesz trzy liczby całkowite, gdzie wykonasz obliczenia: ab + c.  Użyj funkcji readline() i write()).

sys.stdout.write("Podaj 1 liczbe: ")
a = int(sys.stdin.readline())
sys.stdout.write("Podaj 2 liczbe: ")
b = int(sys.stdin.readline())
sys.stdout.write("Podaj 3 liczbe: ")
c = int(sys.stdin.readline())

wynik = a * b + c

sys.stdout.write(f"Wynik: {wynik} \n")

# Zad3. Napisz skrypt, który sprawdzi czy wczytany napis jest palindromem.

napis = input("Podaj napis:")
if napis == napis[::-1]:
    print("jest palindromem.")
else:
    print("nie jest palindromem.")
# Zad4. Napisz skrypt, który sprawdzi czy wczytana liczba jest pierwsza.

def pierwsza(liczba):
    if liczba <= 1:
        return False
    for i in range(2, liczba):
        if liczba % i  == 0:
            return False
    return True
liczba = int(input("Podaj liczbe: "))
if pierwsza(liczba):
    print("Pierwsza")
else:
    print("Nie pierwsza")
breakpoint()
