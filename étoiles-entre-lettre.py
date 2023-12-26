# insertion d'étoiles entre les lettres d'une expression

exp = "azerty"
c = 0
grp = ""
ln = len(exp)
while c < ln:
    grp = grp + exp[c]
    if c < ln - 1:
       grp = grp + "*"
    c += 1
print (grp)        