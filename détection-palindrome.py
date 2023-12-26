# détection d'un palindrome 

exp = "elle"
c = len(exp) - 1
grp = ""
while c > 0:
    grp = grp + exp[c]
    c -= 1
if exp == grp + exp[0]:
    print ("-", exp, "-", "est un palindrome")
else:
    print ("-", exp, "-", "n'est pas un palindrome")