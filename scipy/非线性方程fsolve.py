from scipy.optimize import fsolve
from math import sin

#f计算方程组的误差，x是一组可能的解
def f(x):
    x0,x1,x2 = x.tolist()
    return[5*x1+3,
           4*x0*x0 - 2*sin(x1*x2),
           x1*x2-1.5]

#[1,1,1]是未知数的初始值
result = fsolve(f,[1,1,1])
#输出方程组的解
print(result)
#输出误差
print(f(result))
