# i)
import math

def f(t,x,u):
    return -2*b*u-x    # m d2x/dt2 + b1 dx/dt + kx = 0

m=1.0
b=0.1
b1=2*b
k=1.0
w0=(k/m)**0.5
y=b1/(2*m)
w=(w0**2-y**2)**0.5

if y<w0:                 # Under damped (Osscillation)
    T=2*math.pi/w
else:                    # No oscillation
    T=2*math.pi/w0

n=1000
t=[0.0]*(n+2)
x=[0.0]*(n+2)
u=[0.0]*(n+2)

ti=0.0
tf=8*T
h=(tf-ti)/n

t[0]=ti
x[0]=10.0
u[0]=0.0

file0=open("RK4_sol.dat","w")
           
for i in range(n):
    k1=u[i]
    j1=f(t[i],x[i],u[i])
    k2=u[i]+j1*h/2
    j2=f(t[i]+h/2,x[i]+k1*h/2,u[i]+j1*h/2)
    k3=u[i]+j2*h/2
    j3=f(t[i]+h/2,x[i]+k2*h/2,u[i]+j2*h/2)
    k4=u[i]+h*j3
    j4=f(t[i]+h,x[i]+k3*h,u[i]+j3*h)
    K=(k1+2*k2+2*k3+k4)/6
    j=(j1+2*j2+2*j3+j4)/6
    t[i+1]=t[i]+h
    x[i+1]=x[i]+h*K
    u[i+1]=u[i]+h*j
    file0.write(str(t[i])+"  "+str(x[i])+"\n")

file0.close()

# ii)
import random

N=20
n=1000000

p=0
for i in range(N):
    c=0
    for i in range(n):
        x=random.random()
        y=random.random()
        if x**2+y**2<=1:
            c+=1
        pi=4*c/n
    p=p+pi

print("Mean value of pi: ",p/N)

# iii)
import numpy as np

n=4
a=np.zeros((n,n),dtype=float)
x=np.zeros(n,dtype=float)
b=np.zeros(n,dtype=float)

file1=open("Matrix_data.dat","r")
i=0
for linei in file1:
    temp=linei.split()
    b[i]=temp[n]
    for j in range(n):
        a[i][j]=temp[j]
    i=i+1
file1.close()

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
            a[i][j]=a[i][j]-m*a[k][j]

x[n-1]=b[n-1]/a[n-1][n-1]
for i in range(n-2,-1,-1):
    sum=0
    for j in range(i+1,n):
        sum=sum+a[i][j]*x[j]
    x[i]=(b[i]-sum)/a[i][i]

for i in range(n):
    print("x[",i,"]=",x[i])

# iv)
n=100000
c=0
for i in range(2,n+1):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        c+=1
print("Total number of prime numbers up to ",n," is ",c)