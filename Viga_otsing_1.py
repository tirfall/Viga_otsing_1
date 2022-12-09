from math import * #была ошибка в неправильном порядке комманд, поменял их местами
print() 
print("Ruudu karakteristikud")
a = float(input("Sisesta ruudu külje pikkus => ")) #не было написано float, поставил float
S = a**2
P = 4*a
print(f"Ruudu pindala = {S}") #Поменял способ вывода
print(f"Ruudu ümbermõõt = {P}") #Поменял способ вывода
di= round(sqrt(a**2+a**2), 2) #Была неправильно написана формула, изменил на правильную
print(f"Ruudu diagonaal = {di}") #Поменял способ вывода
print()
print("Ristküliku karakteristikud")
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #не было написано float, поставил float
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #не было написано float, поставил float
Sa= b*c #Переменная повторялась, изменил
print(f"Ristküliku pindala = {Sa}") #Поменял способ вывода, поменял выводимую переменную
Pa= b*2+c*2 #Переменная повторялась, изменил
print(f"Ristküliku ümbermõõt = {Pa}")
dia=round(sqrt(b**2+c**2), 2) #Переменная повторялась, изменил. Также была неправильная формула
print(f"Ristküliku diagonaal = {dia}") #Поменял способ вывода, там не было скобки, поставил скобку
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus =>" )) #не было написано float, поставил float
d=2*r #Также была неправильная формула
print(f"Ringi läbimõõt = {d}") #Поменял способ вывода
Sb= round((pi*r**2), 2) #Переменная повторялась, изменил. Также была неправильная формула
print(f"Ringi pindala = {Sb}") #Поменял способ вывода, поменял переменную
C=round((2*pi*r), 2) #Также была неправильная формула
print(f"Ringjoone pikkus = {C}") #Переменная повторялась, изменил. Также была неправильная формула
