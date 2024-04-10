# Affiche l'élément le plus grand d'une liste. En option, deux arguments début et fin pour délimiter la section de la liste à comparer.

def eleMax(liste,debut=3,fin=7):
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
    while debut < fin:
      if liste[debut] > e:
        e = liste[debut]
      debut += 1
   
  # Avec début, sans fin
  if debut != '' and fin == '':
    while debut < len(liste):
      if liste[debut] > e:
        e = liste[debut]
      debut += 1
      
   # sans début, avec fin
  if debut == '' and fin != '':
    while c < fin:
      if liste[c] > e:
        e = liste[c]
      c += 1
    
  return e
    
# appel fonction
liste = [1,4,6,2,11,5,9,3,0]
debut = ''
fin = 7
print("L'élément le plus grand est ", eleMax(liste,debut,fin))
