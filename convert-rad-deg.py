# 1 Conversion de degrés, minutes, secondes en radian

d, m, s = 30, 15, 45 # valeurs degrés, minutes, secondes

π = 3.14159265359

rd = (d + m/60 + s/3600) * π/180 # conversion de degrés, minutes, secondes à radians

print (d,"° ", m,"' ", s,'" = ', rd, " rad")

#--------------------------------------

# 2 conversion de radian à degrés, minutes, secondes

rad = 3.562588 # valeur en radian 

#π = 3.14159265359

deg = 180/π * rad #degrés 

deg_rnd = round(deg) 

min = (deg - deg_rnd) * 60 #minutes

min_rnd = round(min)

sec = (min - min_rnd) * 60 #secondes

sec_rnd = round(sec)

print (rad, "rad = ", deg_rnd, "° ", min_rnd, "' ", sec_rnd, '"')
