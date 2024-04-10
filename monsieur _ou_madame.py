# demande du genre et du nom
print("""
Entrez votre genre avec la lettre 'M', 'm' ou 'F', 
puis votre nom.""")
g = input()
n = input()
if g == "M" or g == "m":
  print ("Cher monsieur", n)
else:
  print ("Chère madame", n)