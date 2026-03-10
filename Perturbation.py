import numpy as np
import sympy as sp
from scipy import integrate
import matplotlib.pyplot as plt

xi = -1
xf = 1
n = 10001
h = (xf - xi) / (n - 1)

Ei = 0
Ef = 12
n1 = 1001
h1 = (Ef - Ei) / (n1 - 1)

# just for getting perturbed energy levels for different lambda values

# lambda values to build the polynomial and find the coefficients
alist = [0, 0.1, 0.2, 0.3, 0.4, 0.5]
Energy_levels = []

for a in alist:
    EE = []
    yy = []

    for i in range(n1):
        E = Ei + i * h1
        EE.append(E)
        
        y = 0.0
        z = 1.0 # Initial derivative y'(-1)
        
        # RK4 Integration Loop
        for j in range(n-1):
            x = xi + j * h
            
            # The system: 
            # dy/dx = z
            # dz/dx = -2 * (E - a * x**4) * y
            
            def f_z(x_val, y_val):
                return -2 * (E - a * x_val**4) * y_val

            k1y = h * z
            k1z = h * f_z(x, y)

            k2y = h * (z + 0.5 * k1z)
            k2z = h * f_z(x + 0.5 * h, y + 0.5 * k1y)

            k3y = h * (z + 0.5 * k2z)
            k3z = h * f_z(x + 0.5 * h, y + 0.5 * k2y)

            k4y = h * (z + k3z)
            k4z = h * f_z(x + h, y + k3y)

            y = y + (k1y + 2*k2y + 2*k3y + k4y) / 6
            z = z + (k1z + 2*k2z + 2*k3z + k4z) / 6
            
        yy.append(y)

    # Find the first energy level where y(xf) crosses zero
    for i in range(n1 - 1):
        if yy[i] * yy[i + 1] < 0:
            # Linear Interpolation for root refinement
            precise_E = EE[i] - yy[i] * (EE[i+1] - EE[i]) / (yy[i+1] - yy[i])
            Energy_levels.append(precise_E)
            break


degree = 2
coeffs = np.polyfit(alist, Energy_levels, degree)

E2 = coeffs[0]
E1 = coeffs[1]
E0_val = coeffs[2]

print(f"E0 (Unperturbed) = {E0_val:.8f}")
print(f"First order correction (E1): {E1:.8f}")
print(f"Second order correction (E2): {E2:.8f}")

b = 0.5   # lambda value for which we want to calculate the total energy
E_total = E0_val + b*E1 + (b**2)*E2
print("Total corrected ground state energy:", E_total)


EE=[]
yy=[]

# Plotting the unperturbed energy levels
for i in range(n1):
    zi=1
    yi=0
    E=Ei+i*h1
    EE.append(E)
    mi=-2*E*yi
    for j in range(n):
        x=xi+j*h
        z=zi+h*mi
        y=yi+h*zi
        m=-2*EE[i]*y
        yi=y
        zi=z
        mi=m
    yy.append(y)

EE1=[]
for i in range(n1-1):
    if yy[i]*yy[i+1]<0:
        E_root = EE[i] - yy[i] * (EE[i+1] - EE[i]) / (yy[i+1] - yy[i])
        EE1.append(E_root)

# Perturbed energy levels for lambda = 0.5
EE=[]
yy=[]

for i in range(n1):
    yi, zi = 0, 1
    E = Ei + i * h1
    EE.append(E)

    mi = -2 * (E - b * xi**4) * yi

    for j in range(n - 1):
        x = xi + j * h
        z = zi + h * mi
        y = yi + h * zi
        m = -2 * (E - b * x**4) * y
        yi, zi, mi = y, z, m

    yy.append(y)

EE2 = []
for i in range(n1 - 1):
    if yy[i] * yy[i + 1] < 0:
        E_root = EE[i] - yy[i] * (EE[i+1] - EE[i]) / (yy[i+1] - yy[i])
        EE2.append(E_root)

num_states = min(len(EE1), len(EE2), 4)  # plot first few states

for i in range(num_states):

    # -------- UNPERTURBED --------
    E = EE1[i]
    yi, zi = 0, 1
    mi = -2 * E * yi
    xx = [xi]
    yy = [yi]

    for j in range(n - 1):
        x = xi + j * h
        xx.append(x)

        yf = yi + h * zi
        yy.append(yf)

        zf = zi + h * mi
        mf = -2 * E * yf
        yi, zi, mi = yf, zf, mf

    xx_arr = np.array(xx)
    yy_arr = np.array(yy)
    N = integrate.simpson(yy_arr**2, xx_arr)
    yy_arr /= np.sqrt(N)

    plt.plot(xx_arr, yy_arr, label=f"Unpert n={i}")

 # -------- PERTURBED --------
    E = EE2[i]
    yi, zi = 0, 1
    mi = -2 * (E - b * xi**4) * yi
    xx = [xi]
    yy = [yi]

    for j in range(n - 1):
        x = xi + j * h
        xx.append(x)

        yf = yi + h * zi
        yy.append(yf)

        zf = zi + h * mi
        mf = -2 * (E - b * x**4) * yf
        yi, zi, mi = yf, zf, mf

    xx_arr = np.array(xx)
    yy_arr = np.array(yy)
    N = integrate.simpson(yy_arr**2, xx_arr)
    yy_arr /= np.sqrt(N)

    plt.plot(xx_arr, yy_arr, '--', label=f"Pert n={i}")

plt.xlabel("x")
plt.ylabel("Wavefunction ψ(x)")
plt.title("Unperturbed vs Quartic Perturbed Eigenstates")
plt.text(0.05,0.95, f"E0 (Unperturbed) = {E0_val:.8f}\nFirst order correction (E1): {E1:.8f}\nSecond order correction (E2): {E2:.8f}\nTotal Energy: {E_total:.8f}", transform=plt.gca().transAxes, verticalalignment='top')
plt.legend()
plt.grid()
plt.show()