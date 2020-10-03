#!/usr/bin/env python
# -*- coding: utf8 -*-

#############################################################################



from scipy import *
from scipy.integrate import odeint
from pylab import * 



#r2_x,r2_y,r3_x,r3_y
def Fxy(r,tiempo): # devuelve las derivadas del array r
    G = 6.6726*10**(-11)
    m1=5.98*10**(24)
    m2=1.99*10**(30)
    m3=7.35*10**(22)
    a=G*m2
    b=G*m3
    c=G*m1
    d12=sqrt((r[0]-r[4])**2+(r[2]-r[6])**2)
    d13=sqrt((r[0]-r[8])**2+(r[2]-r[10])**2)
    d23=sqrt((r[4]-r[8])**2+(r[6]-r[10])**2)
    
    return array([r[1],
		    -a*((r[0]-r[4])/(d12**3))- b*((r[0]-r[8])/(d13**3)),
		    r[3],
            -a*((r[2]-r[6])/(d12**3))- b*((r[2]-r[10])/(d13**3)),
            r[5],
            -b*((r[4]-r[8])/(d23**3))- c*((r[4]-r[0])/(d12**3)),
            r[7],
            -b*((r[6]-r[10])/(d23**3))- c*((r[6]-r[2])/(d12**3)),
            r[9],
            -a*((r[8]-r[4])/(d23**3))- c*((r[8]-r[0])/(d13**3)),
            r[11],
            -a*((r[10]-r[6])/(d23**3))- c*((r[10]-r[2])/(d13**3))])
            
tiempo = linspace(0.,60*60*24*365,100000)
r10_x=0.
r10_y=1.496*10**11
r10=array([r10_x,r10_y])
r20_x=0.
r20_y=0.
r20=array([r20_x,r20_y])
r30_x=3.844*10**8
r30_y=1.496*10**11
r30=array([r30_x,r30_y])
v10_x=-29.8*10**3  
v10_y=0.
v10=array([v10_x,v10_y])
v20_x=0.
v20_y=0.
v20=array([v20_x,v20_y])
v30_x=-29.8*10**3
v30_y=1.02*10**3
v30=array([v30_x,v30_y])

rvinici=array([r10_x,v10_x,r10_y,v10_y,r20_x,v20_x,r20_y,v20_y,r30_x,v30_x,r30_y,v30_y])

r= odeint(Fxy,rvinici,tiempo)
plot(r[:,0],r[:,2],'b');plot(r[:,4],r[:,6],'r');#plot(r[:,8],r[:,10],'g')
#~ plot(r[:,0],r[:,2],"b")
#~ figure()
#~ plot(tiempo,r[:,0],"r",tiempo,r[:,2],"b")
#~ plot(r[:,4],r[:,6],"r")
#~ plot(r[:,8],r[:,10],"g")

figure()
plot(r[:,8]-r[:,0],r[:,10]-r[:,2],"g")
#~ 
#~ figure()
#~ plot(tiempo,r[:,8]-r[:,0],"g")
#~ 
#~ 
B=list(r[:,0])
a=max(B)
print a
c=B.index(a)
C=list(r[:,0])
b=min(C)
print b
d=C.index(b)
T=tiempo[76153]-tiempo[25377]
print ((2*T)/(60*60*24))

#~ E=list(r[:,8]-r[:,0])
#~ z=max(E)
#~ print z
#~ w=E.index(z)
#~ G=list(r[:,8]-r[:,0])
#~ g=min(G)
#~ print g
#~ h=G.index(g)
#~ T2=tiempo[48919]-tiempo[0]
#~ print ((2*T2)/(60*60*24))

show()



