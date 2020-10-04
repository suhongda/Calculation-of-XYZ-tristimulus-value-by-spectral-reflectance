# -*-coding:utf-8-*-
import numpy as np
from shichang import *

def stimulate(reflectivity, field, lighting):             # 反射率，视场，照明体
    d = reflectivity[0, 0] - reflectivity[1, 0]
    dad=0
    for i in range(80):
        ghd=reflectivity[i, 1]*field[i]*lighting[i]*d/100       # 除100为反射率归一化
        dad=dad+ghd
    return dad
 # 系数K
def coefficient_k(reflectivity, field, lighting):             #反射率，视场，照明体
    d = reflectivity[0, 0] - reflectivity[1, 0]
    dad=0
    for i in range(80):
        ghd=field[i]*lighting[i]*d
        dad=dad+ghd
    dad=100/dad
    return dad

reflectivity=np.loadtxt('反射率数据.txt')       # 380~780nm波长的反射率
O=2    #视场
cct=5000   # Dxx标准照明体色温
# print(reflectivity)
d1 = reflectivity[1, 0] - reflectivity[0, 0]
d2 = (reflectivity[10, 0] - reflectivity[2, 0]) / 8
k=coefficient_k(reflectivity, Field(O, 'y', int(d1)), Dxx(cct))   #系数K
if d1==d2 and d1==5 or d1==10:            # 波长间隔5nm或10nm
    xyz=[]
    for gd in 'xyz':
        xyz.append(stimulate(reflectivity, Field(O, gd, int(d1)), Dxx(cct)) * k)
        print(gd,':',xyz[-1])
else:
    print('输入的数据波长间距不合法')


