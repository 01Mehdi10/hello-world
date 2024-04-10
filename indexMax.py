# fonction qui renvoie l'index de la valeur la plus grande d'une liste.

def indexMax(liste):
  c, idx, max = 0, 0, 0
  ln = len(liste)
  while c < ln:
    if liste[c] > max:
      max = liste[c]
      idx = c
    c += 1
  return idx
      
idx = indexMax([4 ,8 ,6 ,32, 67, 9])
print("L'index du nom le plus grand est :", idx)