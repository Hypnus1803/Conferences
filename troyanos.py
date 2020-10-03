#!/usr/bin/env python
# -*- coding: utf8 -*-

####################################################################################################################
################ Los numeros que aparecen en los parentesis cuadrados de las r's   #################################
################ hablan de la posición que estan ocupando en el array rvinici.     #################################
################ Se uso el sistema S.I. y no el de coordenadas astronomicas porque #################################
################ el código originalmente estaba en coord. S.I.                    ################################## 
####################################################################################################################

from scipy import *
from scipy.integrate import odeint
from pylab import * 



#r2_x,r2_y,r3_x,r3_y
def Fxy(r,tiempo): # devuelve las derivadas del array r
############################################################################
########## Estas primeras lineas es para definir constantes         #######
########## tales como la masa, la constante de Cavendich y tambien  ########
########## para reducir un poco la forma de escribir las ecuaciones ########
########## de movimiento                                            ########
############################################################################
    G = 6.6726*10**(-11)
    m1=1.899*10**(27)
    m2=1.99*10**(30)
    m3=(1./100000000)*5.97*10**(24)
    m4=(1./100000)*5.97*10**(24)
    a=G*m2
    b=G*m3
    c=G*m1
    h=G*m4
    d12=sqrt((r[0]-r[4])**2+(r[2]-r[6])**2)
    d13=sqrt((r[0]-r[8])**2+(r[2]-r[10])**2)
    d23=sqrt((r[4]-r[8])**2+(r[6]-r[10])**2)
    d14=sqrt((r[0]-r[12])**2+(r[2]-r[14])**2)
    d24=sqrt((r[4]-r[12])**2+(r[6]-r[14])**2)
    d34=sqrt((r[8]-r[12])**2+(r[10]-r[14])**2)
#################################################################################################
############# Aqui nos retorna un array donde primero va la velocidad   #########################
############# osea dr/dt y la siguiente es la fuerza gravitacional es   #########################
############# decir la parte de dv/dt. y asi para cada velocidad y      #########################
############# de cada cuerpo en cada coordenada en el plano.            #########################
#################################################################################################
    return array([r[1],
		    -a*((r[0]-r[4])/(d12**3))- b*((r[0]-r[8])/(d13**3)) - h*((r[0]-r[12])/(d14**3)),
		    r[3],
            -a*((r[2]-r[6])/(d12**3))- b*((r[2]-r[10])/(d13**3)) - h*((r[2]-r[14])/(d14**3)),
            r[5],
            -b*((r[4]-r[8])/(d23**3))- c*((r[4]-r[0])/(d12**3)) - h*((r[4]-r[12])/(d24**3)),
            r[7],
            -b*((r[6]-r[10])/(d23**3))- c*((r[6]-r[2])/(d12**3)) - h*((r[6]-r[14])/(d24**3)),
            r[9],
            -a*((r[8]-r[4])/(d23**3))- c*((r[8]-r[0])/(d13**3))- h*((r[8]-r[12])/(d34**3)),
            r[11],
            -a*((r[10]-r[6])/(d23**3))- c*((r[10]-r[2])/(d13**3))- h*((r[10]-r[14])/(d34**3)),
            r[13],
            -a*((r[12]-r[4])/(d24**3))- c*((r[12]-r[0])/(d14**3))-b*((r[12]-r[8])/(d34**3)),
            r[15],
            -a*((r[14]-r[6])/(d24**3))- c*((r[14]-r[2])/(d14**3))-b*((r[14]-r[10])/(d34**3))])
            
            
tiempo = linspace(0.,60*60*24*365*120,1000) 
########## Este es el arreglo que da valores temporales en segundos de 12 años ######## 
########## (periodo sideral de jupiter y el troyano 'aprox.')                  ########
#####################################################################################################################################
################# Aqui empiezan las condiciones iniciales para cada objeto en cada coordenada #######################################
######################################################################################################################################
r10_x=5.2*(1.496*10**11)
r10_y=0.
#~ r10=array([r10_x,r10_y])
r20_x=0.
r20_y=0.
#~ r20=array([r20_x,r20_y])
r30_x=r10_x*cos(pi/3)
r30_y=-r10_x*sin(pi/3)
#~ r30=array([r30_x,r30_y])
r40_x=r10_x*cos(pi/3)
r40_y=r10_x*sin(pi/3)
########################
v10_x=0.  
v10_y=13.0697*10**3
#~ v10=array([v10_x,v10_y])
v20_x=0.
v20_y=0.
#~ v20=array([v20_x,v20_y])
v30_x=13.0406*10**3*cos(pi/6)    
v30_y=13.0406*10**3*sin(pi/6)    
#~ v30=array([v30_x,v30_y])
v40_x=-13.0300*10**3*cos(pi/6)    
v40_y=13.0300*10**3*sin(pi/6) 
############################################################################################
################ Aqui hago un array con las condiciones iniciales  #########################
################ en el mismo orden como aparecen en la funcion Fxy #########################
##############################################################################################
rvinici=array([r10_x,v10_x,r10_y,v10_y,r20_x,v20_x,r20_y,v20_y,r30_x,v30_x,r30_y,v30_y,r40_x,v40_x,r40_y,v40_y])
################# Y aqui aplico la funcion odeint                  #############################
r= odeint(Fxy,rvinici,tiempo)

