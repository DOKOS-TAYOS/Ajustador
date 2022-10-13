#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from decimal import Decimal

from tkinter import *


#Funcion custom
def func_custom(t,\u03B1):
    y=\u03B1*t+5
    return y

def ajcustom(datos, nombre_ajuste, x_name, y_name):
    x = datos['%s'% x_name];ux=datos['u%s'% x_name];y=datos['%s'% y_name]; uy=datos['u%s'% y_name]
    ajuste=curve_fit(func_custom,x,y,sigma=uy,absolute_sigma=True)
    \u03B1=ajuste[0][0]
    s\u03B1=np.sqrt(np.diag(ajuste[1]))[0]
    s\u03B1='%.1E'% Decimal(s\u03B1)
    usus\u03B1=s\u03B1[4:];usus\u03B1=int(usus\u03B1)
    \u03B1=round(\u03B1,1-usus\u03B1)
    v_1='\u03B1={var} ,\u03C3(\u03B1)={inc}'.format(var=\u03B1, inc=s\u03B1)
    texto=v_1
    y_Ajus=func_custom(x,\u03B1)
    from matplotlib.font_manager import FontProperties
    font0 = FontProperties();fontt = font0.copy()
    fontt.set_family('serif');fontt.set_size('xx-large');fontt.set_weight('semibold')
    fonta = font0.copy();fonta.set_family('serif');fonta.set_size('xx-large');fonta.set_style('italic')
    fig, ax =plt.subplots(figsize=(16,8))
    ax.plot(x, y_Ajus, color='black', lw=1.00, ls='-')
    ax.errorbar(x, y, fmt='o',markersize=5, yerr=uy, xerr=ux, ecolor='crimson', markerfacecolor='crimson', markeredgecolor='crimson')
    ax.set_title('%s'% nombre_ajuste,fontproperties=fontt)
    ax.set_xlabel('%s'% x_name, fontproperties=fonta);ax.set_ylabel('%s'% y_name, fontproperties=fonta)
    plt.savefig('Ajuste %s.png' % nombre_ajuste, bbox_inches='tight')
    global menu
    grafica=Toplevel()
    grafica.title('%s'%nombre_ajuste)
    grafica.configure(background='midnight blue')
    grafica.imagen=PhotoImage(file='Ajuste %s.png'% nombre_ajuste)
    from tkinter import font
    grafica.parametros=Label(grafica, text=texto, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.parametros.configure(font=('Courier', 10))
    grafica.image=Label(grafica, image=grafica.imagen, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.aceptar=Button(grafica, text='Aceptar', command=grafica.destroy, width=7, bg='midnight blue', fg='lime green',activebackground='navy', activeforeground='snow')
    grafica.ecuacion=Label(grafica, text="y=\u03B1*x+5",relief="ridge",borderwidth=6, bg="midnight blue", fg="snow")
    grafica.ecuacion.pack()
    grafica.parametros.pack(side=LEFT);grafica.image.pack();grafica.aceptar.pack()
    grafica.aceptar.focus_set()
#Fin custom