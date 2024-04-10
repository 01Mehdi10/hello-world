# conversion miles à km
#  1 mile = 1609 mètres

d = input("Entre la distance en miles / heure :")
d = int(d)
m = d * 1609  # distance en mètres
km = m / 1000
ms = m / 3600
print ("distance en mètres / seconde :",ms)
print ("distance en km / heure :", km)