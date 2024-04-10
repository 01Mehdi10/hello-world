#liste1 = mots de plus de 6 caractères
#liste2 = mots de moins de 6 caractères 

mots = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
liste1 = []
liste2 = []
c = 0
while c<len(mots):
  if len(mots[c]) <= 6:
    liste1.append(mots[c])
  else:
    liste2.append(mots[c])
  c+=1
print("mots de moins de 6 caractères :", liste1)
print("mots de plus de 6 caractères :", liste2)