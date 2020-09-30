#multiplication.py
def x(a, b):
    b = 5
    return(a*b)

#as52.py
import multiplication
import math as m #shortens math to m
b = 7
a = multiplication.x(2, b)#this will return 10 despite b being 7. This is because the namespace b is used in the function
print(a)

c = 5
d = 10 #global
def e(c):
    d = 2 #local
    return c*d
print(e(2), c, d)#should print 4, 5, 10 as d = 2 in e is local but d = 5 is global
print(m.sqrt(2))#since math is shortened to m, we can do this.
