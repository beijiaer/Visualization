import numpy as np
from scipy import linalg
import timeit

m,n = 50, 50
A = np.random.rand(m,n)
B = np.random.rand(m,n)
def my_func1():
    X1 = linalg.solve(A,B)
def my_func2():
    X2 = np.dot(linalg.inv(A),B)
t1 = timeit.Timer(stmt=my_func1).timeit(number=100)
t2 = timeit.Timer(stmt=my_func2).timeit(number=100)
print(t1,t2)



