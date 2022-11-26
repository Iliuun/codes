#wymaganie: program ma posiadać 4 parametry wyjściowe (1. - nazwa programu, 2. - wybór użytkownika, 3. - jakie działanie chce wykonować, 3. i 4. - liczby)

#importowanie zbioru funkcji sys do podania nazwy programu
import sys

#importowanie zbioru funkcji getpass do podania nazwy programu
import getpass

print("Nazwa programu to: ", sys.argv[0])
print("Nazwa użytkownika to: ", sys.argv[1])

c = int(input("Wybierz rodzaj działania: 1 - dodawanie, 2 - odejmowanie, 3 - mnożenie, 4 - dzielenie, 5 - potęgowanie, 6 - pierwiastkowanie: "))

a = int(input("Podaj pierwszą liczbe: "))
b = int(input("Podaj drugą liczbę: "))