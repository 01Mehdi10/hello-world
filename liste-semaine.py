jour = ['dimanche','lundi','mardi','mercredi','jeudi','vendredi','samedi']
a, b = 0, 0
while a<31:
  a = a + 1
  b = a % 7
  print(a, jour[b])