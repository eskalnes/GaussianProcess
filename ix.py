import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import sys
import random


xtrain = np.array([-6,0,7])
ytrain = np.array([3,-2,2])

# use a three units periodic kernel

n = 500
s = -10
f = 10
x = np.linspace(s,f,n)
T = 3*abs(s-f)/(n-1)

def sin2_kernel(a,b):
	return np.exp(-(2/5)*( np.sin( np.pi*abs(a-b)/T) )**2)

def kernel(a,b):
	return np.exp(-(1/5)*np.linalg.norm(a-b)**2)

kxx = np.array( [[kernel(xi,xj) for xi in xtrain ] for xj in xtrain] )
kxx_ = np.array( [[kernel(xi,xj) for xi in x ] for xj in xtrain] )
kx_x = np.array( [[kernel(xi,xj) for xi in xtrain ] for xj in x] )
kx_x_ = np.array( [[kernel(xi,xj) for xi in x ] for xj in x] )

kxxinv = np.linalg.inv(kxx)

mean_ = kx_x @ kxxinv @ ytrain
cov_ = kx_x_ - kx_x @ kxxinv @ kxx_

y = np.random.multivariate_normal(mean_, cov_, 4)

fig,ax = plt.subplots(figsize=(15,5), facecolor='white')
ax.set_ylim(-5,5)


fig,ax = plt.subplots(figsize=(15,5), facecolor='white')
ax.set_ylim(-4,4)
for i,f in enumerate(y):
	ax.plot(x,f, label = f'f{i+1}')

ax.plot(x, mean_, c='k', label ='mean')
ax.scatter(xtrain,ytrain, s=100, )
plt.xticks(x)
plt.title('4 posterior functions created with gaussian kernel')
plt.legend()
plt.show()
fig.savefig('posterior.png')
