# mix des deux listes t1 et t2 pour former la liste t3 = ['janvier',31,'février',28,'mars',31,'avril',30,]

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
t3 = []
lmp = ""
c = 0
while c<12:
  t3.append(t2[c])
  t3.append(t1[c])
  lmp = lmp+t2[c]+" "
  c+=1
print (t3,"\n \n")
print (lmp)
