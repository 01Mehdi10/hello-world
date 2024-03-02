# fonction pour changer le caractère dans une chaîne.
def changeCar(ch,ca1,ca2,debut,fin):
  c = 0
  nCh = ''
  while c < len(ch):
    if ch[c] == ca1:
      c += 1
      nCh = nCh + ca2
    nCh = nCh + ch[c]
    c += 1
  return  nCh
  
# Appel fonction
phrase = 'Ceci est une phrase courte'
ca1 = ' '
ca2 = '*'
debut = 6
fin = 12
print(changeCar(phrase,ca1,ca2,debut,fin))