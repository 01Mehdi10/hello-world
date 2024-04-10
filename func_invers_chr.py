# fontion pour inverser une chaîne de caractères.

def inverse(m):
  c = len(m) - 1
  xi = ""
  while c > 0:
    xi = xi + m[c]
    c -= 1
  xi = xi + m[0]
  return xi
  
p = inverse("azerty")
print(p)
