# Addition des multiples de 3 et de 5 entre 0 et 32
print ("Addition des multiples de 3 et de 5 entre 0 et 32")
a = 0
b = 32
c = 0
while a < b:
  if a % 3 == 0 and a % 5 == 0:
    c += a
  a += 1
print ("La somme est ", c)
print ("********************\n********************")

# Addition des multiples de 3 ou de 5 entre 0 et 32
print ("Addition des multiples de 3 ou de 5 entre 0 et 32")
a = 0
b = 32
c = 0
while a < b:
  if a % 3 == 0 or a % 5 == 0:
    c += a
  a += 1
print ("La somme est ",c)