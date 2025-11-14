import math

def f(t,x,u):
    return -2*b*u-x

w=4.0
b=0.1
n=100

t=[0.0]*(n+2)
x=[0.0]*(n+2)
u=[0.0]*(n+2)

T=2*math.pi/w
ti=0
tf=8*T
h=(tf-ti)/n

t[0]=ti
x[0]=10.0
u[0]=0.0

file1=open("euler_rk2_2ndorder_sol_i.dat","w")
for i in range(n):
    k1=u[i]
    j1=f(t[i],x[i],u[i])
    k2=u[i]+h*j1
    j2=f(t[i]+h,x[i]+h*k1,u[i]+h*j1)
    k=(k1+k2)/2
    j=(j1+j2)/2
    t[i+1]=t[i]+h
    x[i+1]=x[i]+h*k
    u[i+1]=u[i]+h*j
    file1.write(str(t[i])+"   "+str(x[i])+'\n')

file1.close()