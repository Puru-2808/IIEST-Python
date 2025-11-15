# i)
import numpy as np

n=5
a=np.zeros((n,n),dtype=float)
a0=np.zeros((n,n),dtype=float)
b=np.zeros(n,dtype=float)
x=np.zeros((n,n),dtype=float)

file2=open("Matrix_Data2.dat","r")
i=0
for linei in file2:
    temp=linei.split()
    for j in range(n):
        a[i][j]=temp[j]
    i=i+1
file2.close()

if np.linalg.det(a)<=1e-12:
    print("Matrix is singular, cannot proceed further")
else:
    a0=a.copy()
    for ii in range(n):
        a=a0.copy()
        for j in range(n):
            b[j]=0
        b[ii]=1

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
        x[n-1][ii]=b[n-1]/a[n-1][n-1]
        for i in range(n-2,-1,-1):
            sum=0
            for j in range(i+1,n):
                sum=sum+a[i][j]*x[j][ii]
            x[i][ii]=(b[i]-sum)/a[i][i]

print(x)

# ii)
import math

def f(x):
    return x*math.exp(x)*math.cos(x/2)
pi=math.pi
xi,xf=-pi,pi
n=100
h=(xf-xi)/n

xx=[]
yy=[]

for i in range(n):
    x=xi+i*h
    xx.append(x)
    yy.append(f(x))
c=yy[0]+yy[n-1]
for i in range(1,n-1):
    c=c+2*yy[i]

i=c*h/2
print("The integral is:",i)

# iii)
n=100
r=97
def f(x):
    a=1
    for i in range(1,x+1):
        a=a*i
    return a
s=f(n)/(f(r)*f(n-r))
print("The combination is: ",s)

# iv)
def f(x,y):
    return -y

n=100
x=[0.0]*(n+2)
y=[0.0]*(n+2)

xi=1
xf=3
h=(xf-xi)/n
x[0]=xi
y[0]=10

file3=open("RK4_solution1.dat","w")

for i in range(n):
    k1=f(x[i],y[i])
    k2=f(x[i]+h/2,y[i]+k1*h/2)
    k3=f(x[i]+h/2,y[i]+k2*h/2)
    k4=f(x[i]+h,y[i]+h*k3)
    k=(k1+2*k2+2*k3+k4)/6
    x[i+1]=x[i]+h
    y[i+1]=y[i]+h*k
    file3.write(str(x[i])+" "+str(y[i])+"\n")

file3.close()
