import numpy as np 
import matplotlib.pyplot as plt

def hypotenuse (x):
    x =  np.sqrt(x[0]**2 + x[1]**2)  
    return x

qa = 2
qau = 79
ma = 7294.3
ke = 1
c = 137.035999
dt = 0.00001
yo= -0.005
xo = 0
vy = 0.07 * c
vx = 0 
offsetx = 0.0001
radiusvector = []

for i in range (10):
    ri = [offsetx*i, yo]
    vi = [vx, vy]
    rlim = 1.1*hypotenuse(ri)
    radiusvector = []
    while hypotenuse(ri) < rlim:
        a = (ke/ma)*((qau*qa)/(hypotenuse(ri)**2))*(ri/hypotenuse(ri))
        vi = vi + a*dt
        ri = ri + vi*dt
        
        
        
        radiusvector.append(ri)
    radiusvector = np.array(radiusvector)
    plt.plot(radiusvector[:,0],radiusvector[:,1])
    
    

plt.scatter(0,0)
plt.show()

    