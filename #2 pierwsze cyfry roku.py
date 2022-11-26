#zadanie 1 - dodaj opcje potęgowania i pierwiastkowania w programie 

import math
import sys

print("Witaj w prostym kalkulatorze")
a = int(input("Podaj pierwszą liczbe: "))
b = int(input("Podaj drugą liczbe: "))
c = input("Wybierz rodzaj działania: 1 - dodawanie, 2 - odejmowanie, 3 - mnożenie, 4 - dzielenie, 5 - potęgowanie, 6 - pierwiastkowanie: ")

if (c == '1'):
    wynik = a + b
elif (c == '2'):
    wynik = a - b
elif (c == '3'):
    wynik = a * b
elif (c == '4'):
    if (b == 0):
        print("Nie wolno dzielic przez zero")
        sys.exit()
    wynik = a / b
elif (c == '5'):
    wynik = a ** b
elif (c == '6'):
    if (a < 0, b < 0):
        print("Pierwiastek nie moze byc ujemny!")
        sys.exit()
    wynik = math.sqrt(a), math.sqrt(b)
else:
    print("Dokonales zlego wyboru!")

print("Wynik dzialania to: ", wynik)
