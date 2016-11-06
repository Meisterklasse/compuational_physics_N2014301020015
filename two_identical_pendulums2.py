# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 22:48:13 2016

@author: yjq
"""

import pylab as pl
import math
class two_identical_pendulums:
    def __init__(self,q=0.5,g=9.8,l=9.8,OmegaD=2.0/3.0,time_step=0.04,FD=1.2,\
    time_of_duration=60,theta1=0.20,theta2=0.199):
        self.omega1=[0]
        self.omega2=[0]
        self.theta1=[theta1]
        self.theta2=[theta2]
        self.q=q
        self.g=g
        self.l=l
        self.OmegaD=OmegaD
        self.FD=FD
        self.dtheta=[theta1-theta2]
        self.t=[0]
        self.dt=time_step
        self.time=time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        self.line=[math.log(self.dtheta[0])]
        
    def calculate(self):
        for i in range(self.nsteps):
            self.t.append(self.t[i] + self.dt)
            
            temp_omega1=self.omega1[-1]-(self.g/self.l)*\
            math.sin(self.theta1[-1])*self.dt -self.q*self.omega1[-1]*self.dt +\
            self.FD*math.sin(self.OmegaD*self.t[-1])*self.dt
            self.omega1.append(temp_omega1)            
            #这是omega（i+1）的算式
            temp_theta1=self.theta1[-1]+self.omega1[-1]*self.dt
            #这是theta（i+1）
            if(temp_theta1>=math.pi):
                 temp_theta1-=2*math.pi
            if(temp_theta1<=-math.pi):
                 temp_theta1+=2*math.pi
            self.theta1.append(temp_theta1)#以上是第一个摆
            
            temp_omega2=self.omega2[-1]-(self.g/self.l)*\
            math.sin(self.theta2[-1])*self.dt -self.q*self.omega2[-1]*self.dt +\
            self.FD*math.sin(self.OmegaD*self.t[-1])*self.dt
            self.omega2.append(temp_omega2)            
            #这是omega（i+1）的算式
            temp_theta2=self.theta2[-1]+self.omega2[-1]*self.dt
            #这是theta（i+1）
            while(temp_theta2>=math.pi):
                 temp_theta2-=2*math.pi
            while(temp_theta2<=-math.pi):
                 temp_theta2+=2*math.pi
            self.theta2.append(temp_theta2)#以上是第二个摆
            
            D=abs(self.theta1[-1]-self.theta2[-1])
            self.dtheta.append(math.log(D))
            self.line.append(math.log(self.dtheta[0])+0.08*self.t[i])
           
                
    def show_results(self):
        pl.plot(self.t, self.dtheta)
        pl.plot(self.t,self.line,'--')
        pl.show()
        
a=two_identical_pendulums()
a.calculate()
a.show_results()

        