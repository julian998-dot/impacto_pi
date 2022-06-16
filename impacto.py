#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Las dos líneas siguientes son necesaias para hacer 
# compatible el interfaz Tkinter con los programas basados 
# en versiones anteriores a la 8.5, con las más recientes. 
"""
Poyecto 2 DINAMICA APLICADA UMNG

Julian Cortes - 1803147
David Garcia - 1803346

NOTAS :
    
El codigo simula colisiones perfecamente elasticas ( e=1 ) sin friccion, ademas 
muestra la gafica de energia cinetica y momento lineal de ambas masas.
para poder ver estas graficas es necesario dejar correr el programa un buen
tiempo( cuantas muestras se coloquen ).
pEj: usar m1=1 m2=10 v1=v2=1 para ver las graficas saltaran cuando la simulacion
finalice usando 7000 muestras. el eje x de las graficas esta en segundos.
Si se usa para hallar pi funciona, debe colocarse un numero de muestras mayor a 7000
y entre mas sea el grado de n se debe aumentar las muestras para ver los digitos de pi.

N(PI); m1= 1kg m2=100^(n-1)kg

"""
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
import  time


def acept():# funcion que se usa cuando se presiona el boton aceptar
    inicio_de_tiempo = time.time()
    bandera=False#habilitador de graficas
    colisiones=0#contador de colisiones
    cont=-1#contador de muestras
    M1=float(m1.get())#Se toman los valores colocados en la celdas
    M2=float(m2.get())
    V02=float(v2.get())
    V01=float(v1.get())
    MU=int(muestr.get())
    Q=int(MU*0.5)
    Vel[0]=V01#condiciones iniciales de velocidad
    Vel[1]=V02
    Vel[0]=Vel[0]
    Vel[1]=-Vel[1]#se hace la velocidad de m2 negativa para que colisione con m1
    Vel1=0#variables temporales.
    Vel2=0
    xPos[0]=200#condiciones iniciales de posicion
    xPos[1]=1000
    stop=0 #contador para detener el programa
    print("Se pulso aceptar")
    while True:#bucle infinito
        cont+=1#el contador de muestras empieza a aumentar en caad iteracion
        if(Vel[1]>Vel[0] or cont>MU):#condiciones para detener el programa
             stop=stop+1
             if (xPos[1]-xPos[0]-100)>5000:
                 bandera=True
             if stop==Q or bandera==True:#si el contador de stop ha llegado a 5000 iteraciones se grafica y detiene el bucle
                 t.set("Finalizo la simulacion")
                 Momento = Tk()#En este momento se hace uso de insertar graficos en Tkinter, creando sus porpios entornos Tk().
                 Energia=Tk()
                 Momento.wm_title("Grafica de Momento lineal[Kgm/s]")
                 Energia.wm_title("Grafica de Energia[J]")
                 fig1 = Figure(figsize=(5, 4), dpi=100)
                 fig2 = Figure(figsize=(5, 4), dpi=100)
                 fig1.add_subplot(111).plot(tiempoa,Mom1)
                 fig1.add_subplot(111).plot(tiempob,Mom2)
                 canvasM = FigureCanvasTkAgg(fig1, master=Momento)  # CREAR AREA DE DIBUJO DE TKINTER.
                 canvasM.draw()
                 canvasM.get_tk_widget().pack(side="top", fill="both", expand=1)
                 canvasM.get_tk_widget().pack(side="top", fill="both", expand=1)
                 ##
                 fig2.add_subplot(111).plot(tiempoa,E1)
                 fig2.add_subplot(111).plot(tiempob,E2)
                 canvasE = FigureCanvasTkAgg(fig2, master=Energia)  # CREAR AREA DE DIBUJO DE TKINTER.
                 canvasE.draw()
                 canvasE.get_tk_widget().pack(side="top", fill="both", expand=1)
                 canvasE.get_tk_widget().pack(side="top", fill="both", expand=1)
                 Momento.mainloop()
                 Energia.mainloop()
                 break#se rompe el while infinito.
        
        if ((xPos[0]+100)==xPos[1]) or (xPos[1]-xPos[0]-100)<0.0:#condicion de choque entre masas
            colisiones+=1#aumenta las colisones
            Vel1=Vel[0]#se asiganas las variables temporales
            Vel2=Vel[1]
            Vel[0]=(M1*Vel1+M2*Vel2-(Vel1-Vel2)*M2)/(M1+M2)#se depeja de la formula sabiendo que e=1
            Vel[1]=Vel1-Vel2+Vel[0]#con e=1 se tiene que la otra velocidad es esta formula
            r.set(colisiones)
        if (xPos[0]-40<0):#condicion de choque con la pared
            colisiones+=1
            Vel[0]=-Vel[0]#cambia el sentido de la velocidad
            r.set(colisiones)
            print("choco pared")#indicativo de funcionaminto
        Canvas.delete("all")#se elimina todo de el canvas para hacer una actulizacion
        Canvas.create_rectangle(1500, 390, 40, 350, fill="black")#se crea el piso y la pared
        Canvas.create_rectangle(40, 390, 10, 75, fill="black")
        tiempo_final = time.time()
        for Num in range(2):#se crea un for para crear los bloques sus posiciones 
            xPos[Num]=xPos[Num]+Vel[Num]*0.5# de la ecuacion cinematica de posicion 
            Canvas.create_rectangle(xPos[Num],250,xPos[Num]+100,350, fill=color[Num])#se crea el objeto en su sitio
            t.set("Simulando...")#indicativo de funcionamiento de la posicion de m1
            tempo=tiempo_final-inicio_de_tiempo
            if stop<(Q):#condiciones de llenar los vectores de muestras
                if Num==0:
                    Mom1.append(M1*Vel[Num])
                    E1.append((M1*(Vel[Num]**2))/2)
                    tiempoa.append(tempo)
                    # Mom1[cont]=M1*Vel[Num]
                    # E1[cont]=(M1*(Vel[Num]**2))/2
                if Num==1:
                    Mom2.append(M1*Vel[Num])
                    E2.append((M1*(Vel[Num]**2))/2)
                    tiempob.append(tempo)
                    # Mom2[cont]=M1*Vel[1]
                    # E2[cont]=(M1*(Vel[1]**2))/2
        root.update()#se actualiza el entorno en cada iteracion
