# Draw 5 branches stars, triangle, 
# 6 branches star and square in a
# curl shape.
# Exercise from the book in french 
# Apprendre à développer avec
# python 3. Author: Gérard Swinnen
# You can download it in the
# tutorial section for python
# in the site
# https://www.developpez.com/

import turtle
bill = turtle.Turtle()
bill.penup()
bill.goto(-5,-110)
bill.speed(10)

#function draw shape

 # star5
def str5(size,d,ds5):
  c = 0
  bill.color("blue")
  for c in range(5):
    bill.pendown()
    bill.forward(size)
    bill.left(144)
    bill.forward(size)
  bill.penup()
  bill.right(0)
  bill.forward(size + d)
  
  # triangle
def tri(s,d):
  c = 0
  bill.color("red")
  bill.pendown()
  for c in range(3):
    bill.forward(s)
    bill.left(120)
    c += 1
  bill.penup()
  bill.left(0)
  bill.forward(s + 5)
  
 # star6
def star6(s,d):
  bill.left(60)
  bill.pendown()
  bill.color("blue")
  c = 0
  for c in range(3):
    bill.forward(s)
    bill.right(120)
    c += 1
  bill.penup()
  bill.forward(s)
  bill.right(90)
  bill.forward(s * 60 / 100)
  bill.right(90)
  bill.pendown()
  c = 0
  for c in range(3):
    bill.forward(s)
    bill.right(120)
    c += 1
  bill.penup()
  bill.right(180)
  bill.forward(d)

 # square
def sqr(s,d,sd5):
  bill.color("red")
  bill.pendown()
  c = 0
  for c in range(4):
    bill.forward(s)
    bill.left(90)
    c += 1
  bill.penup()
  bill.forward(s * sd5 + d)
  
  
#Call function
ct = 0
s = 10 #size
d = 5 #distance
ds5 = 1
str5(s,d,ds5)
s = 25
tri(s,d)
for ct in range(8):
  s += 2
  star6(s,d)
  ds5 = 2
  d = d - 15
  sqr(s,d,ds5)
  ds5 = 1
  s = s - 15
  d = d + 15
  str5(s,d,ds5)
  s = s + 15
  tri(s,d)
star6(s,d)
sqr(s,d,ds5)
bill.color("blue")
bill.goto(0,-200)
#bill.write("C'est réussi :-)", None, None, "16pt bold")