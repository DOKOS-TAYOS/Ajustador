#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from decimal import Decimal

from tkinter import *

def func_linealn(t,m,n):
    y =m*t+n
    return y

def func_lineal(t,m):
    y =m*t
    return y

def func_cuadrat(t, a, b, c):
    y =a+b*t+c*t**2
    return y

def func_cuad(t,a):
    y =a*t**2
    return y

def func_cuarta(t,a):
    y =a*t**2
    return y

def func_sin(t,a,b):
    y =a*np.sin(b*t)
    return y

def func_sinc(t,a,b,c):
    y =a*np.sin(b*t+c)
    return y

def func_cos(t,a,b):
    y =a*np.cos(b*t)
    return y

def func_cosc(t,a,b,c):
    y =a*np.cos(b*t+c)
    return y

def func_sinh(t,a,b):
    y =a*np.sinh(b*t)
    return y

def func_cosh(t,a,b):
    y =a*np.cosh(b*t)
    return y

def func_ln(t,a):
    y =a*np.log(t)
    return y

def func_inv(t,a):
    y =a/t
    return y

def func_invcuad(t,a):
    y =a/(t**2)
    return y


def ajlinealn(datos, nombre_ajuste, x_name, y_name):
    x = datos['%s'% x_name];ux=datos['u%s'% x_name];y=datos['%s'% y_name]; uy=datos['u%s'% y_name]

    ajuste=curve_fit(func_linealn,x,y,sigma=uy,absolute_sigma=True)

    m,n = ajuste[0]
    
    
    sm,sn=np.sqrt(np.diag(ajuste[1]))
    
    sm='%.1E'% Decimal(sm)
    ususm=sm[4:]; ususm=int(ususm)
    m=round(m, 1-ususm)
    
    sn='%.1E'% Decimal(sn)
    ususn=sn[4:]; ususn=int(ususn)
    n=round(n, 1-ususn)
   

    v_1='m={var} ,\u03C3(m)={inc}'.format(var=m, inc=sm)
    v_2='n={var} ,\u03C3(n)={inc}'.format(var=n, inc=sn)
    texto=v_1+'\n'+v_2
    

    y_Ajus=func_linealn(x,m,n)
    
    #Ahora graficamos y guardamos
    from matplotlib.font_manager import FontProperties
    font0 = FontProperties();fontt = font0.copy()
    fontt.set_family('serif');fontt.set_size('xx-large');fontt.set_weight('semibold')
    fonta = font0.copy();fonta.set_family('serif');fonta.set_size('xx-large');fonta.set_style('italic')
    
    
    fig, ax =plt.subplots(figsize=(12,6))
    
    ax.plot(x, y_Ajus, color="black", lw=1.00, ls='-')
    ax.errorbar(x, y, fmt='o',markersize=5, yerr=uy, xerr=ux, ecolor='crimson', markerfacecolor='crimson', markeredgecolor='crimson')
    
    ax.set_title('%s'% nombre_ajuste,fontproperties=fontt)
    ax.set_xlabel('%s'% x_name, fontproperties=fonta);ax.set_ylabel('%s'% y_name, fontproperties=fonta)
    plt.savefig("Graficas\\Ajuste %s.png" % nombre_ajuste, bbox_inches='tight')
    
    global menu
    grafica=Toplevel()
    grafica.title('%s'%nombre_ajuste)
    grafica.configure(background='midnight blue')
    grafica.imagen=PhotoImage(file="Graficas\\Ajuste %s.png"% nombre_ajuste)
    from tkinter import font
    grafica.parametros=Label(grafica, text=texto, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.parametros.configure(font=('Courier', 10))
    
    grafica.image=Label(grafica, image=grafica.imagen, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.aceptar=Button(grafica, text='Aceptar', command=grafica.destroy, width=7, bg='midnight blue', fg='lime green',activebackground='navy', activeforeground='snow')
    grafica.ecuacion=Label(grafica, text="y={0}x+{1}".format(m,n),relief="ridge",borderwidth=6, bg="midnight blue", fg="snow")
    
    grafica.ecuacion.pack(padx=3, pady=3)
    grafica.parametros.pack(side=LEFT,padx=3, pady=3);grafica.image.pack(padx=3, pady=3);grafica.aceptar.pack(padx=3, pady=3)
    grafica.aceptar.focus_set()
    
    
    
    
def ajlineal(datos, nombre_ajuste, x_name, y_name):
    x = datos['%s'% x_name];ux=datos['u%s'% x_name];y=datos['%s'% y_name]; uy=datos['u%s'% y_name]

    ajuste=curve_fit(func_lineal,x,y,sigma=uy,absolute_sigma=True)

    m= ajuste[0][0]

    sm=np.sqrt(np.diag(ajuste[1]))[0]
    
    sm='%.1E'% Decimal(sm)
    ususm=sm[4:]; ususm=int(ususm)
    m=round(m, 1-ususm)

    v_1='m={var} ,\u03C3(m)={inc}'.format(var=m, inc=sm)
    texto=v_1
    

    y_Ajus=func_lineal(x,m)
    
    #Ahora graficamos y guardamos
    from matplotlib.font_manager import FontProperties
    font0 = FontProperties();fontt = font0.copy()
    fontt.set_family('serif');fontt.set_size('xx-large');fontt.set_weight('semibold')
    fonta = font0.copy();fonta.set_family('serif');fonta.set_size('xx-large');fonta.set_style('italic')
    
    
    fig, ax =plt.subplots(figsize=(12,6))
    
    ax.plot(x, y_Ajus, color="black", lw=1.00, ls='-')
    ax.errorbar(x, y, fmt='o',markersize=5, yerr=uy, xerr=ux, ecolor='crimson', markerfacecolor='crimson', markeredgecolor='crimson')
    
    ax.set_title('%s'% nombre_ajuste,fontproperties=fontt)
    ax.set_xlabel('%s'% x_name, fontproperties=fonta);ax.set_ylabel('%s'% y_name, fontproperties=fonta)
    plt.savefig("Graficas\\Ajuste %s.png" % nombre_ajuste, bbox_inches='tight')
    
    global menu
    grafica=Toplevel()
    grafica.title('%s'%nombre_ajuste)
    grafica.configure(background='midnight blue')
    grafica.imagen=PhotoImage(file="Graficas\\Ajuste %s.png"% nombre_ajuste)
    from tkinter import font
    grafica.parametros=Label(grafica, text=texto, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.parametros.configure(font=('Courier', 10))
    
    grafica.image=Label(grafica, image=grafica.imagen, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.aceptar=Button(grafica, text='Aceptar', command=grafica.destroy, width=7, bg='midnight blue', fg='lime green',activebackground='navy', activeforeground='snow')
    grafica.ecuacion=Label(grafica, text='y={0}x'.format(m),relief="ridge",borderwidth=6, bg="midnight blue", fg="snow")
    
    grafica.ecuacion.pack(padx=3, pady=3)
    grafica.parametros.pack(side=LEFT,padx=3, pady=3);grafica.image.pack(padx=3, pady=3);grafica.aceptar.pack(padx=3, pady=3)
    grafica.aceptar.focus_set()
    
    
    
    
def ajcuadrat(datos, nombre_ajuste, x_name, y_name):
    x = datos['%s'% x_name];ux=datos['u%s'% x_name];y=datos['%s'% y_name]; uy=datos['u%s'% y_name]

    ajuste=curve_fit(func_cuadrat,x,y,sigma=uy,absolute_sigma=True)

    a,b,c = ajuste[0]
    
    sa,sb,sc=np.sqrt(np.diag(ajuste[1]))
    
    sa='%.1E'% Decimal(sa)
    ususa=sa[4:]; ususa=int(ususa)
    a=round(a, 1-ususa)
    
    
    sb='%.1E'% Decimal(sb)
    ususb=sb[4:]; ususb=int(ususb)
    b=round(b, 1-ususb)
    
    sc='%.1E'% Decimal(sc)
    ususc=sc[4:]; ususc=int(ususc)
    c=round(c, 1-ususc)
   

    v_1='a={var} ,\u03C3(a)={inc}'.format(var=a, inc=sa)
    v_2='b={var} ,\u03C3(b)={inc}'.format(var=b, inc=sb)
    v_3='c={var} ,\u03C3(c)={inc}'.format(var=c, inc=sc)
    texto=v_1+'\n'+v_2+'\n'+v_3
    
    #La función ajustada. Ahora t es x.
    y_Ajus=func_cuadrat(x,a,b,c)

    #Ahora graficamos y guardamos
    from matplotlib.font_manager import FontProperties
    font0 = FontProperties();fontt = font0.copy()
    fontt.set_family('serif');fontt.set_size('xx-large');fontt.set_weight('semibold')
    fonta = font0.copy();fonta.set_family('serif');fonta.set_size('xx-large');fonta.set_style('italic')
    
    
    fig, ax =plt.subplots(figsize=(12,6))
    
    ax.plot(x, y_Ajus, color="black", lw=1.00, ls='-')
    ax.errorbar(x, y, fmt='o',markersize=5, yerr=uy, xerr=ux, ecolor='crimson', markerfacecolor='crimson', markeredgecolor='crimson')
    
    ax.set_title('%s'% nombre_ajuste,fontproperties=fontt)
    ax.set_xlabel('%s'% x_name, fontproperties=fonta);ax.set_ylabel('%s'% y_name, fontproperties=fonta)
    plt.savefig("Graficas\\Ajuste %s.png" % nombre_ajuste, bbox_inches='tight')
    
    global menu
    grafica=Toplevel()
    grafica.title('%s'%nombre_ajuste)
    grafica.configure(background='midnight blue')
    grafica.imagen=PhotoImage(file="Graficas\\Ajuste %s.png"% nombre_ajuste)
    from tkinter import font
    grafica.parametros=Label(grafica, text=texto, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.parametros.configure(font=('Courier', 10))
    
    grafica.image=Label(grafica, image=grafica.imagen, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.aceptar=Button(grafica, text='Aceptar', command=grafica.destroy, width=7, bg='midnight blue', fg='lime green',activebackground='navy', activeforeground='snow')
    grafica.ecuacion=Label(grafica, text='y={0}x^2+{1}x+{2}'.format(c,b,a),relief="ridge",borderwidth=6, bg="midnight blue", fg="snow")
    
    grafica.ecuacion.pack(padx=3, pady=3)
    grafica.parametros.pack(side=LEFT,padx=3, pady=3);grafica.image.pack(padx=3, pady=3);grafica.aceptar.pack(padx=3, pady=3)
    grafica.aceptar.focus_set()

    
    
def ajcuad(datos, nombre_ajuste, x_name, y_name):
    x = datos['%s'% x_name];ux=datos['u%s'% x_name];y=datos['%s'% y_name]; uy=datos['u%s'% y_name]

    ajuste=curve_fit(func_cuad,x,y,sigma=uy,absolute_sigma=True)

    a= ajuste[0][0]
    
    sa=np.sqrt(np.diag(ajuste[1]))[0]
    
    sa='%.1E'% Decimal(sa)
    ususa=sa[4:]; ususa=int(ususa)
    a=round(a, 1-ususa)
    
    v_1='a={var} ,\u03C3(a)={inc}'.format(var=a, inc=sa)
    texto=v_1
    
    #La función ajustada. Ahora t es x.
    y_Ajus=func_cuad(x,a)

    #Ahora graficamos y guardamos
    from matplotlib.font_manager import FontProperties
    font0 = FontProperties();fontt = font0.copy()
    fontt.set_family('serif');fontt.set_size('xx-large');fontt.set_weight('semibold')
    fonta = font0.copy();fonta.set_family('serif');fonta.set_size('xx-large');fonta.set_style('italic')
    
    
    fig, ax =plt.subplots(figsize=(12,6))
    
    ax.plot(x, y_Ajus, color="black", lw=1.00, ls='-')
    ax.errorbar(x, y, fmt='o',markersize=5, yerr=uy, xerr=ux, ecolor='crimson', markerfacecolor='crimson', markeredgecolor='crimson')
    
    ax.set_title('%s'% nombre_ajuste,fontproperties=fontt)
    ax.set_xlabel('%s'% x_name, fontproperties=fonta);ax.set_ylabel('%s'% y_name, fontproperties=fonta)
    plt.savefig("Graficas\\Ajuste %s.png" % nombre_ajuste, bbox_inches='tight')
    
    global menu
    grafica=Toplevel()
    grafica.title('%s'%nombre_ajuste)
    grafica.configure(background='midnight blue')
    grafica.imagen=PhotoImage(file="Graficas\\Ajuste %s.png"% nombre_ajuste)
    from tkinter import font
    grafica.parametros=Label(grafica, text=texto, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.parametros.configure(font=('Courier', 10))
    
    grafica.image=Label(grafica, image=grafica.imagen, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.aceptar=Button(grafica, text='Aceptar', command=grafica.destroy, width=7, bg='midnight blue', fg='lime green',activebackground='navy', activeforeground='snow')
    grafica.ecuacion=Label(grafica, text='y={0}x^2'.format(a),relief="ridge",borderwidth=6, bg="midnight blue", fg="snow")
    
    grafica.ecuacion.pack(padx=3, pady=3)
    grafica.parametros.pack(side=LEFT,padx=3, pady=3);grafica.image.pack(padx=3, pady=3);grafica.aceptar.pack(padx=3, pady=3)
    grafica.aceptar.focus_set()
    
    
def ajcuarta(datos, nombre_ajuste, x_name, y_name):
    x = datos['%s'% x_name];ux=datos['u%s'% x_name];y=datos['%s'% y_name]; uy=datos['u%s'% y_name]

    ajuste=curve_fit(func_cuarta,x,y,sigma=uy,absolute_sigma=True)

    a= ajuste[0][0]
    
    sa=np.sqrt(np.diag(ajuste[1]))[0]
    
    sa='%.1E'% Decimal(sa)
    ususa=sa[4:]; ususa=int(ususa)
    a=round(a, 1-ususa)
    
    v_1='a={var} ,\u03C3(a)={inc}'.format(var=a, inc=sa)
    texto=v_1
    
    #La función ajustada. Ahora t es x.
    y_Ajus=func_cuarta(x,a)

    #Ahora graficamos y guardamos
    from matplotlib.font_manager import FontProperties
    font0 = FontProperties();fontt = font0.copy()
    fontt.set_family('serif');fontt.set_size('xx-large');fontt.set_weight('semibold')
    fonta = font0.copy();fonta.set_family('serif');fonta.set_size('xx-large');fonta.set_style('italic')
    
    
    fig, ax =plt.subplots(figsize=(12,6))
    
    ax.plot(x, y_Ajus, color="black", lw=1.00, ls='-')
    ax.errorbar(x, y, fmt='o',markersize=5, yerr=uy, xerr=ux, ecolor='crimson', markerfacecolor='crimson', markeredgecolor='crimson')
    
    ax.set_title('%s'% nombre_ajuste,fontproperties=fontt)
    ax.set_xlabel('%s'% x_name, fontproperties=fonta);ax.set_ylabel('%s'% y_name, fontproperties=fonta)
    plt.savefig("Graficas\\Ajuste %s.png" % nombre_ajuste, bbox_inches='tight')
    
    global menu
    grafica=Toplevel()
    grafica.title('%s'%nombre_ajuste)
    grafica.configure(background='midnight blue')
    grafica.imagen=PhotoImage(file="Graficas\\Ajuste %s.png"% nombre_ajuste)
    from tkinter import font
    grafica.parametros=Label(grafica, text=texto, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.parametros.configure(font=('Courier', 10))
    
    grafica.image=Label(grafica, image=grafica.imagen, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.aceptar=Button(grafica, text='Aceptar', command=grafica.destroy, width=7, bg='midnight blue', fg='lime green',activebackground='navy', activeforeground='snow')
    grafica.ecuacion=Label(grafica, text='y={0}x^4'.format(a),relief="ridge",borderwidth=6, bg="midnight blue", fg="snow")
    
    grafica.ecuacion.pack(padx=3, pady=3)
    grafica.parametros.pack(side=LEFT,padx=3, pady=3);grafica.image.pack(padx=3, pady=3);grafica.aceptar.pack(padx=3, pady=3)
    grafica.aceptar.focus_set()
    
def ajsin(datos, nombre_ajuste, x_name, y_name):
    x = datos['%s'% x_name];ux=datos['u%s'% x_name];y=datos['%s'% y_name]; uy=datos['u%s'% y_name]

    ajuste=curve_fit(func_sin,x,y,sigma=uy,absolute_sigma=True)

    a,b = ajuste[0]
    
    sa,sb=np.sqrt(np.diag(ajuste[1]))
    
    sa='%.1E'% Decimal(sa)
    ususa=sa[4:]; ususa=int(ususa)
    a=round(a, 1-ususa)
    
    
    sb='%.1E'% Decimal(sb)
    ususb=sb[4:]; ususb=int(ususb)
    b=round(b, 1-ususb)

   

    v_1='a={var} ,\u03C3(a)={inc}'.format(var=a, inc=sa)
    v_2='b={var} ,\u03C3(b)={inc}'.format(var=b, inc=sb)
    texto=v_1+'\n'+v_2
    
    #La función ajustada. Ahora t es x.
    y_Ajus=func_sin(x,a,b)

    #Ahora graficamos y guardamos
    from matplotlib.font_manager import FontProperties
    font0 = FontProperties();fontt = font0.copy()
    fontt.set_family('serif');fontt.set_size('xx-large');fontt.set_weight('semibold')
    fonta = font0.copy();fonta.set_family('serif');fonta.set_size('xx-large');fonta.set_style('italic')
    
    
    fig, ax =plt.subplots(figsize=(12,6))
    
    ax.plot(x, y_Ajus, color="black", lw=1.00, ls='-')
    ax.errorbar(x, y, fmt='o',markersize=5, yerr=uy, xerr=ux, ecolor='crimson', markerfacecolor='crimson', markeredgecolor='crimson')
    
    ax.set_title('%s'% nombre_ajuste,fontproperties=fontt)
    ax.set_xlabel('%s'% x_name, fontproperties=fonta);ax.set_ylabel('%s'% y_name, fontproperties=fonta)
    plt.savefig("Graficas\\Ajuste %s.png" % nombre_ajuste, bbox_inches='tight')
    
    global menu
    grafica=Toplevel()
    grafica.title('%s'%nombre_ajuste)
    grafica.configure(background='midnight blue')
    grafica.imagen=PhotoImage(file="Graficas\\Ajuste %s.png"% nombre_ajuste)
    from tkinter import font
    grafica.parametros=Label(grafica, text=texto, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.parametros.configure(font=('Courier', 10))
    
    grafica.image=Label(grafica, image=grafica.imagen, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.aceptar=Button(grafica, text='Aceptar', command=grafica.destroy, width=7, bg='midnight blue', fg='lime green',activebackground='navy', activeforeground='snow')
    grafica.ecuacion=Label(grafica, text='y={0} sin({1}x)'.format(a,b),relief="ridge",borderwidth=6, bg="midnight blue", fg="snow")
    
    grafica.ecuacion.pack(padx=3, pady=3)
    grafica.parametros.pack(side=LEFT,padx=3, pady=3);grafica.image.pack(padx=3, pady=3);grafica.aceptar.pack(padx=3, pady=3)
    grafica.aceptar.focus_set()
    
    
def ajsinc(datos, nombre_ajuste, x_name, y_name):
    x = datos['%s'% x_name];ux=datos['u%s'% x_name];y=datos['%s'% y_name]; uy=datos['u%s'% y_name]

    ajuste=curve_fit(func_sinc,x,y,sigma=uy,absolute_sigma=True)

    a,b,c = ajuste[0]
    
    sa,sb,sc=np.sqrt(np.diag(ajuste[1]))
    
    sa='%.1E'% Decimal(sa)
    ususa=sa[4:]; ususa=int(ususa)
    a=round(a, 1-ususa)
    
    
    sb='%.1E'% Decimal(sb)
    ususb=sb[4:]; ususb=int(ususb)
    b=round(b, 1-ususb)
    
    sc='%.1E'% Decimal(sc)
    ususc=sc[4:]; ususc=int(ususc)
    c=round(c, 1-ususc)
   

    v_1='a={var} ,\u03C3(a)={inc}'.format(var=a, inc=sa)
    v_2='b={var} ,\u03C3(b)={inc}'.format(var=b, inc=sb)
    v_3='c={var} ,\u03C3(c)={inc}'.format(var=c, inc=sc)
    texto=v_1+'\n'+v_2+'\n'+v_3
    
    #La función ajustada. Ahora t es x.
    y_Ajus=func_sinc(x,a,b,c)

    #Ahora graficamos y guardamos
    from matplotlib.font_manager import FontProperties
    font0 = FontProperties();fontt = font0.copy()
    fontt.set_family('serif');fontt.set_size('xx-large');fontt.set_weight('semibold')
    fonta = font0.copy();fonta.set_family('serif');fonta.set_size('xx-large');fonta.set_style('italic')
    
    
    fig, ax =plt.subplots(figsize=(12,6))
    
    ax.plot(x, y_Ajus, color="black", lw=1.00, ls='-')
    ax.errorbar(x, y, fmt='o',markersize=5, yerr=uy, xerr=ux, ecolor='crimson', markerfacecolor='crimson', markeredgecolor='crimson')
    
    ax.set_title('%s'% nombre_ajuste,fontproperties=fontt)
    ax.set_xlabel('%s'% x_name, fontproperties=fonta);ax.set_ylabel('%s'% y_name, fontproperties=fonta)
    plt.savefig("Graficas\\Ajuste %s.png" % nombre_ajuste, bbox_inches='tight')
    
    global menu
    grafica=Toplevel()
    grafica.title('%s'%nombre_ajuste)
    grafica.configure(background='midnight blue')
    grafica.imagen=PhotoImage(file="Graficas\\Ajuste %s.png"% nombre_ajuste)
    from tkinter import font
    grafica.parametros=Label(grafica, text=texto, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.parametros.configure(font=('Courier', 10))
    
    grafica.image=Label(grafica, image=grafica.imagen, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.aceptar=Button(grafica, text='Aceptar', command=grafica.destroy, width=7, bg='midnight blue', fg='lime green',activebackground='navy', activeforeground='snow')
    grafica.ecuacion=Label(grafica, text='y={0} sin({1}x+{2})'.format(a,b,c),relief="ridge",borderwidth=6, bg="midnight blue", fg="snow")
    
    grafica.ecuacion.pack(padx=3, pady=3)
    grafica.parametros.pack(side=LEFT,padx=3, pady=3);grafica.image.pack(padx=3, pady=3);grafica.aceptar.pack(padx=3, pady=3)
    grafica.aceptar.focus_set()
    
    
def ajcos(datos, nombre_ajuste, x_name, y_name):
    x = datos['%s'% x_name];ux=datos['u%s'% x_name];y=datos['%s'% y_name]; uy=datos['u%s'% y_name]

    ajuste=curve_fit(func_cos,x,y,sigma=uy,absolute_sigma=True)

    a,b = ajuste[0]
    
    sa,sb=np.sqrt(np.diag(ajuste[1]))
    
    sa='%.1E'% Decimal(sa)
    ususa=sa[4:]; ususa=int(ususa)
    a=round(a, 1-ususa)
    
    
    sb='%.1E'% Decimal(sb)
    ususb=sb[4:]; ususb=int(ususb)
    b=round(b, 1-ususb)

   

    v_1='a={var} ,\u03C3(a)={inc}'.format(var=a, inc=sa)
    v_2='b={var} ,\u03C3(b)={inc}'.format(var=b, inc=sb)
    texto=v_1+'\n'+v_2
    
    #La función ajustada. Ahora t es x.
    y_Ajus=func_cos(x,a,b)

    #Ahora graficamos y guardamos
    from matplotlib.font_manager import FontProperties
    font0 = FontProperties();fontt = font0.copy()
    fontt.set_family('serif');fontt.set_size('xx-large');fontt.set_weight('semibold')
    fonta = font0.copy();fonta.set_family('serif');fonta.set_size('xx-large');fonta.set_style('italic')
    
    
    fig, ax =plt.subplots(figsize=(12,6))
    
    ax.plot(x, y_Ajus, color="black", lw=1.00, ls='-')
    ax.errorbar(x, y, fmt='o',markersize=5, yerr=uy, xerr=ux, ecolor='crimson', markerfacecolor='crimson', markeredgecolor='crimson')
    
    ax.set_title('%s'% nombre_ajuste,fontproperties=fontt)
    ax.set_xlabel('%s'% x_name, fontproperties=fonta);ax.set_ylabel('%s'% y_name, fontproperties=fonta)
    plt.savefig("Graficas\\Ajuste %s.png" % nombre_ajuste, bbox_inches='tight')
    
    global menu
    grafica=Toplevel()
    grafica.title('%s'%nombre_ajuste)
    grafica.configure(background='midnight blue')
    grafica.imagen=PhotoImage(file="Graficas\\Ajuste %s.png"% nombre_ajuste)
    from tkinter import font
    grafica.parametros=Label(grafica, text=texto, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.parametros.configure(font=('Courier', 10))
    
    grafica.image=Label(grafica, image=grafica.imagen, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.aceptar=Button(grafica, text='Aceptar', command=grafica.destroy, width=7, bg='midnight blue', fg='lime green',activebackground='navy', activeforeground='snow')
    grafica.ecuacion=Label(grafica, text='y={0} cos({1}x)'.format(a,b),relief="ridge",borderwidth=6, bg="midnight blue", fg="snow")
    
    grafica.ecuacion.pack(padx=3, pady=3)
    grafica.parametros.pack(side=LEFT,padx=3, pady=3);grafica.image.pack(padx=3, pady=3);grafica.aceptar.pack(padx=3, pady=3)
    grafica.aceptar.focus_set()
    
    
def ajcosc(datos, nombre_ajuste, x_name, y_name):
    x = datos['%s'% x_name];ux=datos['u%s'% x_name];y=datos['%s'% y_name]; uy=datos['u%s'% y_name]

    ajuste=curve_fit(func_cosc,x,y,sigma=uy,absolute_sigma=True)

    a,b,c = ajuste[0]
    
    sa,sb,sc=np.sqrt(np.diag(ajuste[1]))
    
    sa='%.1E'% Decimal(sa)
    ususa=sa[4:]; ususa=int(ususa)
    a=round(a, 1-ususa)
    
    
    sb='%.1E'% Decimal(sb)
    ususb=sb[4:]; ususb=int(ususb)
    b=round(b, 1-ususb)
    
    sc='%.1E'% Decimal(sc)
    ususc=sc[4:]; ususc=int(ususc)
    c=round(c, 1-ususc)
   

    v_1='a={var} ,\u03C3(a)={inc}'.format(var=a, inc=sa)
    v_2='b={var} ,\u03C3(b)={inc}'.format(var=b, inc=sb)
    v_3='c={var} ,\u03C3(c)={inc}'.format(var=c, inc=sc)
    texto=v_1+'\n'+v_2+'\n'+v_3
    
    #La función ajustada. Ahora t es x.
    y_Ajus=func_cosc(x,a,b,c)

    #Ahora graficamos y guardamos
    from matplotlib.font_manager import FontProperties
    font0 = FontProperties();fontt = font0.copy()
    fontt.set_family('serif');fontt.set_size('xx-large');fontt.set_weight('semibold')
    fonta = font0.copy();fonta.set_family('serif');fonta.set_size('xx-large');fonta.set_style('italic')
    
    
    fig, ax =plt.subplots(figsize=(12,6))
    
    ax.plot(x, y_Ajus, color="black", lw=1.00, ls='-')
    ax.errorbar(x, y, fmt='o',markersize=5, yerr=uy, xerr=ux, ecolor='crimson', markerfacecolor='crimson', markeredgecolor='crimson')
    
    ax.set_title('%s'% nombre_ajuste,fontproperties=fontt)
    ax.set_xlabel('%s'% x_name, fontproperties=fonta);ax.set_ylabel('%s'% y_name, fontproperties=fonta)
    plt.savefig("Graficas\\Ajuste %s.png" % nombre_ajuste, bbox_inches='tight')
    
    global menu
    grafica=Toplevel()
    grafica.title('%s'%nombre_ajuste)
    grafica.configure(background='midnight blue')
    grafica.imagen=PhotoImage(file="Graficas\\Ajuste %s.png"% nombre_ajuste)
    from tkinter import font
    grafica.parametros=Label(grafica, text=texto, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.parametros.configure(font=('Courier', 10))
    
    grafica.image=Label(grafica, image=grafica.imagen, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.aceptar=Button(grafica, text='Aceptar', command=grafica.destroy, width=7, bg='midnight blue', fg='lime green',activebackground='navy', activeforeground='snow')
    grafica.ecuacion=Label(grafica, text='y={0} cos({1}x+{2})'.format(a,b,c),relief="ridge",borderwidth=6, bg="midnight blue", fg="snow")
    
    grafica.ecuacion.pack(padx=3, pady=3)
    grafica.parametros.pack(side=LEFT,padx=3, pady=3);grafica.image.pack(padx=3, pady=3);grafica.aceptar.pack(padx=3, pady=3)
    grafica.aceptar.focus_set()

def ajsinh(datos, nombre_ajuste, x_name, y_name):
    x = datos['%s'% x_name];ux=datos['u%s'% x_name];y=datos['%s'% y_name]; uy=datos['u%s'% y_name]

    ajuste=curve_fit(func_sinh,x,y,sigma=uy,absolute_sigma=True)

    a,b = ajuste[0]
    
    sa,sb=np.sqrt(np.diag(ajuste[1]))
    
    sa='%.1E'% Decimal(sa)
    ususa=sa[4:]; ususa=int(ususa)
    a=round(a, 1-ususa)
    
    
    sb='%.1E'% Decimal(sb)
    ususb=sb[4:]; ususb=int(ususb)
    b=round(b, 1-ususb)

   

    v_1='a={var} ,\u03C3(a)={inc}'.format(var=a, inc=sa)
    v_2='b={var} ,\u03C3(b)={inc}'.format(var=b, inc=sb)
    texto=v_1+'\n'+v_2
    
    #La función ajustada. Ahora t es x.
    y_Ajus=func_sinh(x,a,b)

    #Ahora graficamos y guardamos
    from matplotlib.font_manager import FontProperties
    font0 = FontProperties();fontt = font0.copy()
    fontt.set_family('serif');fontt.set_size('xx-large');fontt.set_weight('semibold')
    fonta = font0.copy();fonta.set_family('serif');fonta.set_size('xx-large');fonta.set_style('italic')
    
    
    fig, ax =plt.subplots(figsize=(12,6))
    
    ax.plot(x, y_Ajus, color="black", lw=1.00, ls='-')
    ax.errorbar(x, y, fmt='o',markersize=5, yerr=uy, xerr=ux, ecolor='crimson', markerfacecolor='crimson', markeredgecolor='crimson')
    
    ax.set_title('%s'% nombre_ajuste,fontproperties=fontt)
    ax.set_xlabel('%s'% x_name, fontproperties=fonta);ax.set_ylabel('%s'% y_name, fontproperties=fonta)
    plt.savefig("Graficas\\Ajuste %s.png" % nombre_ajuste, bbox_inches='tight')
    
    global menu
    grafica=Toplevel()
    grafica.title('%s'%nombre_ajuste)
    grafica.configure(background='midnight blue')
    grafica.imagen=PhotoImage(file="Graficas\\Ajuste %s.png"% nombre_ajuste)
    from tkinter import font
    grafica.parametros=Label(grafica, text=texto, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.parametros.configure(font=('Courier', 10))
    
    grafica.image=Label(grafica, image=grafica.imagen, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.aceptar=Button(grafica, text='Aceptar', command=grafica.destroy, width=7, bg='midnight blue', fg='lime green',activebackground='navy', activeforeground='snow')
    grafica.ecuacion=Label(grafica, text='y={0} sinh({1}x)'.format(a,b),relief="ridge",borderwidth=6, bg="midnight blue", fg="snow")
    
    grafica.ecuacion.pack(padx=3, pady=3)
    grafica.parametros.pack(side=LEFT,padx=3, pady=3);grafica.image.pack(padx=3, pady=3);grafica.aceptar.pack(padx=3, pady=3)
    grafica.aceptar.focus_set()
    
def ajcosh(datos, nombre_ajuste, x_name, y_name):
    x = datos['%s'% x_name];ux=datos['u%s'% x_name];y=datos['%s'% y_name]; uy=datos['u%s'% y_name]

    ajuste=curve_fit(func_cosh,x,y,sigma=uy,absolute_sigma=True)

    a,b = ajuste[0]
    
    sa,sb=np.sqrt(np.diag(ajuste[1]))
    
    sa='%.1E'% Decimal(sa)
    ususa=sa[4:]; ususa=int(ususa)
    a=round(a, 1-ususa)
    
    
    sb='%.1E'% Decimal(sb)
    ususb=sb[4:]; ususb=int(ususb)
    b=round(b, 1-ususb)

   

    v_1='a={var} ,\u03C3(a)={inc}'.format(var=a, inc=sa)
    v_2='b={var} ,\u03C3(b)={inc}'.format(var=b, inc=sb)
    texto=v_1+'\n'+v_2
    
    #La función ajustada. Ahora t es x.
    y_Ajus=func_cosh(x,a,b)

    #Ahora graficamos y guardamos
    from matplotlib.font_manager import FontProperties
    font0 = FontProperties();fontt = font0.copy()
    fontt.set_family('serif');fontt.set_size('xx-large');fontt.set_weight('semibold')
    fonta = font0.copy();fonta.set_family('serif');fonta.set_size('xx-large');fonta.set_style('italic')
    
    
    fig, ax =plt.subplots(figsize=(12,6))
    
    ax.plot(x, y_Ajus, color="black", lw=1.00, ls='-')
    ax.errorbar(x, y, fmt='o',markersize=5, yerr=uy, xerr=ux, ecolor='crimson', markerfacecolor='crimson', markeredgecolor='crimson')
    
    ax.set_title('%s'% nombre_ajuste,fontproperties=fontt)
    ax.set_xlabel('%s'% x_name, fontproperties=fonta);ax.set_ylabel('%s'% y_name, fontproperties=fonta)
    plt.savefig("Graficas\\Ajuste %s.png" % nombre_ajuste, bbox_inches='tight')
    
    global menu
    grafica=Toplevel()
    grafica.title('%s'%nombre_ajuste)
    grafica.configure(background='midnight blue')
    grafica.imagen=PhotoImage(file="Graficas\\Ajuste %s.png"% nombre_ajuste)
    from tkinter import font
    grafica.parametros=Label(grafica, text=texto, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.parametros.configure(font=('Courier', 10))
    
    grafica.image=Label(grafica, image=grafica.imagen, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.aceptar=Button(grafica, text='Aceptar', command=grafica.destroy, width=7, bg='midnight blue', fg='lime green',activebackground='navy', activeforeground='snow')
    grafica.ecuacion=Label(grafica, text='y={0} cosh({1}x)'.format(a,b),relief="ridge",borderwidth=6, bg="midnight blue", fg="snow")
    
    grafica.ecuacion.pack(padx=3, pady=3)
    grafica.parametros.pack(side=LEFT, padx=3, pady=3);grafica.image.pack(padx=3, pady=3);grafica.aceptar.pack(padx=3, pady=3)
    grafica.aceptar.focus_set()
    
def ajln(datos, nombre_ajuste, x_name, y_name):
    x = datos['%s'% x_name];ux=datos['u%s'% x_name];y=datos['%s'% y_name]; uy=datos['u%s'% y_name]

    ajuste=curve_fit(func_ln,x,y,sigma=uy,absolute_sigma=True)

    a = ajuste[0][0]
    
    sa=np.sqrt(np.diag(ajuste[1]))[0]
    
    sa='%.1E'% Decimal(sa)
    ususa=sa[4:]; ususa=int(ususa)
    a=round(a, 1-ususa)


   

    v_1='a={var} ,\u03C3(a)={inc}'.format(var=a, inc=sa)
    texto=v_1
    
    #La función ajustada. Ahora t es x.
    y_Ajus=func_ln(x,a)

    #Ahora graficamos y guardamos
    from matplotlib.font_manager import FontProperties
    font0 = FontProperties();fontt = font0.copy()
    fontt.set_family('serif');fontt.set_size('xx-large');fontt.set_weight('semibold')
    fonta = font0.copy();fonta.set_family('serif');fonta.set_size('xx-large');fonta.set_style('italic')
    
    
    fig, ax =plt.subplots(figsize=(12,6))
    
    ax.plot(x, y_Ajus, color="black", lw=1.00, ls='-')
    ax.errorbar(x, y, fmt='o',markersize=5, yerr=uy, xerr=ux, ecolor='crimson', markerfacecolor='crimson', markeredgecolor='crimson')
    
    ax.set_title('%s'% nombre_ajuste,fontproperties=fontt)
    ax.set_xlabel('%s'% x_name, fontproperties=fonta);ax.set_ylabel('%s'% y_name, fontproperties=fonta)
    plt.savefig("Graficas\\Ajuste %s.png" % nombre_ajuste, bbox_inches='tight')
    
    global menu
    grafica=Toplevel()
    grafica.title('%s'%nombre_ajuste)
    grafica.configure(background='midnight blue')
    grafica.imagen=PhotoImage(file="Graficas\\Ajuste %s.png"% nombre_ajuste)
    from tkinter import font
    grafica.parametros=Label(grafica, text=texto, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.parametros.configure(font=('Courier', 10))
    
    grafica.image=Label(grafica, image=grafica.imagen, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.aceptar=Button(grafica, text='Aceptar', command=grafica.destroy, width=7, bg='midnight blue', fg='lime green',activebackground='navy', activeforeground='snow')
    grafica.ecuacion=Label(grafica, text='y={0} ln(x)'.format(a),relief="ridge",borderwidth=6, bg="midnight blue", fg="snow")
    
    grafica.ecuacion.pack(padx=3, pady=3)
    grafica.parametros.pack(side=LEFT,padx=3, pady=3);grafica.image.pack(padx=3, pady=3);grafica.aceptar.pack(padx=3, pady=3)
    grafica.aceptar.focus_set()

    
    
def ajinv(datos, nombre_ajuste, x_name, y_name):
    x = datos['%s'% x_name];ux=datos['u%s'% x_name];y=datos['%s'% y_name]; uy=datos['u%s'% y_name]

    ajuste=curve_fit(func_inv,x,y,sigma=uy,absolute_sigma=True)

    a = ajuste[0][0]
    
    sa=np.sqrt(np.diag(ajuste[1]))[0]
    
    sa='%.1E'% Decimal(sa)
    ususa=sa[4:]; ususa=int(ususa)
    a=round(a, 1-ususa)


   

    v_1='a={var} ,\u03C3(a)={inc}'.format(var=a, inc=sa)
    texto=v_1
    
    #La función ajustada. Ahora t es x.
    y_Ajus=func_inv(x,a)

    #Ahora graficamos y guardamos
    from matplotlib.font_manager import FontProperties
    font0 = FontProperties();fontt = font0.copy()
    fontt.set_family('serif');fontt.set_size('xx-large');fontt.set_weight('semibold')
    fonta = font0.copy();fonta.set_family('serif');fonta.set_size('xx-large');fonta.set_style('italic')
    
    
    fig, ax =plt.subplots(figsize=(12,6))
    
    ax.plot(x, y_Ajus, color="black", lw=1.00, ls='-')
    ax.errorbar(x, y, fmt='o',markersize=5, yerr=uy, xerr=ux, ecolor='crimson', markerfacecolor='crimson', markeredgecolor='crimson')
    
    ax.set_title('%s'% nombre_ajuste,fontproperties=fontt)
    ax.set_xlabel('%s'% x_name, fontproperties=fonta);ax.set_ylabel('%s'% y_name, fontproperties=fonta)
    plt.savefig("Graficas\\Ajuste %s.png" % nombre_ajuste, bbox_inches='tight')
    
    global menu
    grafica=Toplevel()
    grafica.title('%s'%nombre_ajuste)
    grafica.configure(background='midnight blue')
    grafica.imagen=PhotoImage(file="Graficas\\Ajuste %s.png"% nombre_ajuste)
    from tkinter import font
    grafica.parametros=Label(grafica, text=texto, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.parametros.configure(font=('Courier', 10))
    
    grafica.image=Label(grafica, image=grafica.imagen, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.aceptar=Button(grafica, text='Aceptar', command=grafica.destroy, width=7, bg='midnight blue', fg='lime green',activebackground='navy', activeforeground='snow')
    grafica.ecuacion=Label(grafica, text='y={0}/x'.format(a),relief="ridge",borderwidth=6, bg="midnight blue", fg="snow")
    
    grafica.ecuacion.pack(padx=3, pady=3)
    grafica.parametros.pack(side=LEFT, padx=3, pady=3);grafica.image.pack(padx=3, pady=3);grafica.aceptar.pack(padx=3, pady=3)
    grafica.aceptar.focus_set()
    
def ajinvcuad(datos, nombre_ajuste, x_name, y_name):
    x = datos['%s'% x_name];ux=datos['u%s'% x_name];y=datos['%s'% y_name]; uy=datos['u%s'% y_name]

    ajuste=curve_fit(func_invcuad,x,y,sigma=uy,absolute_sigma=True)

    a = ajuste[0][0]
    
    sa=np.sqrt(np.diag(ajuste[1]))[0]
    
    sa='%.1E'% Decimal(sa)
    ususa=sa[4:]; ususa=int(ususa)
    a=round(a, 1-ususa)


   

    v_1='a={var} ,\u03C3(a)={inc}'.format(var=a, inc=sa)
    texto=v_1
    
    #La función ajustada. Ahora t es x.
    y_Ajus=func_invcuad(x,a)

    #Ahora graficamos y guardamos
    from matplotlib.font_manager import FontProperties
    font0 = FontProperties();fontt = font0.copy()
    fontt.set_family('serif');fontt.set_size('xx-large');fontt.set_weight('semibold')
    fonta = font0.copy();fonta.set_family('serif');fonta.set_size('xx-large');fonta.set_style('italic')
    
    
    fig, ax =plt.subplots(figsize=(12,6))
    
    ax.plot(x, y_Ajus, color="black", lw=1.00, ls='-')
    ax.errorbar(x, y, fmt='o',markersize=5, yerr=uy, xerr=ux, ecolor='crimson', markerfacecolor='crimson', markeredgecolor='crimson')
    
    ax.set_title('%s'% nombre_ajuste,fontproperties=fontt)
    ax.set_xlabel('%s'% x_name, fontproperties=fonta);ax.set_ylabel('%s'% y_name, fontproperties=fonta)
    plt.savefig("Graficas\\Ajuste %s.png" % nombre_ajuste, bbox_inches='tight')
    
    global menu
    grafica=Toplevel()
    grafica.title('%s'%nombre_ajuste)
    grafica.configure(background='midnight blue')
    grafica.imagen=PhotoImage(file="Graficas\\Ajuste %s.png"% nombre_ajuste)
    from tkinter import font
    grafica.parametros=Label(grafica, text=texto, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.parametros.configure(font=('Courier', 10))
    
    grafica.image=Label(grafica, image=grafica.imagen, relief='ridge',borderwidth=6, bg='midnight blue', fg='snow')
    grafica.aceptar=Button(grafica, text='Aceptar', command=grafica.destroy, width=7, bg='midnight blue', fg='lime green',activebackground='navy', activeforeground='snow')
    grafica.ecuacion=Label(grafica, text='y={0}/x^2'.format(a),relief="ridge",borderwidth=6, bg="midnight blue", fg="snow")
    
    grafica.ecuacion.pack(padx=3, pady=3)
    grafica.parametros.pack(side=LEFT, padx=3, pady=3);grafica.image.pack(padx=3, pady=3);grafica.aceptar.pack(padx=3, pady=3)
    grafica.aceptar.focus_set()
