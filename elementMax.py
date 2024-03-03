# Affiche l'élément le plus grand d'une liste. En option, deux arguments début et fin pour délimiter la section de la liste à comparer.

def eleMax(liste,debut,fin):
  c = 0
  e = 0
  
  # Sans arguments
  if debut == '' and fin == '':
    while c < len(liste):
      if liste[c] > e:
        e = liste[c]
      c += 1
  # Avec les deux arguments
  if debut != '' and fin != '':
    while debut < liste[fin]:
      if liste[debut] > e:
        e = liste[debut]
      debut += 1
  return e
    
# appel fonction
liste = [5,8,4,1,2,7,5,9,3,10,0]
debut = 0
fin = 5
print("L'élément le plus grand est ", eleMax(liste,debut,fin))
