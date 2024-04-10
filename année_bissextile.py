# script pour determiner si une année est bissextile
print ("Entre une année")
y = int(input ())
if y % 4 == 0:
  if y % 100 == 0:
    if y % 400 == 0:
      print (y, "est une année bissextile")
    else:
      print (y, "n'est pas une année bissextile")
  else:
    print (y, "est une année bissextile")
else: 
  (y, "n'est pas une année bissextile")
  