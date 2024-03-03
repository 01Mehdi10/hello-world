# Affiche l'élément le plus grand d'une liste

def eleMax(liste):
  c = 0
  e = 0
  while c < len(liste):
    if liste[c] > e:
      e = liste[c]
    c += 1
  return e
    
# appel fonction
liste = [5,8,4,1,2,7,5]
print("L'élément le plus grand est ", eleMax(liste))
