# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 22:23:26 2016

@author: yjq
"""
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

class two_capacitor_paltes:
    def __init__(self,v1=1.0,v2=-1.0,v=0,step=0.1,x1=-1.5,x2=1.5,y1=-1.5,y2=1.5):
        self.v1=v1
        self.v2=v2
        self.v=[[0]*30 for i in range(30)]
        for i in range(11,17):
            self.v[i][11]=self.v1
            self.v[i][17]=self.v2
        self.deltav=0
        
        self.dx=0.1
        self.dy=0.1
        self.ex=[[0]*30 for i in range(30)]
        self.ey=[[0]*30 for i in range(30)]
    def update_v(self):
        n=1  
        while 1:
            self.deltav=0
            tempv=[[0]*30 for i in range(30)]
            for i in range(1,29):
                for j in range(1,29):
                    tempv[i][j]=(self.v[i-1][j]+self.v[i+1][j]+self.v[i][j-1]+self.v[i][j+1])/4
                    ##进行一次运算，结果储存在tempv中
                   
            for i in range(11,17):
                tempv[i][11]=self.v1
                tempv[i][17]=self.v2
                ##初始条件修正
            for i in range(1,29):
              for j in range(1,29):
                  self.deltav+=abs(tempv[i][j]-self.v[i][j]) 
                  self.v[i][j]=tempv[i][j]
                  ##计算差值
            if self.deltav<=1e-5:           
                break
            n+=1
            if n==10000:
                break
            ##强制结束循环，防止无限循环的情况
        for i in range(30):
          print self.v[i]
        print n
        print self.deltav
    
    def electric_field(self):
        for i in range(1,29):
                for j in range(1,29):
                    self.ex[i][j]=-(self.v[i][j+1]-self.v[i][j-1])/2/self.dx
                    ##由于i是行j是列，因此ex是同一行不同列方向上的导数
                    self.ey[i][j]=-(self.v[i+1][j]-self.v[i-1][j])/2/self.dy
    
    def electric_potential_near_two_plates(self):
        plt.figure()
        plt.title('electric potential near two capacitor plates')
        plt.xlabel('x(m)')
        plt.ylabel('y(m)')
        X = np.arange(-1.5, 1.5, 0.1)
        Y = np.arange(-1.5, 1.5, 0.1)
        Z=[[0]*30 for i in range(30)]
        for i in range(0,30):
              for j in range(0,30):
                  Z[i][j]=self.v[i][j]
        CS = plt.contour(X, Y, Z, 8, alpha=1.0, cmap='jet')
        plt.clabel(CS, inline=1, fontsize=12)
        plt.colorbar(CS)
        plt.show()
    
    def electric_potential_in_three_dimension(self):
        fig = plt.figure()
        ax = Axes3D(fig)
        X = np.arange(-1.5, 1.5, 0.1)
        Y = np.arange(-1.5, 1.5, 0.1)
        X, Y = np.meshgrid(X, Y)
        Z=[[0]*30 for i in range(30)]
        for i in range(0,30):
              for j in range(0,30):
                  Z[i][j]=self.v[i][j] 
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
        ax.set_xlabel('x(m)')
        ax.set_ylabel('y(m)')
        ax.set_zlabel('voltage(V)')
        ax.set_title('voltage in 3D picture')
        plt.show()
        
    def electric_field_near_two_metal_plates(self):
        fig0, ax0 = plt.subplots()
        X = np.arange(-1.5, 1.5, 0.1)
        Y = np.arange(-1.5, 1.5, 0.1)
        strm = ax0.streamplot(X, Y, np.array(self.ex), np.array(self.ey), color=np.array(self.ex), linewidth=2, cmap=plt.cm.autumn)
        fig0.colorbar(strm.lines)
        ax0.set_xlabel('x(m)')
        ax0.set_ylabel('y(m)')
        ax0.set_title('Electric field near two plates')
        plt.show()

        
            
a=two_capacitor_paltes()
a.update_v()
a.electric_field()
a.electric_potential_near_two_plates()
a.electric_potential_in_three_dimension()
a.electric_field_near_two_metal_plates()

    
        

        