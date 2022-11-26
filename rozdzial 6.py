print("Witaj w prostym kalkulatorze")
a = int(input("Podaj pierwszą liczbe: "))
b = int(input("Podaj drugą liczbe: "))
c = input("Wybierz rodzaj działania: 1 - dodawanie, 2 - odejmowanie, 3 - mnożenie, 4 - dzielenie: ")

if (c == '1'):
    wynik = a + b
elif (c == '2')
    wynik = a - b
elif (c == '3')
    wynik = a * b
elif (c == '4')
    wynik = a / b
else:
    print("Dokonales zlego wyboru!")

print("Wynik dzialania to: ", wynik)