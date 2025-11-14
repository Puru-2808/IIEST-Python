import math

def f(x):
    return x*math.exp(x)*math.cos(x/2)

a=-math.pi
b=math.pi
n=1000
h=(b-a)/n

xx=[]
yy=[]

for i in range(n):
    x=a+i*h
    xx.append(x)
    yy.append(f(x))

c=yy[0]+yy[n-1]
for i in range(1,n-1):
    c+=2*yy[i]

s=(h/2)*c
print("Integral: ",s)