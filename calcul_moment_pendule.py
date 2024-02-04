""" Calcul du moment d'un pendule simple.
Formule m = 2π√(l/g)
l représentant la longueur du pendule et g la valeur de l'accélération de la pesanteur au lieu d'expérience. g est de 9,8 m/s² sur terre.
"""
from math import pi, sqrt
print ("*** Calcul du moment d'un pendule simple *** \n")
print("Entre la longueur du pendule :")
l = float(input())
g = 9.8
m = 2*pi*sqrt(l/g)
m = round(m, 2)
print ("Le moment du pendule simple est ", m, "m/s")