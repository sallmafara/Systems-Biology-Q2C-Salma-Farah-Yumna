import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parameters
Vmax = 5
Km = 2
Ki = 3
X = 10

k2 = 1
k3 = 0.8
k4 = 0.3

# System of ODEs
def model(y, t):

    A, B, P = y

    # Reaction rates
    v1 = (Vmax*X/(Km+X))*(1/(1+(P/Ki)))
    v2 = k2*A
    v3 = k3*B
    v4 = k4*A

    # Differential equations
    dAdt = v1-v2-v4
    dBdt = v2-v3
    dPdt = v3

    return [dAdt, dBdt, dPdt]

# Initial concentrations
y0 = [0,0,0]

# Time points
t = np.linspace(0,50,500)

# Solve ODE
sol = odeint(model,y0,t)

# Plot
plt.figure(figsize=(7,5))

plt.plot(t,sol[:,0],label='A')
plt.plot(t,sol[:,1],label='B')
plt.plot(t,sol[:,2],label='P')

plt.xlabel('Time')
plt.ylabel('Concentration')
plt.title('Dynamic Simulation of Metabolite Concentrations')
plt.legend()
plt.grid()

plt.show()
