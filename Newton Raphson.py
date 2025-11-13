def f(x):
    return 7*x**2-50
def f1(x):
    return 14*x

x0=7
eps=0.00001

for i in range(1,100):
    h=-f(x0)/f1(x0)
    x0=x0+h
    if f(x0)<=eps:
        print("The root is",x0)
        break