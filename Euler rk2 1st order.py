import math

def f(x,y):
    return 5*y*math.cos(4*x)

n=100
xx=[0.0]*(n+2)
yy=[0.0]*(n+2)
a=0.0
b=2*math.pi
h=(b-a)/n

xx[0]=a
yy[0]=0.5

file1=open("rk2_1storder_sol.dat","w")

for i in range(n):
    k1=f(xx[i],yy[i])
    k2=f(xx[i]+h,yy[i]+k1*h)
    k=(k1+k2)/2
    yy[i+1]=yy[i]+h*k
    xx[i+1]=xx[i]+h
    file1.write(str(xx[i])+"   "+str(yy[i])+"\n")

file1.close()