axhline(y=0.,xmin=0.5,xmax= 5.2*(1.496*10**11))
plot([0.5,5.2*(1.496*10**11)*cos(pi/3)],[0.,-5.2*(1.496*10**11)*sin(pi/3)],'b')
plot([0.5,5.2*(1.496*10**11)*cos(pi/3)],[0.,5.2*(1.496*10**11)*sin(pi/3)],'b')
plot([0.5,r[199,0]],[0.,r[199,2]],'k--')
plot([0.5,r[199,8]],[0.,r[199,10]],'k--')
plot([0.5,r[199,12]],[0.,r[199,14]],'k--')

plot([0.5,5.2*(1.496*10**11)*cos(pi/3)],[0.,5.2*(1.496*10**11)*sin(pi/3)],'b')
plot(r[:,0],r[:,2],'b');plot(r[:,4],r[:,6],'r');plot(r[:,8],r[:,10],'g');plot(r[:,12],r[:,14],'y');plot(r[0,0],r[0,2],'mo');plot(r[0,8],r[0,10],'go');plot(r[0,12],r[0,14],'mo');plot(r[0,8],r[0,10],'mo');plot(r[199,0],r[199,2],'r*');plot(r[199,8],r[199,10],'r*');plot(r[199,12],r[199,14],'r*')
ylabel('Y [m]')
xlabel('X [m]')
title('TRAYECTORIA')

show()

figure()
plot(tiempo,sqrt((r[:,9])**2+(r[:,11])**2))
plot(tiempo,sqrt((r[:,13])**2+(r[:,15])**2))
ylabel('Velocidad [m/s]')
xlabel('Tiempo [s]')
legend(['Enomo','Hektor'])
title('Velocidad')
grid()
show()



#~ #############################Encontrar el angulo#################################
Theta1=[]
Theta2=[]
for i in range(len(r)):
	a=sqrt((r[i,4]-r[i,0])**2+(r[i,6]-r[i,2])**2)
	b=sqrt((r[i,4]-r[i,8])**2+(r[i,6]-r[i,10])**2)
	c=sqrt((r[i,8]-r[i,0])**2+(r[i,10]-r[i,2])**2)
	p=c**2-a**2-b**2
	q=-2*a*b
	theta=(arccos(p/q))*180/pi
	Theta1.append(theta)

for j in range(len(r)):
	a=sqrt((r[j,4]-r[j,0])**2+(r[j,6]-r[j,2])**2)
	k=sqrt((r[j,4]-r[j,12])**2+(r[j,6]-r[j,14])**2)
	l=sqrt((r[j,12]-r[j,0])**2+(r[j,14]-r[j,2])**2)
	p=l**2-a**2-k**2
	q=-2*a*k
	theta1=(arccos(p/q))*180/pi
	Theta2.append(theta1)


def sumar(x,y):
	return x+y
sumita1=reduce(sumar,Theta1)
sumita2=reduce(sumar,Theta2)
prom1=sumita1/1000
prom2=sumita2/1000
print prom1,prom2

E1=[]
E2=[]
for i in range(len(Theta1)):
	e1=abs(60-Theta1[i])/60
	e2=abs(60-Theta2[i])/60
	E1.append(e1)
	E2.append(e2)


plot(tiempo,E1,'b--');plot(tiempo,E2,'g--')
ylabel('Error del Angulo [Grados]')
xlabel('Tiempo [s]')
legend(['Enomo', 'Hektor'])
title('Error Normalizado')
grid()
show()


figure()
plot(tiempo,Theta1);plot(tiempo,Theta2)
ylabel('Angulo [Grados]')
xlabel('Tiempo [seg]')
legend(['Enomo', 'Hektor'])
grid()
title('Angulo del asteroide con respecto a la linea que une al Jupiter y el Sol')
show()


