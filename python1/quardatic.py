import cmath

a=int(input("enter th number a"))
b=int(input("enter th number b"))
c=int(input("enter th number c"))


d=(b**2)-(4*a*c)

s1=(-b-cmath.sqrt(d)/(2*a))
s2=(-b-cmath.sqrt(d)/(2*a))

print(s1,s2)