import numpy as np
from scipy.optimize import leastsq
X = np.array([8.19, 2.72, 6.39, 8.71, 4.7, 2.66, 3.78])
Y = np.array([7.01, 2.78, 6.47, 6.71, 4.1, 4.23, 4.05])
#计算以p为参数的直线和原始数据之间的误差
def f(p):
    k, b = p
    return(Y-(k*X+b))
#leastsq使得f的输出数组的平方和最小，参数初始值为[1,0]
r = leastsq(f, [1,0])
k, b = r[0]
print("k=",k,"b=",b)
