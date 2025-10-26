import random

a=random.random()

b=random.randint(1,10)

c=random.uniform(1,10)

print(a)
print(b)
print(c)

N=1000000
count=0
for i in range(N):
    x=random.random()
    y=random.random() 
    if x**2+y**2<=1:
        count+=1

pi=4*count/N
print(pi)