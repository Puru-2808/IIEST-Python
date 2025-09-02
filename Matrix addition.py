a=[[0]*4]*5
b=[[0]*4]*5
c=[[0]*4]*5

for i in range(0,5):
    for j in range(0,4):
        a[i][j]=i*j
        b[i][j]=i+j

for i in range(0,5):
    for j in range(0,4):
        c[i][j]=a[i][j]+b[i][j]
        
print(a,"+",b,"=",c)