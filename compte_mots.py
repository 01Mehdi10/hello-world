# fonction pour compter les mots, entre les espaces, dans une phrase.

def compteMots(phrase):
  mots = phrase.split()
  nMots = len(mots)
  print("Le nombre de mots est : ", nMots)

print("Entre un mot ou un phrase :", end = " ")
phr = input()
compteMots(phr)