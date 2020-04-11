from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import sys

# create the covariance matrix with the gaussian kernel w/ h=5
def kernel(a,b):
	return np.exp(-(1/5)*np.linalg.norm(a-b)**2)

n= 5
x = np.linspace(-10,10,n)
cov = np.array( [[kernel(xi,xj) for xj in x ] for i, xi in enumerate(x)] )
y = np.random.multivariate_normal(np.zeros(n), cov, 4)

[print(l) for l in cov]



fig,ax = plt.subplots(figsize=(15,5), facecolor='white')
ax.set_ylim(-3,3)
for i,f in enumerate(y):
	ax.plot(x,f, label = f'f{i+1}')

#fig.savefig('gaussian,kernel2')
plt.title('4 random functions created with gaussian kernel')
plt.legend()
plt.show()
# def kernel(a,b):
# 	return np.exp(-.5*np.linalg.norm(a-b)**2) #maybe divide this by h ?? 
