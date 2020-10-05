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

def f_t(xyz_n, t):
    if xyz_n > t :
        ft=xyz_n**(1/3)
    else:
        ft=(1/3)*((29/6)**3)*xyz_n+(16/116)
    return ft

def xyz2Lab(xyz):         # xyz转Lab
    Lab=[]
    xyz_n=[xyz[0]/96.4221, xyz[1]/100.0, xyz[2]/82.5221]       # [x/x_n, y/y_n, z/z_n]，x_n、y_n与z_n为白点的CIEXYZ三色刺激值
    t = (6 / 29) ** 3
    Lab.append(f_t(xyz_n[1], t)*116- 16)       #L*
    print('L*:', Lab[-1])
    Lab.append((f_t(xyz_n[0], t)-f_t(xyz_n[1], t))*500)  # a*
    print('a*:', Lab[-1])
    Lab.append((f_t(xyz_n[1], t) - f_t(xyz_n[2], t)) * 200)  # b*
    print('b*:', Lab[-1])

reflectivity=np.loadtxt('反射率数据.txt')       # 380~780nm波长的反射率
O=2    #视场
cct=5000   # Dxx标准照明体色温
# print(reflectivity)
d1 = reflectivity[1, 0] - reflectivity[0, 0]
d2 = (reflectivity[10, 0] - reflectivity[2, 0]) / 8
k=coefficient_k(reflectivity, Field(O, 'y', int(d1)), Dxx(cct))   #系数K
xyz=[]
if d1==d2 and d1==5 or d1==10:            # 波长间隔5nm或10nm
    for gd in 'xyz':
        xyz.append(stimulate(reflectivity, Field(O, gd, int(d1)), Dxx(cct)) * k)
        print(gd,':',xyz[-1])         # 输出xyz
else:
    print('输入的数据波长间距不合法')

xyz2Lab(xyz)        # xyz转Lab

