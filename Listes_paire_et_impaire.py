# filtrer les nombres paires des nombres impairs
lst = [32, 5, 12, 88, 3, 75, 2, 95]
lst1 = []
lst2 = []
c, n = 0, 0
while c < len(lst):
  if lst[c] % 2 == 0:
    lst1.append(lst[c])
  else:
    lst2.append(lst[c])
  c+=1
print ("liste paire : ", lst1, "\n", "liste impaire :", lst2)