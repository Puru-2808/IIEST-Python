x=float(input("x= "))
y=float(input("y= "))

a=((x-2)**2+(y-2)**2)**0.5
radius=5

if a<radius:
    print("POint inside the curve")
elif a==radius:
    print("Point on the curve")
else:
    print("Point outside the curve")
   