import numpy as np
from scipy import interpolate
import pylab as pl
#创建数据点集并绘制
x = np.linspace(0, 10, 11)
y = np.sin(x)
pl.plot(x,y,'ro')
#建立插值数据点
xnew = np.linspace(0, 10, 101)
for kind in ['nearest', 'zero','linear','quadratic']:
    #根据kind创建插值对象interp1d
    f = interpolate.interp1d(x, y, kind = kind)
    ynew = f(xnew)#计算插值结果
    pl.plot(xnew, ynew, label = str(kind)) #str(kind)显示插值类型
#参数 loc='upper right' 表示图例将添加在图中的右上角.
pl.legend(loc = 'lower left')
pl.show()

