import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl 
#设置字体
mpl.rcParams['font.sans-serif'] = ['Yahei Consolas Hybrid']
#标签
labels = np.array(['听力','阅读','写作'])
#数据个数
dataLenth = 3
#数据
l = input("请输入你的听力成绩: ")
r = input("请输入你的阅读成绩: ")
w = input("请输入你的写作成绩: ")
data = np.array([l,r,w])
#========自己设置结束============

angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
data = np.concatenate((data, [data[0]])) # 闭合
angles = np.concatenate((angles, [angles[0]])) # 闭合

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)# polar参数！！
ax.plot(angles, data, 'bo-', linewidth=2)# 画线
ax.fill(angles, data, facecolor='r', alpha=0.25)# 填充
ax.set_thetagrids(angles * 180/np.pi, labels)
ax.set_title("四六级成绩", va='bottom')
ax.set_rlim(0,250)
ax.grid(True)
plt.show()