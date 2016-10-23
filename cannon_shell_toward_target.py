# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 21:40:24 2016

@author: yjq
"""


import pylab as pl
import math
N=[99999,9999]
X=[0,0]
Y=[0,0]
class cannon_shell_toward_target:
    def __init__(self,g=9.8,time_step=0.01,initial_v=700,x=0,y=0,a=0.0065,\
    alpha=2.5,b2=0.00004,m=1,T0=288.15,initial_theta=math.pi/4,x0=12000,y0=2500.0):
        #the unit of theta is rad
        self.x0=x0
        self.y0=y0
        self.k=y0/x0        
        self.m=m
        self.a=a
        self.alpha=alpha
        self.T0=T0
        self.v=initial_v
        self.theta=initial_theta
        self.x=[x]
        self.y=[y]
        self.vx=[self.v*math.cos(self.theta)]
        self.vy=[self.v*math.sin(self.theta)]
        self.g=g
        self.dt=time_step
        self.B2=[b2/m]
    
    def calculate(self):
        i=0
        while(1):
            tempv=(self.vx[i]**2+self.vy[i]**2)**0.5
            self.B2.append(self.B2[0]*(1-self.a*self.y[i]/self.T0)**self.alpha)
            self.x.append(self.x[i]+self.vx[i]*self.dt)
            self.y.append(self.y[i]+self.vy[i]*self.dt)
            self.vx.append(self.vx[i]-self.B2[i]*self.vx[i]*tempv*self.dt/self.m)
            self.vy.append(self.vy[i]-(self.g+self.B2[i]*self.vy[i]*tempv/self.m)*self.dt)
            i+=1
            if(self.x[i]>self.x0): 
                global N,X,Y
                distance=((self.x[i]-self.x0)**2+(self.y[i]-self.y0)**2)**0.5
                N+=[distance]
                X+=[self.x[i]]
                Y+=[self.y[i]]
                break
            
    def show_results(self):
        pl.plot(self.x,self.y)
        pl.title('Trajectory of cannon shell')
        pl.xlabel('x($m$)')
        pl.ylabel('y($m$)')
        pl.show()
    
    def compare(self):
        
        n=math.atan(self.k)*180/math.pi
        print n
        while(n<90):
            a=cannon_shell_toward_target(initial_theta=n*math.pi/180)
            a.calculate()
            if(N[-1]>N[-2]):
                a.show_results()
                print "炮弹离目标点距离为:",N[-2]
                print "炮弹落点为:",X[-2],Y[-2]
                print "炮弹出射角为:",n
                break
            n+=0.04
       
                
a=cannon_shell_toward_target()
a.compare()                  
 