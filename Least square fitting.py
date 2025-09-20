xx=[]
yy=[]

file1=open("input_data.dat","r")

for linei in file1:
    temp1=linei.split()
    xx.append(float(temp1[0]))
    yy.append(float(temp1[1]))

file1.close()

n=len(xx)

k1=0.0
for i in range(n):
    k1+=xx[i]*yy[i]

k2=0.0
for i in range(n):
    k2+=xx[i]

k3=0.0
for i in range(n):
    k3+=yy[i]

k4=0
for i in range(n):
    k4+=xx[i]**2

# slope
a=((n*k1)-(k2*k3))/((n*k4)-(k2**2))

# intercept
b=(k3-(a*k2))/n

print("slope= ",a)
print("intercept= ",b)