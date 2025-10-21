def f(x,y):
    return 5*x-y        # dy/dx = 5x-y

n=100
x=[0.0]*(n+2)
y=[0.0]*(n+2)

# range
a=0.0
b=6.0
h=(b-a)/n

# initial conditions
x[0]=a
y[0]=1.0

file1=open("euler1storder_sol.dat","w")

for i in range(n):
    x[i+1]=x[i]+h
    y[i+1]=y[i]+h*f(x[i],y[i])             # from taylor sries

    file1.write(str(x[i])+"  "+str(y[i])+"\n")

file1.close()