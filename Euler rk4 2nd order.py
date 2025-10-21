import math

#i) 
w0=4
b=1

def f(t,x,u):                  # d2y/dx2
    return -2*b*u - w0**2*x    # u=dy/dx

n=10000

t=[0.0]*(n+2)
x=[0.0]*(n+2)
u=[0.0]*(n+2)

T=(2*math.pi)/w0
ti=0
tf=15*T
h=(tf-ti)/(n-1)

t[0]=ti
x[0]=10.0
u[0]=0.0

file1=open("euler_rk4_2ndorder_sol_i.dat","w")
for i in range(n):
    k1=u[i]
    j1=f(t[i],x[i],u[i])
    k2=u[i]+(h/2)*j1
    j2=f(t[i]+(h/2),x[i]+(k1*h/2),u[i]+(j1*h/2))
    k3=u[i]+(h/2)*j2
    j3=f(t[i]+(h/2),x[i]+(k2*h/2),u[i]+(j2*h/2))
    k4=u[i]+h*j3
    j4=f(t[i]+h,x[i]+k3*h,u[i]+h*j3)
    k=(k1+2*k2+2*k3+k4)/6
    j=(j1+2*j2+2*j3+j4)/6
    t[i+1]=t[i]+h
    x[i+1]=x[i]+h*k
    u[i+1]=u[i]+h*j
    file1.write(str(t[i])+"   "+str(x[i])+'\n')

file1.close()          # 10*(-bt) has been plotted in gnuplot


#ii)
w0=4
b=1.5

def f(t,x,u):                  # d2y/dx2
    return -2*b*u - w0**2*x    # u=dy/dx

n=10000

t=[0.0]*(n+2)
x=[0.0]*(n+2)
u=[0.0]*(n+2)

T=(2*math.pi)/w0
ti=0
tf=15*T
h=(tf-ti)/(n-1)

t[0]=ti
x[0]=10.0
u[0]=0.0

file2=open("euler_rk4_2ndorder_sol_ii.dat","w")
for i in range(n):
    k1=u[i]
    j1=f(t[i],x[i],u[i])
    k2=u[i]+(h/2)*j1
    j2=f(t[i]+(h/2),x[i]+(k1*h/2),u[i]+(j1*h/2))
    k3=u[i]+(h/2)*j2
    j3=f(t[i]+(h/2),x[i]+(k2*h/2),u[i]+(j2*h/2))
    k4=u[i]+h*j3
    j4=f(t[i]+h,x[i]+k3*h,u[i]+h*j3)
    k=(k1+2*k2+2*k3+k4)/6
    j=(j1+2*j2+2*j3+j4)/6
    t[i+1]=t[i]+h
    x[i+1]=x[i]+h*k
    u[i+1]=u[i]+h*j
    file2.write(str(t[i])+"   "+str(x[i])+'\n')

file2.close()            # 10*(-bt) has been plotted in gnuplot

#iii)
w0=4
b=2

def f(t,x,u):                  # d2y/dx2
    return -2*b*u - w0**2*x    # u=dy/dx

n=10000

t=[0.0]*(n+2)
x=[0.0]*(n+2)
u=[0.0]*(n+2)

T=(2*math.pi)/w0
ti=0
tf=15*T
h=(tf-ti)/(n-1)

t[0]=ti
x[0]=10.0
u[0]=0.0

file3=open("euler_rk4_2ndorder_sol_iii.dat","w")
for i in range(n):
    k1=u[i]
    j1=f(t[i],x[i],u[i])
    k2=u[i]+(h/2)*j1
    j2=f(t[i]+(h/2),x[i]+(k1*h/2),u[i]+(j1*h/2))
    k3=u[i]+(h/2)*j2
    j3=f(t[i]+(h/2),x[i]+(k2*h/2),u[i]+(j2*h/2))
    k4=u[i]+h*j3
    j4=f(t[i]+h,x[i]+k3*h,u[i]+h*j3)
    k=(k1+2*k2+2*k3+k4)/6
    j=(j1+2*j2+2*j3+j4)/6
    t[i+1]=t[i]+h
    x[i+1]=x[i]+h*k
    u[i+1]=u[i]+h*j
    file3.write(str(t[i])+"   "+str(x[i])+'\n')

file3.close()                  # -10*(-bt) has been plotted in gnuplot

#iv)
w0=4
b=0.9

def f(t,x,u):                  # d2y/dx2
    return -2*b*u - w0**2*x    # u=dy/dx

n=10000

t=[0.0]*(n+2)
x=[0.0]*(n+2)
u=[0.0]*(n+2)

T=(2*math.pi)/w0
ti=0
tf=15*T
h=(tf-ti)/(n-1)

t[0]=ti
x[0]=10.0
u[0]=0.0

file4=open("euler_rk4_2ndorder_sol_iv.dat","w")
for i in range(n):
    k1=u[i]
    j1=f(t[i],x[i],u[i])
    k2=u[i]+(h/2)*j1
    j2=f(t[i]+(h/2),x[i]+(k1*h/2),u[i]+(j1*h/2))
    k3=u[i]+(h/2)*j2
    j3=f(t[i]+(h/2),x[i]+(k2*h/2),u[i]+(j2*h/2))
    k4=u[i]+h*j3
    j4=f(t[i]+h,x[i]+k3*h,u[i]+h*j3)
    k=(k1+2*k2+2*k3+k4)/6
    j=(j1+2*j2+2*j3+j4)/6
    t[i+1]=t[i]+h
    x[i+1]=x[i]+h*k
    u[i+1]=u[i]+h*j
    file4.write(str(t[i])+"   "+str(x[i])+'\n')

file4.close()                # -10*(-bt) has been plotted in gnuplot

#v)
w0=4
b=0.75

def f(t,x,u):                  # d2y/dx2
    return -2*b*u - w0**2*x    # u=dy/dx

n=10000

t=[0.0]*(n+2)
x=[0.0]*(n+2)
u=[0.0]*(n+2)

T=(2*math.pi)/w0
ti=0
tf=15*T
h=(tf-ti)/(n-1)

t[0]=ti
x[0]=10.0
u[0]=0.0

file5=open("euler_rk4_2ndorder_sol_v.dat","w")
for i in range(n):
    k1=u[i]
    j1=f(t[i],x[i],u[i])
    k2=u[i]+(h/2)*j1
    j2=f(t[i]+(h/2),x[i]+(k1*h/2),u[i]+(j1*h/2))
    k3=u[i]+(h/2)*j2
    j3=f(t[i]+(h/2),x[i]+(k2*h/2),u[i]+(j2*h/2))
    k4=u[i]+h*j3
    j4=f(t[i]+h,x[i]+k3*h,u[i]+h*j3)
    k=(k1+2*k2+2*k3+k4)/6
    j=(j1+2*j2+2*j3+j4)/6
    t[i+1]=t[i]+h
    x[i+1]=x[i]+h*k
    u[i+1]=u[i]+h*j
    file5.write(str(t[i])+"   "+str(x[i])+'\n')

file5.close()              # -10*(-bt) has been plotted in gnuplot