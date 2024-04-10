# détection d'un palindrome 
print("*** Ce mot est-il un palindrome ? ***\nEcris un mot :")
exp = input()
c = len(exp) - 1
grp = ""
while c > 0:
    grp = grp + exp[c]
    c -= 1
if exp == grp + exp[0]:
    print ("-", exp, "-", "est un palindrome")
else:
    print ("-", exp, "-", "n'est pas un palindrome")