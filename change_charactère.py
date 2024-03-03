# fonction pour changer le caractère dans une chaîne.
# Apprendre à programmer avec Python 3
# Par Gérard Swinnen
# Exercice page 73
def changeCar(ch,ca1,ca2,debut,fin):
  c = 0
  nCh = ''
  
  #ni début ni fin
  if debut == '' and fin =='':
      nCh = ch

  # avec un début et une fin
  if debut != '' and fin != '':
      while c < debut: #len(ch):
        nCh = nCh + ch[c]
        c += 1
      while c < fin:
        if ch[c] == ca1:
          c += 1
          nCh = nCh + ca2
        nCh = nCh + ch[c]
        c += 1
      while c < len(ch):
        nCh = nCh + ch[c]
        c += 1
        
        
  # avec un début sans fin   
  if debut != '' and fin == '':
      while c < debut:
        nCh = nCh + ch[c]
        c += 1
      while c < len(ch):
        if ch[c] == ca1:
          c += 1
          nCh = nCh + ca2
        nCh = nCh + ch[c]
        c += 1
        
  # sans début, avec fin   
  if debut == '' and fin != '':
     while c < fin:
        if ch[c] == ca1:
          c += 1
          nCh = nCh + ca2
        nCh = nCh + ch[c]
        c += 1
     while c < len(ch):
        nCh = nCh + ch[c]
        c += 1
      
  return  nCh
  
# Appel fonction
phrase = 'Ceci est une toute petite phrase.'
ca1 = ' ' #charatère à remplacer
ca2 = '*' 
debut = 6 
fin = 18
print(changeCar(phrase,ca1,ca2,debut,fin))
