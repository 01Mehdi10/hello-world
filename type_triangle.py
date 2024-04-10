from sys import exit
print ("""Entrez les valeurs des trois côtés du triangle 
(séparées par des virgules)""")
a, b, c = eval(input())
if a < b + c and b < a + c and c < a + b:
  print ("Ces valeurs permettent de faire un triangle.")
else:
  print ("Ces valeurs ne permettent pas de faire un triangle.")
  exit()
f = 0
if a == b and b == c:
  print("C'est un triangle équilatéral.")
  f = 1
elif a == b or a == c or b == c:
  print("C'est un triangle isocèle.")
  f = 1
if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
  print("C'est un triangle rectangle.")
  f = 1
if f == 0:
  print("C'est un triangle quelconque.")