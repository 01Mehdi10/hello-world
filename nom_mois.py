# fonction qui affiche le nom du mois de l'année à partir de son numéro.

def nomMois(n):
  an = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
  c = 0
  mois = ""
  ln = len(an)
  while c < ln:
    if c == n - 1:
      mois = an[c]
    c += 1
  if n < 0 or n > 12:
    mois = "f"
  return mois
  
  
##########################################
#   Appel de la fonction et affichage    #
#   du mois.                             #
##########################################
print("Entre le numéro du mois pour afficher son nom : ", end = " ")  
n = int(input())
m = nomMois(n)
if m == "f":
  print("Tu n'as pas entré un numéro valide !")
else:
  print("Le mois est : ", m)
  