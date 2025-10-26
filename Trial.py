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
print(integral)'''

import random
N=2*365*24*60*60
c=0
c1=0
for i in range(N):
    x=random.choice(["yes","No"])
    if x=="yes":
        c+=1
    else:
        c1+=1

if c>c1:
    print("You'll get her ")
else:
    print("You'll never get her ")