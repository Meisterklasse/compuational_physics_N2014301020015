# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 23:50:23 2016

@author: yjq
"""

import pylab as pl
import math
class billiard_problem:
    def __init__(self,x0=0,y0=-10.0,vx0=1.5,vy0=1.2,dt=0.01):
        self.x=[x0]
        self.y=[y0]
        self.vx=vx0
        self.vy=vy0
        self.dt=dt
        self.t=[0]
        self.xx=[]
        self.yy=[]
        
    
    def calculate(self):
        for i in range(0,360):
            self.xx.append(5*math.cos(1*i))
            self.yy.append(5*math.sin(1*i))
        for i in range(0,50000):
            
            
            if self.x[-1]>10 or self.x[-1]<-10:
                self.vx=-self.vx
            if self.y[-1]>10 or self.y[-1]<-10:
                self.vy=-self.vy
            #正方形外框
            if self.x[-1]**2+self.y[-1]**2<=25:
                tempvx=(2*self.x[-1]*self.y[-1]*self.vy+(self.x[-1]**2+self.y[-1]**2)*self.vx)/(self.y[-1]**2-self.x[-1]**2)
                tempvy=(2*self.x[-1]*self.y[-1]*self.vx+(self.x[-1]**2+self.y[-1]**2)*self.vy)/(-self.y[-1]**2+self.x[-1]**2)
                self.vx=tempvx
                self.vy=tempvy
            print self.x[-1]
            print self.y[-1]
            print self.vx
            print self.vy
            print'---'
            
            
            self.x.append(self.x[-1]+self.vx*self.dt)
            self.y.append(self.y[-1]+self.vy*self.dt)
            
            
            
           
            
                   
                
            self.t.append(self.dt)
    def show_results(self):
        pl.plot(self.x,self.y)
        pl.plot(self.xx,self.yy,".")
        pl.xlim(-10,10)
        pl.ylim(-10,10)
        pl.show()
        

a=billiard_problem()
a.calculate()
a.show_results()