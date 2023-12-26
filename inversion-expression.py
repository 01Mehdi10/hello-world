# inversion d'une expression 

exp = "azerty"
c = len(exp) - 1
grp = ""
#ln = len(exp)
while c > 0:
    grp = grp + exp[c]
    c -= 1
print ("à l'endroit :", exp, "\n")
print ("à l'envers :", grp + exp[0])