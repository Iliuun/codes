#Napisz program, w którym najpierw pytasz o pierwszą literę imienia, a następnie o jego nazwisko. Połącz całość kropką tak, aby posiadała format M.Wiszniewskie, a wynik wypisz na ekranie.

imie = input("Podaj pierwsza litere swojego imienia: ")
nazwisko = input("Podaj swoje nazwisko: ") 

print(imie.upper() + "." + nazwisko.upper())