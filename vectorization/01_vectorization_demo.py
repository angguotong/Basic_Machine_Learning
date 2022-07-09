from re import L
import numpy as np
import time 

a = np.random.rand(1000000)
b = np.random.rand(1000000)


tic = time.time()

l = np.dot(a,b)
toc = time.time()

codeRuntime = (toc-tic)* 1000

print ("Vetorization: {}ms".format(codeRuntime))


tic = time.time()
c = 0
for i,j in zip(a,b):
    c += i*j

toc = time.time()

print("Vectorization: {}ms".format((toc-tic)*1000))


tic = time.time()
z = 0
for i in range(1000000):
    z += a[i]*b[i]
toc = time.time()

print("Vectorization: {}ms".format((toc-tic)*1000))

print (l,c,z)


#Try not to use for loop, using vetorization, we can reduce the speed down to very quick computation. 