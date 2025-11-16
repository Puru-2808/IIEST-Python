# i)
def f(x):
    a=0
    for i in range(len(x)):
        a+=x[i]
    return a
def f1(x,y):
    b=0
    for i in range(len(x)):
        b+=x[i]*y[i]
    return b

xx=[]
yy=[]
file6=open("LSF_input.dat","r")
i=0
for linei in file6:
    temp=linei.split()
    xx.append(float(temp[0]))
    yy.append(float(temp[1]))
    i+=1
file6.close()

n=len(xx)
a=(n*f1(xx,yy)-f(xx)*f(yy))/(n*f1(xx,xx)-f(xx)**2)
b=(f(yy)-a*f(xx))/n

print("The slope is",a)
print("The intersection is",b)

# ii)
import math

def f(x):
    return x*math.sin(x)

xi=0
xf=2*math.pi
n=100
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

i=s*h/3
print("Integral",i)

# iii)
import numpy as np

n=3

a=np.zeros((n,n),dtype=float)
a0=np.zeros((n,n),dtype=float)
b=np.zeros(n,dtype=float)
xx=np.zeros((n,n),dtype=float)

file7=open("Matrix7_data.dat","r")
i=0
for linei in file7:
    temp=linei.split()
    for j in range(n):
        a[i][j]=temp[j]
    i+=1
file7.close()

if np.linalg.det(a)<=0.00001:
    print("No inverse")
else:
    a0=a.copy()
    for ii in range(n):
        for j in range(n):
            b[j]=0
        b[ii]=1
        a=a0.copy()
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
        xx[n-1][ii]=b[n-1]/a[n-1][n-1]
        for i in range(n-2,-1,-1):
            sum=0
            for j in range(i+1,n):
                sum=sum+a[i][j]*xx[j][ii]
            xx[i][ii]=(b[i]-sum)/a[i][i]

print(xx)

# iv)
def f(x,y):
    return 5*x-3*y     # dx/dt
def f1(x,y):
    return -6*x+2*y    # dy/dt

n=1000
t=[0.0]*(n+2)
x=[0.0]*(n+2)
y=[0.0]*(n+2)

ti=0
tf=1
h=(tf-ti)/n

t[0]=0
x[0]=15
y[0]=0

file=open("RK4_coupled.dat","w")
file1=open("RK4_coupled1.dat","w")

for i in range(n):
    k1x=f(x[i],y[i])
    k1y=f1(x[i],y[i])

    k2x=f(x[i]+h/2,y[i]+k1x*h/2)
    k2y=f1(x[i]+h/2,y[i]+k1y*h/2)

    k3x=f(x[i]+h/2,y[i]+k2x*h/2)
    k3y=f1(x[i]+h/2,y[i]+k2y*h/2)

    k4x=f(x[i]+h,y[i]+k3x*h)
    k4y=f1(x[i]+h,y[i]+k3y*h)

    kx=(k1x+2*k2x+2*k3x+k4x)/6
    ky=(k1y+2*k2y+2*k3y+k4y)/6

    t[i+1]=t[i]+h
    x[i+1]=x[i]+h*kx
    y[i+1]=y[i]+h*ky

    file.write(str(t[i])+" "+str(x[i])+"\n")
    file1.write(str(t[i])+" "+str(y[i])+"\n")

file.close()
file1.close()