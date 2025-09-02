def f(x):
    return x**3+4*x**2+x+10

a,b=-50,50
fa=f(a)
fb=f(b)

if f(a)*f(b)>0:
    print("Choose different range")
else:
    for i in range(1,100):
        c=(a+b)/2
        fc=f(c)
        if f(a)*f(c)<0:
            b=c
            fb=fc
        else:
            a=c
            fa=fc

    if abs(fc)<=0.00001:
       print(c)
    