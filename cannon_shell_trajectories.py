# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 23:41:22 2016

@author: yjq
"""

import pylab as pl
import math

class cannon_shell_trajectories:
    def __init__(self,g=9.8,time_step=0.05,\
    initial_v=10.0,initial_theta=math.pi/4,\
    x=0,y=0):
        #the unit of theta is rad
        self.v=initial_v
        self.theta=initial_theta
        self.x=[x]
        self.y=[y]
        self.vx=[self.v*math.sin(self.theta)]
        self.vy=[self.v*math.cos(self.theta)]
        self.g=g
        self.dt=time_step
    
    def calculate(self):
        i=0
        while(1):
            tempvx=self.vx[i]
            tempvy=self.vy[i]-self.g*self.dt
            tempx=self.x[i]+self.vx[i]*self.dt
            tempy=self.y[i]+self.vy[i]*self.dt
            self.x.append(tempx)
            self.y.append(tempy)
            self.vx.append(tempvx)
            self.vy.append(tempvy)
            i+=1
            if(tempy<0): break

    def show_results(self):
        pl.plot(self.x,self.y)
        pl.title('Trajectory of cannon shell')
        pl.xlabel('x($km$)')
        pl.ylabel('y($km$)')
        pl.ylim(0,5)
        pl.show()

a=cannon_shell_trajectories()
a.calculate()
a.show_results()
                   
            
            
        