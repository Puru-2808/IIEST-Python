n=int(input("n= "))

x=[1,1]

# Finding nth term
for i in range(1,n-1):
    x.append(x[i]+x[i-1])

# Sum
s=0
for i in range(len(x)):
    s=s+x[i]

print("nth term is: ",x[n-1])
print("Sum is: ",s)

