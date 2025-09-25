import math

def f(x,u,t):
    return -w**2*x      # d2x/dt2 = -w^2*x

n=100
w=2*math.pi

ti=0.0
tf=3.0
h=(tf-ti)/n

t=[0.0]*n
x=[0.0]*n
u=[0.0]*n

x[0]=1
u[0]=0

file1=open("euler2ndorder_sol.dat","w")

for i in range(n-1):
    x[i+1]=x[i]+h*u[i]
    u[i+1]=u[i]+h*f(x[i],u[i],t[i])
    t[i+1]=t[i]+h

    file1.write(str(t[i])+"  "+str(x[i])+"\n")

file1.close()

