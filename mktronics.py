import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


class DC_Motor:

	def __init__(self,K,R,L,B=0,J=0,F=0):
		# self.theta=0
		# self.domega=0
		self.omega_out=0
		self.tau_out=0
		self.I=0

		self.K=K 	#Motor Constant
		self.B=B 	#Viscous damping coefficient
		self.J_out=J	#Motor Moment of inertia
		self.R=R 	#Motor Resistance
		self.L=L
		self.F=F
		self.Fa=0

	def update(self,V,dt):

		if abs(self.K*self.I-self.B*self.omega_out)>self.F:
			self.Fa=self.F*np.sign(self.omega_out)
		else:
			self.Fa=self.K*self.I-self.B*self.omega_out

		
		self.Ea=self.omega_out/self.K

		# self.domega=self.tau_out/self.J_ou
		# self.omega=self.omega+self.domega*dt
		# self.theta=self.theta+self.omega*dt

		self.dI = (V - self.Ea - self.R*self.I) / self.L
		self.I = self.I + self.dI*dt
		self.tau_out=self.K*self.I-self.B*self.omega_out-self.Fa

		return(self.omega_out,self.I)

class BLDC_Motor:

	def __init__():
		return 0

class AC_Motor:

	def __init__():
		return 0

class Motor_Controller:

	def __init__(self):
		self.sat=0

	def P(self,target,current,k):

		self.e = target - current
		self.p=self.e*k

		if self.sat==1:
			if self.p>self.upper:
				self.p=self.upper
			if self.p<self.lower:
				self.p=self.lower

		return self.p

	def saturate(self,upper,lower):
		self.upper=upper
		self.lower=lower
		self.sat=1

class Mechanical_System:

	def __init__(self,time,timestep):
		
		self.components=[]
		self.t=time
		self.dt=timestep
		self.tau=[]
		self.J=[]
		self.omega=[]

	def add_component(self,component):

		self.components.append(component)
		print('Component 1 added')
		self.tau.append(component.tau_out)
		self.J.append(component.J_out)
		self.omega.append(component.omega_out)
		
	def update_system(self,sys_input):
		
		self.components[0].update(sys_input,self.dt)
		for i in range(1,len(self.components)):
			self.components[i].update_T(self.components[i-1].tau_out,self.dt)
		for i in range(0,len(self.components)):
			self.tau[i]=self.components[i].tau_out
		self.components[i].update(sys_input,self.dt)
		for i in range(1,len(self.components)):
			self.components[i].update_J(self.components[i-1].J_out,self.dt)
		for i in range(0,len(self.components)):
			self.J[i]=self.components[i].J_out
		return(self.tau,self.J)

























