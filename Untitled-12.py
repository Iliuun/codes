import sys

a = int(input("Podaj pierwszą liczbe: "))
b = int(input("Podaj drugą liczbe: "))

if (a < b):
    print("Liczba pierwsza jest mniejsza od drugiej")
else:
    print("Liczba druga jest mniejsza od pierwszej")

if (a < b):
    if (b == 0):
        print("Nie wolno dzielic przez zero")
        sys.exit()
    wynik = b / a
elif (a > b):
    if (b == 0):
        print("Nie wolno dzielic przez zero")
        sys.exit()
    wynik = a / b

print("Wynik działania to: ", wynik)