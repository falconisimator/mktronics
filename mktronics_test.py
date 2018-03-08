import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from mktronics import *


Motor1=DC_Motor( 8.72, 0.3, 0.006, B=0.1, J=0.1)

Sys1=Mechanical_System(time=10,timestep=0.01)
Sys1.add_component(Motor1)

xy=[]
x=[]
y=[]

for i in range(0,1000):
	Sys1.update_system(24)
	
	


	x.append(i)
	y.append(Motor1.omega_out)


plt.plot(x,y)
plt.show()