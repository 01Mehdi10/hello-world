# fonction pour changer le caractère dans une chaîne.
def changeCar(ch,ca1,ca2,debut,fin):
  c = 0
  while c < len(ch):
    if ch[c] == '':
      ch[c] = '*'
    c += 1
    
# Appel fonction
phrase = 'Ceci est une phrase courte'
