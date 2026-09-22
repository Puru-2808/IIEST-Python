import matplotlib.pyplot as plt
import numpy as np

a=2.0
E=-2.24
m=938.91
hc=197.33
vi=2.25
vf=150
n=10001
h=(vf-vi)/(n-1)
vv=[]
zz=[]
yy1=[]
yy2=[]

for i in range(n):
    v=vi+i*h
    vv.append(v)
    k=((m*(E+v))**0.5)/(hc)
    z=k*a
    zz.append(z)
    z_0=(a/hc)*((m*v)**0.5)
    y1=-(1/np.tan(z))
    y2=(((z_0/z)**2)-1)**0.5
    yy1.append(y1)
    yy2.append(y2)

diff = np.array(yy1) - np.array(yy2)

for i in range(len(diff)-1):
    if diff[i] * diff[i+1] < 0:
        if abs(diff[i]-diff[i+1])<10:
            print("Intersection v =",vv[i],"MeV")

plt.plot(vv,yy1)
plt.plot(vv,yy2)
plt.ylim(-2, 5)   
plt.grid()
plt.show()