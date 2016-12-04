# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 22:40:56 2016

@author: yjq
"""
import pylab as pl
import math as m
class hyperion:
    def __init__(self,xc=1,yc=0,vx=0,vy=2*m.pi,time_step=0.0001,theta1=0,omega1=0,\
    theta2=0.01,omega2=0):
        self.rc=[(xc**2+yc**2)**0.5]
        self.xc=[xc]
        self.yc=[yc]
        self.vx=[vx]
        self.vy=[vy]
        self.dt=time_step
        self.t=[0]
        self.theta1=[theta1]
        self.omega1=[omega1]
        self.theta2=[theta2]
        self.omega2=[omega2]
        self.dtheta=[m.log(theta2-theta1)]
        self.line=[m.log(theta2-theta1)]
    def calculate(self):
        for i in range(40000):
            self.rc.append((self.xc[-1]**2+self.yc[-1]**2)**0.5)
            self.vx.append(self.vx[-1]-4*(m.pi**2)*self.xc[-1]*self.dt/self.rc[-1]**3)
            self.vy.append(self.vy[-1]-4*(m.pi**2)*self.yc[-1]*self.dt/self.rc[-1]**3)
            self.xc.append(self.xc[-1]+self.vx[-1]*self.dt)
            self.yc.append(self.yc[-1]+self.vy[-1]*self.dt)
            ##质心的椭圆轨道
            
            temp1=self.xc[-1]*m.sin(self.theta1[-1])-self.yc[-1]*m.cos(self.theta1[-1])
            temp2=self.xc[-1]*m.sin(self.theta1[-1])+self.yc[-1]*m.cos(self.theta1[-1])
            self.omega1.append(self.omega1[-1]-12*(m.pi**2)*temp1*temp2*self.dt/(self.rc[-1]**5))
            temp_theta1=self.theta1[-1]+self.omega1[-1]*self.dt
            while(temp_theta1>=m.pi):
                 temp_theta1-=2*m.pi
            while(temp_theta1<=-m.pi):
                 temp_theta1+=2*m.pi
            self.theta1.append(temp_theta1)
            
            temp1=self.xc[-1]*m.sin(self.theta2[-1])-self.yc[-1]*m.cos(self.theta2[-1])
            temp2=self.xc[-1]*m.sin(self.theta2[-1])+self.yc[-1]*m.cos(self.theta2[-1])
            self.omega2.append(self.omega2[-1]-12*(m.pi**2)*temp1*temp2*self.dt/(self.rc[-1]**5))
            temp_theta2=self.theta2[-1]+self.omega2[-1]*self.dt
            while(temp_theta2>=m.pi):
                 temp_theta2-=2*m.pi
            while(temp_theta2<=-m.pi):
                 temp_theta2+=2*m.pi
            self.theta2.append(temp_theta2)
            
            D=abs(self.theta1[-1]-self.theta2[-1])
            self.dtheta.append(m.log(D))
            self.line.append(self.line[0]+1.*self.t[i])
            self.t.append(self.t[-1] + self.dt)
        
    def show_results(self):
        pl.plot(self.t,self.dtheta,'.')  
        pl.plot(self.t,self.line,'-')
        pl.title('$Hyperion$ $\\Delta\\theta$ $versus$ $time$')
        pl.xlabel('$time(yr)$')
        pl.ylabel('$\\Delta\\theta$$(radians)$')
        pl.text(0.7,0,'$\lambda$=1',fontsize=15)
        pl.show
        
a=hyperion()
a.calculate()
a.show_results()
    