# fonction pour calculer le volume d'une boîte
def volBoite(L=10,l=10,p=10):
  #if L != 1 and l != 1 and p != 1:
  v = L*l*p
  v = round(v, 3)
  return v

# demande des valeurs, appel fonction puis affichage.
print("Calcul du volume d'une boîte \n","\nEntre les trois valeurs :")
Lg = input()
lg = input()
pr = input()
Lg = str(Lg)
lg = str(lg)
pr = str(pr)
if Lg == "" or Lg < "0":
  Lg = 0
if lg == "" or lg < "0":
  lg = 0
if pr == "" or pr < "0":
  pr = 0
Lg = float(Lg)
lg = float(lg)
pr = float(pr)
if Lg == 0 and lg ==0 and pr == 0:
  print("Le volume de la boîte est",volBoite())
if Lg > 0 and lg == 0 and pr == 0:
  print("Le volume de la boîte est",volBoite(Lg))
if Lg > 0 and lg > 0 and pr == 0:
  print("Le volume de la boîte est",volBoite(Lg,lg))
if Lg > 0 and lg > 0 and pr > 0:
  print("Le volume de la boîte est",volBoite(Lg,lg,pr))