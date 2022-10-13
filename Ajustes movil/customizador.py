#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from decimal import Decimal

from tkinter import *


#Funcion custom
def func_custom(t,a,b):
    y=8*a+7*t+b
    return y

def ajcustom(datos, nombre_ajuste, x_name, y_name):
    x = datos['%s'% x_name];ux=datos['u%s'% x_name];y=datos['%s'% y_name]; uy=datos['u%s'% y_name]
    ajuste=curve_fit(func_custom,x,y,sigma=uy,absolute_sigma=True)
    a,b=ajuste[0]
    sa,sb=np.sqrt(np.diag(ajuste[1]))
    sa='%.1E'% Decimal(sa)
    ususa=sa[4:];ususa=int(ususa)
    a=round(a,1-ususa)

    sb='%.1E'% Decimal(sb)
    ususb=sb[4:];ususb=int(ususb)
    b=round(b,1-ususb)
    v_1='a={var} ,\u03C3(a)={inc}'.format(var=a, inc=sa)
    v_2='b={var} ,\u03C3(b)={inc}'.format(var=b, inc=sb)
    texto=v_1+'\n'+v_2
    y_Ajus=func_custom(x,a,b)
    from matplotlib.font_manager import FontProperties
    font0 = FontProperties();fontt = font0.copy()
    fontt.set_family('serif');fontt.set_size('xx-large');fontt.set_weight('semibold')
    fonta = font0.copy();fonta.set_family('serif');fonta.set_size('xx-large');fonta.set_style('italic')
    fig, ax =plt.subplots(figsize=(12,6))
    ax.plot(x, y_Ajus, color='black', lw=1.00, ls='-')
    ax.errorbar(x, y, fmt='o',markersize=5, yerr=uy, xerr=ux, ecolor='crimson', markerfacecolor='crimson', markeredgecolor='crimson')
    ax.set_title('%s'% nombre_ajuste,fontproperties=fontt)
    ax.set_xlabel('%s'% x_name, fontproperties=fonta);ax.set_ylabel('%s'% y_name, fontproperties=fonta)
    plt.savefig('Graficas/Ajuste %s.png' % nombre_ajuste, bbox_inches='tight')
    global menu
    grafica=Toplevel()
    grafica.title('%s'%nombre_ajuste)
    grafica.configure(background='midnight blue')
    grafica.imagen=PhotoImage(file='Graficas/Ajuste %s.png'% nombre_ajuste)
    from tkinter import font
    grafica.parametros=Label(grafica, text=texto, relief='ridge',borderwidth=3, bg='midnight blue', fg='snow')
    grafica.parametros.configure(font=('Courier', 5))
    grafica.image=Label(grafica, image=grafica.imagen, relief='ridge',borderwidth=3, bg='midnight blue', fg='snow')
    grafica.aceptar=Button(grafica, text='Aceptar', command=grafica.destroy, width=15, bg='midnight blue', fg='lime green',activebackground='navy', activeforeground='snow')
    grafica.ecuacion=Label(grafica, text="y=8*a+7*x+b",relief="ridge",borderwidth=3, bg="midnight blue", fg="snow")
    grafica.ecuacion.pack()
    grafica.parametros.pack(side=LEFT);grafica.image.pack();grafica.aceptar.pack()
    grafica.aceptar.focus_set()
#Fin custom