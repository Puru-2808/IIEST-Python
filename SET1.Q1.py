a=float(input("a= "))
b=float(input("b= "))
c=float(input("c= "))

x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
x2=(-b-(b**2-4*a*c)**0.5)/(2*a)

if b**2-4*a*c<0:
   print("Complex roots")
   print("x1=",x1)
   print("x2=",x2)
elif b**2-4*a*c==0:
   print("Real and equal roots")
   print("x1=",x1)
   print("x2=",x2)
else:
   print("Real and distinct roots")
   print("x1=",x1)
   print("x2=",x2)