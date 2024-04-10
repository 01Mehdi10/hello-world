# recherche du nombre le plus grand 
lst = [32, 5, 12, 8, 3, 75, 2, 9]
lng = len(lst)
c, max = 0, 0
while c<lng:
  if lst[c]>max:
    max = lst[c]
  c+=1
print ('Le nombre le plus grand est',  max)