#prosty kalkulator z użyciwm switch i case dla 3.10

import math
import sys
 
print("Witaj w prostym kalkulatorze")
a = int(input("Podaj pierwszą liczbe: "))
b = int(input("Podaj drugą liczbe: "))   
c = input("Wybierz rodzaj działania: 1 - dodawanie, 2 - odejmowanie, 3 - mnożenie, 4 - dzielenie, 5 - potęgowanie, 6 - pierwiastkowanie: ")
    
def switch(c):
    if (c == '1'):
        return a + b
    elif (c == '2'):
        return a - b
    elif (c == '3'):
        return a * b
    elif (c == '4' and (b == 0)):
            print("Nie wolno dzielic przez zero")
            sys.exit()
        return a / b
    elif (c == '5'):
        return a ** b
    elif (c == '6' and (a < 0), (b < 0 )):
        print("Pierwiastek nie moze byc ujemny!")
        sys.exit()
    wynik = math.sqrt(a), math.sqrt(b)