#variables usadas como listas.
xPos=[]
Vel=[]
Mom1=[]
Mom2=[]
E1=[]
E2=[]
tiempoa=[]
tiempob=[]
muestras=[]
color=["cyan","red"]
root = Tk()#raiz de el entorno Tk
bandera= False
root.config(bd=15)
root.geometry('1650x600') #se crea el entorno grafico de unas dimesniones
root.title('Colisiones para PI')
#variables asociadas a las casillas de texto
m1 = StringVar()
m2 = StringVar()
r = StringVar()
t = StringVar()
v1 = StringVar()
v2 = StringVar()
muestr = StringVar()
#se inician las listas de velociadd y posicion
for i in range(2):
    xPos.append(i)
    Vel.append(i)
#se crea el entorno de la interfaz. botones, cuadros de texto, labels... etc.
label = Label(root,text="Masa 1")
label.place(x=20,y=500)
#places the label in the following x and y coordinates
e1=Entry(root, textvariable=m1)
e1.place(x=20,y=520)
label2 = Label(root,text="Masa 2")
label2.place(x=190,y=500)
e2=Entry(root, textvariable=m2)
e2.place(x=190,y=520)
l3=Label(root, text="Colisiones")
l3.place(x=20,y=430)##############<<<---
e3=Entry(root, justify="left", textvariable=r, state="disabled")
e3.place(x=20,y=450)
label4 = Label(root,text="Velocidad inicial m2")
label4.place(x=340,y=500)
e4=Entry(root, textvariable=v2)
e4.place(x=340,y=520)
label5 = Label(root,text="Velocidad inicial m1")
label5.place(x=470,y=500)
e5=Entry(root, textvariable=v1)
e5.place(x=470,y=520)
b1=Button(root, text="Aceptar", command=acept)#boton de aceptar
b1.place(x=610,y=520)
b2=Button(root, text="SALIR", command=root.destroy)#boton de salir
b2.place(x=680,y=520)
qq=Entry(root, justify="left", textvariable=t, state="disabled")
qq.place(x=200,y=450)
##
label6 = Label(root,text="Numero de muestras (mayor o igual a 7000)")
label6.place(x=350,y=430)
e6=Entry(root, textvariable=muestr)
e6.place(x=350,y=450)
Canvas=Canvas(root, bg="white",width=1200, height=400)# Se crea el 'Canvas' para la simulacion de la colision
Canvas.pack(fill="both", expand=False)
root.mainloop()

    