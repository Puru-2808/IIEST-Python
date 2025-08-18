import matplotlib.pyplot as plt

xx = []
yy = []

for i in range(1,80):
    xx.append(i/10)   # finer steps like 0.1, 0.2, ... 7.9
    r = i/10
    y = 5*(((1/r)**12) - 2*(1/r)**6)
    yy.append(y)

plt.plot(xx, yy)
plt.xlabel("r")
plt.ylabel("V(r)")
plt.title("Lennard-Jones Potential")
plt.grid(True)
plt.show()
