""" Remplissage d'une liste d'éléments automatiquement """
print("*** Remplissage d'une liste d'éléments\n automatiquement ***")
lst = []
e = "start"
while e != "":
  print("Veuillez entrer une valeur : ")
  e = input ()
  if e != "":
    lst.append(e)
print(lst)