# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 22:40:56 2016

@author: yjq
"""
import pylab as pl
import math as m
class elliptical_orbits:
    def __init__(self,x=1.0,y=0,vx=0,vy=2.*m.pi,time_step=0.002,beta=2.1):
        self.r=[(x**2+y**2)**0.5]
        self.x=[x]
        self.y=[y]
        self.vx=[vx]
        self.vy=[vy]
        self.dt=time_step
        self.t=[0]
        self.beta=beta
    def calculate(self):
        for i in range(10000):
            self.r.append((self.x[-1]**2+self.y[-1]**2)**0.5)
            self.vx.append(self.vx[i]-4*(m.pi**2)*self.x[i]*self.dt/self.r[i]**(self.beta+1))
            self.vy.append(self.vy[i]-4*(m.pi**2)*self.y[i]*self.dt/self.r[i]**(self.beta+1))
            self.x.append(self.x[i]+self.vx[i+1]*self.dt)
            self.y.append(self.y[i]+self.vy[i+1]*self.dt)
            self.t.append(self.dt)
        
    def show_results(self):
        pl.plot(self.x,self.y)
        pl.plot(0,0,'r.')
        pl.title('simulation of elliptical orbot')
        pl.text(0.7,0.8,'beta=2.1',fontsize=15)
        pl.xlabel('x(AU)')
        pl.ylabel('y(AU)')
        
        pl.show
a=elliptical_orbits()
a.calculate()
a.show_results()
    