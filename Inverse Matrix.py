import numpy as np

n=5  # Order of Matrix

a=np.zeros((n,n),dtype=float) # Original Matrix
a0=np.zeros((n,n),dtype=float) # Copy of Original Matrix
b=np.zeros(n,dtype=float)  # Identity Matrix    
xx=np.zeros((n,n),dtype=float) # Inverse Matrix

# Reading Matrix from file
file1=open("Matrix_input.dat","r")
i=0
for linei in file1:
    temp=linei.split()
    for j in range(n):
        a[i][j]=temp[j]
    i+=1
file1.close()

if np.linalg.det(a)<=0.000000000001:       # Checking for Singular Matrix
    print("Matrix is Singular, Inverse cannot be found")
    exit()
else:
   a0=a.copy()
    
   for ii in range(n):
      a=a0.copy()
      # Identity Matrix
      for i in range(n):
         b[i]=0.0
      b[ii]=1.0

      # Applying Gaussian Elimination n times
      for k in range(n):
         if a[k][k]==0:
            for j in range(n):
               t=a[k][j]
               a[k][j]=a[k+1][j]   # Swapping rows to avoid zero pivot element 
               a[k+1][j]=t
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