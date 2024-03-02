# fonction pour calculer le volume d'une boîte
def volBoite(L,l,p):
  if L != 1 and l != 1 and p != 1:
    v = L*l*p
    v = round(v, 3)
  if L != 1 and l == 1 and p == 1:
    v = L*L*L
  if L == 1 and l != 1 and p == 1:
    v = l*l*l
  if L == 1 and l == 1 and p != 1:
    v = p*p*p
  if L != 1 and l != 1 and p == 1:
    v = L*L*l
  if L == 1 and l != 1 and p != 1:
    v = l*l*p
  if L != 1 and l == 1 and p != 1:
    v = L*L*p
  return v

# demande des valeurs, appel fonction puis affichage.
print("Calcul du volume d'une boîte \n","\nEntre les trois valeurs :")
Lg = input()
lg = input()
pr = input()
Lg,lg,pr = str(Lg),str(lg),str(pr)
if Lg == "" or Lg <= "0":
  Lg = 1
if lg == "" or lg <= "0":
  lg = 1
if pr == "" or pr <= "0":
  pr = 1
Lg,lg,pr = float(Lg),float(lg),float(pr)
print("Le volume de la boîte est", volBoite(Lg,lg,pr))