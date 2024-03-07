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

sys.stdout.write(f"Wynik: {wynik}")