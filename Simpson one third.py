import math

def f(x):
    return x*math.exp(x)*math.cos(x/2)

p=math.pi

xi,xf=-p,p
n=10000
h=(xf-xi)/n

xx=[]
yy=[]

for i in range(n):
    x=xi+i*h
    xx.append(x)
    y=f(x)
    yy.append(y)

c=yy[0]+yy[n-1]
for i in range(1,n-1,2):
    c+=4*yy[i]
s=c
for i in range(2,n-1,2):
    s+=2*yy[i]

print("Integral =",h*s/3)
