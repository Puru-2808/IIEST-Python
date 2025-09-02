x=[2,21,-34,1,67,-45,310,37,56,23,517]

for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i]<x[j]:
            t=x[i]
            x[i]=x[j]
            x[j]=t
print(x)