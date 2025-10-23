xx=[]
yy=[]

file2=open("lagrange_inter_input_data.dat","r")

for linei in file2:
    temp1=linei.split()
    xx.append(float(temp1[0]))
    yy.append(float(temp1[1]))

file2.close()



file3=open("lagrange_inter_output_data.dat","w")

xi=-1.0
xf=3.0
h=0.1
for i in range(int((xf-xi)/h)+1):
     x=xi+i*h
     pn=0.0
     for j in range(len(xx)):
        li=1.0
        for k in range(len(xx)):
            if k!=j:
               li=li*((x-xx[k])/(xx[j]-xx[k]))
        pn=pn+(li*yy[j])
     file3.write(str(x)+" "+str(pn)+"\n")
file3.close()