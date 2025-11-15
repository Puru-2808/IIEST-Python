import numpy as np

n=5

a=np.zeros((n,n),dtype=float)
x=np.zeros(n,dtype=float)
b=np.zeros(n,dtype=float)

file4=open("Matrix2_input,dat","r")
i=0
for linei in file4:
    temp=linei.split()
    b[i]=temp[n]
    for j in range(n):
        a[i][j]=temp[j]
    i+=1
file4.close()

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

# ii)
def f(x):
    return x**2-48
def f1(x):
    return 2*x

x0=4.0
for i in range(1,100):
    h=-(f(x0)/f1(x0))
    x0=x0+h
    if abs(f(x0))<=1e-12:
        print("The root is",x0)
        break

# iii)
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

I=(s)*h/3
print("Integration=",I)

# iv)
def f(x,y,u):
    return -u-6*y

n=100
x=[0.0]*(n+2)
y=[0.0]*(n+2)
u=[0.0]*(n+2)

xi=0
xf=5
h=(xf-xi)/n

x[0]=xi
y[0]=0
u[0]=5

file5=open("RK4_solution5.dat","w")

for i in range(n):
    k1=u[i]
    j1=f(x[i],y[i],u[i])
    k2=u[i]+j1*h/2
    j2=f(x[i]+h/2,y[i]+k1*h/2,u[i]+j1*h/2)
    k3=u[i]+j2*h/2
    j3=f(x[i]+h/2,y[i]+k2*h/2,u[i]+j2*h/2)
    k4=u[i]+h*j3
    j4=f(x[i]+h,y[i]+k3*h,u[i]+j3*h)
    k=(k1+2*k2+2*k3+k4)/6
    j=(j1+2*j2+2*j3+j4)/6
    x[i+1]=x[i]+h
    y[i+1]=y[i]+h*k
    u[i+1]=u[i]+h*j
    file5.write(str(x[i])+" "+str(y[i])+"\n")
file5.close()
                
