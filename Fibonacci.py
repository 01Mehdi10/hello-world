#suite de fibonacci
a, b, c = 1, 1, 1
while c < 20:
    a, b, c = b, a+b, c+1
    print (b)