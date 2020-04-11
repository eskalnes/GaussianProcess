from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import sys

# each sample from mvn is an n-vector (n=500)
# this n-vector represents a random function
# here I create 4 random functions 
n= 500
a = np.ones((n,n))
a[1:,0] = .9
a[0,1:] = .9

b = np.ones((n,n))
b[1:,0] = .1
b[0,1:] = .1

c = np.ones((n,n))/5

covs = [ np.ones((n,n)), np.eye(n), a, b, c]
names = ['ones', 'identity', 'ones,point9', 'ones,point1', 'all,.2']

for name,cov in zip(names,covs): 
	x = np.linspace(-10,10,n)
	y = np.random.multivariate_normal(np.zeros(n), cov, 4)

	print(y)

	fig,ax = plt.subplots(figsize=(15,5), facecolor='white')
	ax.set_ylim(-3,3)
	for i,f in enumerate(y):
		ax.plot(x,f, label = f'f{i+1}')

	fig.savefig(f'{name}.png')

	plt.title(f'{name}')
	plt.legend()
	plt.show()