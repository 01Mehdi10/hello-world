print("Ce script recherche le plus grand de trois nombres")

print("Veuillez entrer trois nombres séparés par des \nvirgules : ")

ch =input()

nn = list(eval(ch))

max, index = nn[0], 'premier'

if nn[1] > max: # ne pas omettre le double point !
  max = nn[1]
  index = 'second'
if nn[2] > max:
  max = nn[2]
  index = 'troisième'
print("Le plus grand de ces nombres est", max)
print("Ce nombre est le", index, "de votre liste.")