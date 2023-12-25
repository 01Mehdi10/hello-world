# Conversion de degrés, minutes, secondes en radian

d, m, s = 30, 15, 45 # valeurs degrés, minutes, secondes

π = 3.14159265359

rd = (d + m/60 + s/3600) * π/180 # conversion de degrés, minutes, secondes à radians

print (d,"° ", m,"' ", s,'" = ', rd, " rad")
