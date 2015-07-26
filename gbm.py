import pylab as p
import numpy as np

#define the parameter
mu=0.1;
sigma=0.26;
s0=39;
n_path=1000; #this is the number of simulation
n=n_partition=1000;

#generate 1000 simulation of brownian motion
t=p.linspace(0,3,n+1);
dB=p.randn(n_path, n+1)/p.sqrt(n/3);
dB[:,0]=0;
B = dB.cumsum(axis=1);

nu = mu-sigma*sigma/2.0;
S=p.zeros_like(B);
S[:,0]=s0;
S[:,1:]= s0*p.exp(nu*t[1:]+sigma*B[:,1:]);

#we plot only 5 realization
splot= S[0:5]
p.plot(t,splot.transpose());
p.title('Simulating geometric brownian motion');
p.xlabel('time');
p.ylabel('stock prices')
p.show();

#calculation
s3= p.array(S[:,-1]);
exp= np.mean(s3)
print('E(s3)=', exp)

var=np.var(s3)
print('Var(s3)=',var)

#to calculate probability of s3>39
count1 = s3 > 39;
prob_s3= sum(count1)/n_path
print('P(s3>39) = ',prob_s3)

#to calculate E[S(3) | S(3) > 39]
count2= count1 * s3
E_s3_s339= sum(count2)/sum(count1)
print('E[s3 | s3 > 39] = ',E_s3_s339)


#now find the theoretical expectation and variance of S3
print('The theoretical expectation and variance of S(3) are')
exp_s3 = s0 * p.exp(mu*3)
var_s3 = (s0**2)*(p.exp(2*mu*3))*(p.exp(sigma*sigma*3)-1)
print('Theoretical Expectation of S(3) = ',exp_s3)
print('Theoretical Variance of S(3) = ', var_s3)

