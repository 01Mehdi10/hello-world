""" 
Soit le triangle avec les cotés a,b,c.
Calcule de la surface du triangle avec la formule de Héron. S = √(dp.(dp-a).(dp-b).(dp-c))
On commence par calculer le demi-périmètre (a+b+c)/2.
La variable dp contient la valeur du demi-périmètre 
La variable S contient la valeur calculée de la surface.
"""
from math import sqrt
print ("***** Calcul de la surface d'un triangle ***** \n ***** Formule de Héron *****")
print("Entre la longueur du 1er côté :")
a = float(input())
print("Entre la longueur du 2ème côté :")
b = float(input())
print("Entre la longueur du 3ème côté :")
c = float(input())

# calcul du demi-perimetre
dp = (a+b+c)/2

s = 0
# Calcul de la surface 
s = sqrt(dp*(dp-a)*(dp-b)*(dp-c))
s = round(s)
print("Le périmètre du triangle est", dp*2, "cm")
print("La surface du triangle est ", s, "cm²")