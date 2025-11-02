'''import random

a=random.random()

b=random.randint(1,10)

c=random.uniform(1,10)

print(a)
print(b)
print(c)

N=1000000
count=0
for i in range(N):
    x=random.random()   
    y=random.random() 
    if x**2+y**2<=1:
        count+=1

pi=4*count/N
print(pi)


def f(x):
    return x**2

N=1000000
s=0
for i in range(N):
    x=random.uniform(0,5)
    y=f(x)
    s+=y

integral=5*s/N
print(integral)



def f(x):
    return x**2

xi=0
xf=5
n=100001
h=(xf-xi)/n
xx=[]
yy=[]
for i in range(n):
    x=xi+i*h
    xx.append(x)
    yy.append(f(x))
c=yy[0]+yy[n-1]
s=0
for i in range(1,n-1):
    s+=2*yy[i]
c+=s
integral=h*c/2
print(integral)


def f(x):
    return x**2
xi=0
xf=5
n=100001
h=(xf-xi)/n
xx=[]
yy=[]
for i in range(n):
    x=xi+i*h
    xx.append(x)
    yy.append(f(x))
c=yy[0]+yy[n-1]
s=0
for i in range(1,n-1,2):
    s+=4*yy[i]
s1=0
for i in range(2,n-1,2):
    s1+=2*yy[i]
c+=s+s1
integral=h*c/3
print(integral)

import random
N=2*365*24*60*60
c=0
c1=0
for i in range(N):
    x=random.choice(["No","Yes"])
    if x=="No":
        c+=1
    else:
        c1+=1

if c<c1:
    print("You'll get her ")
else:
    print("You'll never get her ")'''

import numpy as np

n=4

a=np.zeros((n,n),dtype=float)
x=np.zeros(n,dtype=float)
b=np.zeros(n,dtype=float)

file=open("input.dat","r")

i=o
for linei in file:
    temp=linei.split()
    for j in range(n):
        a[i][j]=temp[j]
    b[i]=temp[n]
    i+=1

file.close()

for k in range(n):
    if a[k][k]==0:
        for j in range(n):
            ta=a[k][j]
            a[k][j]=a[k+1][j]
            a[k+1][j]=ta
        tb=b[k]
        b[k]=b[k+1]
        b[k+1]=tb
    for i in range(k+1,n):
        m=a[i][k]/a[k][k]
        b[i]=b[i]-m*b[k]
        for j in range(k,n):
            a[i][j]=a[i][j]+m*a[k][j]
    
x[n-1]=b[n-1]/a[n-1][n-1]
for i in range(n-2,-1,-1):
    sum=0
    for j in range(i+1,n):
        sum=sum+a[i][j]*x[j]
    x[i]=(b[i]-sum)/a[i][i]

for i in range(n):
    print(x[i])