xx=[]
yy=[]

file2=open("lagrange_inter_input_data.dat","r")

for linei in file2:
    temp1=linei.split()
    xx.append(float(temp1[0]))
    yy.append(float(temp1[1]))

file2.close()

n=15

with open("lagrange_inter_output_data.dat","w") as file3:
    for i in range(n):
         x=i**0.2
         pn=0.0
         for j in range(len(xx)):
            li=yy[j]
            for k in range(len(xx)):
                if k!=j:
                    li=li*((x-xx[k])/(xx[j]-xx[k]))
            pn=pn+li
         file3.write(f"{x} {pn}\n")