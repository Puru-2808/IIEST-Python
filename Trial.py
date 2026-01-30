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


import numpy as np

n=5  # Order of Matrix

a=np.zeros((n,n),dtype=float) # Original Matrix
a0=np.zeros((n,n),dtype=float) # Copy of Original Matrix
b=np.zeros(n,dtype=float)  # Identity Matrix    
xx=np.zeros((n,n),dtype=float) # Inverse Matrix

# Reading Matrix from file
file1=open("Matrix_input.dat","r")
i=0
for linei in file1:
    temp=linei.split()
    for j in range(n):
        a[i][j]=temp[j]
    i+=1
file1.close()

if np.linalg.det(a)<=0.000000000001:       # Checking for Singular Matrix
    print("Matrix is Singular, Inverse cannot be found")
    exit()
else:
   a0=a.copy()
    
   for ii in range(n):
      a=a0.copy()
      # Identity Matrix
      for i in range(n):
         b[i]=0.0
      b[ii]=1.0

      # Applying Gaussian Elimination n times
      for k in range(n):
         if a[k][k]==0:
            for j in range(n):
               t=a[k][j]
               a[k][j]=a[k+1][j]   # Swapping rows to avoid zero pivot element 
               a[k+1][j]=t
            tb=b[k]
            b[k]=b[k+1]
            b[k+1]=tb
         for i in range(k+1,n):
            m=a[i][k]/a[k][k]
            b[i]=b[i]-m*b[k]
            for j in range(k,n):
               a[i][j]=a[i][j]-m*a[k][j]

      xx[n-1][ii]=b[n-1]/a[n-1][n-1]
      for i in range(n-2,-1,-1):
         sum=0
         for j in range(i+1,n):
            sum=sum+a[i][j]*xx[j][ii]
         xx[i][ii]=(b[i]-sum)/a[i][i]

print(xx)'''

import numpy as np
xx=[0.5,0.6,0.7,0.8,1,2,3,4,5,10,15,20,25,30,35,40,50,56,60,70,75,85,90,100,110,120,130,140,150,170,190,200,230,260,300,340,400]
x=[]
for i in range(len(xx)):
    x1=xx[i]*1000
    x.append(x1)
yy=[280,320,356,384,436,560,604,628,640,656,664,664,664,664,664,664,664,660,660,660,656,648,648,644,634,628,620,612,608,592,576,568,545,520,490,458,411]
y=[]
print(len(x),len(yy))
for i in range(len(yy)):
    y1=yy[i]/100
    y.append(y1)
print(y)
k=0
n=len(x)
for i in range(n):
    k=k+y[i]
k1=0
for i in range(n):
    k1=k1+x[i]
k2=0
for i in range(n):
    k2=k2+x[i]**2
k3=0
for i in range(n):
    k3=k3+x[i]*y[i]

m=((n*k3)-k*k1)/((n*k2)-k1**2) #slope
c1=k
c2=m*k1
c3=len(x)
c=(c1-c2)/c3

y_f=[]
for i in range(n):
    y2=m*x[i]+c
    y_f.append(y2)



import matplotlib.pyplot as plt
plt.plot(x,y_f,'-r')
plt.plot(x,y,'.k')
plt.show()