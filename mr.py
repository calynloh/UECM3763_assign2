import pylab as p
import numpy as np


# define the parameters
alpha = 1;  
theta = 0.064; 
sigma = 0.27;
t = 1;
r0=3;
n_path=1000;   
n=n_partition=1000;    
dt = t/n;

# generate brownian motion
t = p.linspace(0,t,n+1)[:-1]   
dB = p.randn(n_path,n+1) * p.sqrt(dt);
dB[:,0] = 0
B = dB.cumsum(axis=1)

R = p.zeros_like(B)
R[:,0] = r0
for col in range(n):
    R[:,col+1] = R[:,col] +(theta-R[:,col])*dt + sigma*R[:,col]*dB[:,col+1]

#plot 5 realisation
R_5 = R[0:5:,:-1] #choosing 5 realisation
p.plot(t,R_5.transpose())

p.title('5 realisation of the mean reversal process for dR(t)=[0.064-R(t)]dt + 0.27R(t)dB(t)')
p.xlabel('time, t')          
p.ylabel('R(t)')
p.show()

# Calculation for  P[S(3)>39]
r1 = p.array(R[:,-1]) #take all the time 1 value
exp_r1 = np.mean(r1)
print('The expected value of R(1) is ',exp_r1)


#Calculation for E[S(3)|S(3)>39]
count = r1 > 2
Prob = sum(count)/n_path
print('\n P[R(1)> 2 ]= ',Prob)