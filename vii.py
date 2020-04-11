import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import sys
import random
import copy

n = 100
s = -10
f = 10
x = np.linspace(s,f,n)

def sin2_kernel(a,b,p):
	T = p*abs(s-f)/(n-1)
	return np.exp(-(2/5)*( np.sin( np.pi*abs(a-b)/T) )**2)

def tan_kernel(a,b,p):
	T = p*abs(s-f)/(n-1)
	return abs(np.tan(np.pi*(a-b)/T))

''' mean of 0's means that the function will be exactly the same in each period'''
mean = np.zeros(n)
''' random mean adds noise'''
#mean = [random.randint(-100,100)/100 for i in range(n)]

cov = np.eye(n)
cov.astype(float)

cov01 = copy.deepcopy(cov)
for i,row in enumerate(cov01):
	for j,e in enumerate(row):
		if (abs(i-j) % 3) == 0 :
			cov01[i,j] = 1.0 

names = ['cov01', 'cov_tan', 'cov_sin2']
periods = [3, 10]

for p in periods:
	cov_tan = [[round(tan_kernel(xi,xj,p),3) for xj in x ] for xi in x]
	cov_sin2 = [[round(sin2_kernel(xi,xj,p),3) for xj in x ] for xi in x] 
	covs = [cov01, cov_tan, cov_sin2]
	for c,name in zip(covs,names):
		y = np.random.multivariate_normal(mean, c, 4)
		fig,ax = plt.subplots(figsize=(15,5), facecolor='white')
		ax.set_ylim(-3,3)
		for i,f in enumerate(y):
			ax.plot(x,f, label = f'f{i+1}')
		fig.savefig(f'{name},n{n},p{p}.png')
		plt.xticks(x)
		plt.title(f'{name},n{n},p{p}')
		plt.legend()
		plt.show()

# # for i,f in enumerate(y):
# # 	fig,ax = plt.subplots(figsize=(15,5), facecolor='white')
# # 	ax.set_ylim(-3,3)
# # 	ax.plot(x,f, label = f'f{i+1}')
# # 	plt.xticks(x)
# # 	plt.title('4 random functions created with periodic kernel')
# # 	plt.legend()
# # 	plt.show()

# cov_smooth = np.zeros((n,n)).astype(float)

# p = 10

# for i,row in enumerate(cov_smooth):
# 	for j,e in enumerate(row):
# 		if (abs(i-j) % 1) == 0:
# 			cov_smooth[i,j] = .8

# 		if (abs(i-j) % 2) == 0:
# 			cov_smooth[i,j] = .6

# 		if (abs(i-j) % 3) == 0:
# 			cov_smooth[i,j] = .4

# 		if (abs(i-j) % 4) == 0:
# 			cov_smooth[i,j] = .2

# 		if (abs(i-j) % 5) == 0:
# 			cov_smooth[i,j] = .1

# 		if (abs(i-j) % 6) == 0:
# 			cov_smooth[i,j] = .2

# 		if (abs(i-j) % 7) == 0:
# 			cov_smooth[i,j] = .4

# 		if (abs(i-j) % 8) == 0:
# 			cov_smooth[i,j] = .6

# 		if (abs(i-j) % 9) == 0:
# 			cov_smooth[i,j] = .8

# 		if (abs(i-j) % p) == 0:
# 			cov_smooth[i,j] = 1.0

# [print(l) for l in cov_smooth]

# y = np.random.multivariate_normal(mean, cov_smooth, 4)


# for i,f in enumerate(y):
# 	fig,ax = plt.subplots(figsize=(15,5), facecolor='white')
# 	ax.set_ylim(-3,3)
# 	ax.plot(x,f, label = f'f{i+1}')
# 	plt.xticks(x)
# 	plt.title('4 random functions created with smooth kernel')
# 	plt.legend()
# 	plt.show()

