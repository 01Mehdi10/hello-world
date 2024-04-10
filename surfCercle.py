#fonction pour calculer la surface d'un cercle
from math import pi
def surfCercle(r):
  R = 0
  R = r*r
  s = pi * R
  return s

# Demande du rayon et appel de la fonction pour calculer puis afficher le résultat.
print("Entre la valeur du rayon")
Rc = eval(input())
print("la surface du cercle de rayon", Rc, "\n est", surfCercle(Rc))