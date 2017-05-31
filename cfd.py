import numpy as np
import matplotlib.pyplot as plt

def check(i,j,n,m,k,b):
	if i == 0 or j == 0 or i == n-1 or j == m-1:
		b[n*i +j] = 1
	else:
		b[n*i +j] = k
	return b
 
a = []
d = []
n, m = 100, 100
delx = 100
dely = 400
c = -1000
for i in range(0,n):
	for j in range(0,m):
		b = [0] * n * m
		if i == 0 or j == 0 or i == n-1 or j == m-1:
			check(i,j,n,m,0,b)
			a.append(b)
			d.append(0)
		else:
			check(i-1,j,n,m,delx,b)
			check(i+1,j,n,m,delx,b)
			check(i,j-1,n,m,dely,b)
			check(i,j+1,n,m,dely,b)
			check(i,j,n,m,(-2*delx)+(-2*dely),b)
			a.append(b)
			d.append(c)

a = np.array(a)
d = np.array(d)
x = np.linalg.solve(a, d)

'''
for i in range(0,n):
	for j in range(0,m):
		if x[n*i + j] != 0:
			print 'w'+str(i+1)+str(j+1), x[n*i + j]
'''

xlist = np.arange(0, n, 1)
ylist = np.arange(0, m, 1)
X, Y = np.meshgrid(xlist, ylist)
Z = x.reshape((n,m))

plt.figure()
cp = plt.contourf(X, Y, Z)
plt.colorbar(cp)
plt.title('Contours Plot')
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.show()
plt.show()
