import numpy as np

n=3
a=np.zeros((n,n),dtype=float)
x=np.zeros(n,dtype=float)
b=np.zeros(n,dtype=float)

file1=open("gauss_elimination_input.dat","r")

i=0
for linei in file1:
    temp=linei.split()
    b[i]=temp[n]
    for j in range(n):
        a[i][j]=temp[j]
    i=i+1

file1.close()

for k in range(0,n):
    if a[k][k]==0:
        for j in range(n):
            ta=a[k][j]
            a[k][j]=a[k+1][j]    # Swapping rows to avoid zero pivot element
            a[k+1][j]=ta
        tb=b[k]
        b[k]=b[k+1]
        b[k+1]=tb
    for i in range(k+1,n):
        m=a[i][k]/a[k][k]
        b[i]=b[i]-(a[i][k]/a[k][k])*b[k]
        for j in range(k,n):
            a[i][j]=a[i][j]-m*a[k][j]

for i in range(n):
    print(a[i])

x[n-1]=b[n-1]/a[n-1][n-1]
for i in range(n-2,-1,-1):
    sum=0
    for j in range(i+1,n):
        sum=sum+a[i][j]*x[j]
    x[i]=(b[i]-sum)/a[i][i]

for i in range(n):
    print(x[i])
print(0*x[0]+2*x[1]+3*x[2])
print(4*x[0]+5*x[1]+6*x[2])
print(7*x[0]+8*x[1]+9*x[2])

