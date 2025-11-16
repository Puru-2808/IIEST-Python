# i)
xx=[]
yy=[]

file=open("Lagrange_table_input1.dat","r")
i=0
for linei in file:
    temp=linei.split()
    xx.append(float(temp[0]))
    yy.append(float(temp[1]))
    i+=1
file.close()

xi,xf=-1,1
h=0.1

file1=open("Lagrange_output11.dat","w")
for i in range(int((xf-xi)/h)+1):
    x=xi+i*h
    pn=0
    for j in range(len(xx)):
        li=1
        for k in range(len(xx)):
            if k!=j:
                li=li*((x-xx[k])/(xx[j]-xx[k]))
        pn=pn+yy[j]*li
    file1.write(str(x)+" "+str(pn)+"\n")

file1.close()

# ii)
def f(x):
    return x**2-48

a=-20.0
b=0.0

fa=f(a)
fb=f(b)

if fa*fb>0:
    print("Change range")
else:
    for i in range(100):
        c=(a+b)/2
        fc=f(c)
        if fa*fc<=0:
            b=c
            fb=fc
        else:
            a=c
            fa=fc
    if abs(fc)<=0.00001:
        print("Root is",c)

# iii)
n=100000
c=0
for i in range(2,n+1):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        c+=1
print("there are",c,"no of prime numbers")

# iv)
import random
N=1000000
p=0
for i in range(20):
    c=0
    for j in range(N):
        x=random.random()
        y=random.random()
        if x**2+y**2<=1:
            c+=1
    p=p+(4*c/N)
    
print("mean value of pi",p/20)

# v)
import math
def f(x):
    return x*math.exp(x)*math.cos(x/2)

pi=math.pi
xi=-pi
xf=pi
n=1000
h=(xf-xi)/n

xx=[]
yy=[]

for i in range(n):
    x=xi+i*h
    yy.append(f(x))
c=yy[0]+yy[n-1]

for i in range(1,n-1,2):
    c+=4*yy[i]
s=c
for i in range(2,n-1,2):
    s+=2*yy[i]

print("The integral is",s*h/3)