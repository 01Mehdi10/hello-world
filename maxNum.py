# fonction pour évaluer 3 nombres et renvoyer le plus grand.
def maxNum(n1,n2,n3):
  l = [n1,n2,n3]
  max = l[0]
  if l[1] > max:
    max = l[1]
  if l[2] > max:
    max = l[2]
  return max

# les trois variables pour demander les valeurs à comparer.
N1 = 0
N2 = 0
N3 = 0

# demande des trois nombres, appel de la fonction et affichage du résultat
print("Evaluation entre trois nombres\n et affichage du plus grand.\n","\nEntre trois nombres séparés par des virgules.")
N1, N2, N3 = eval(input())
print("La valeur la plus grande est ", maxNum(N1,N2,N3))