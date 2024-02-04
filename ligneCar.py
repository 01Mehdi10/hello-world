# fonction ligneCar(n, car), qui renvoie n fois le charactère car.
def ligneCar(n, car):
  c = 1
  ca = ""
  while c <= n:
    ca = ca + car + " " + str(c) + " \n" + " \n"
    c += 1
  return ca
    
# Variables pour input
ct = 1
cr = ""

##########################################
#       partie principale du code.       #
##########################################

# demande du nombre de répétitions, du ou des charactère à utiliser. appel de la fonction ligneCar(n, car)  
print("Entre le nombre de répétitions.", end = " ")
ct = int(input ())
print("Entre le caractère ou le mot qui sera répété", end = " ")
cr = input ()
print (ligneCar(ct, cr))