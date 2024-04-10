#Fontion pour la mutiplication
def mutiplication(nb):
  c = 1
  while c < 11:
    r = c * nb
    print (c, "x", nb, "=", r)
    c += 1
a = 1 
while a < 11:
  mutiplication(a)
  print("__________\n")
  a += 1