#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Alejandro Mata Ali (DOKOS TAYOS)"
__copyright__ = "Public content for science use"
__credits__ = ["Alejandro Mata Ali"]
__version__ = "0.0.1"
__maintainer__ = "Alejandro Mata Ali (DOKOS TAYOS)"
__email__ = "alejandro.mata.ali@gmail.com"
__status__ = "Prototype"

import pandas as pd

from tkinter import *
from tkinter import messagebox

import re
from os import scandir, getcwd
from sys import modules

def documento_csv(nombre):
    #datos será nuestro archivo de uso, con los datos de nombre, sustituyendo todos los 'no' por NaN values.
    datos=pd.read_csv(nombre, na_values=['no'])
    return datos

def documento_excel(nombre):
    #Obtenemos los datos del excel xlsx
    datos=pd.read_excel(nombre)
    return datos

def llamada_datos():
    global menu
    #Lista de archivos en la carpeta
    ruta = getcwd(); archivos=[arch.name for arch in scandir(ruta+'/Datos') if arch.is_file()]

    #Diferenciamos los diferentes tipos de archivos en listas separadas.
    patroncsv=r'.*\.csv$'; patronxls=r'.*\.xls$'; patronxlsx=r'.*\.xlsx$'
    csv=[];xls=[];xlsx=[]
    for archivo in archivos:
        if re.match(patroncsv, archivo):
            csv.append(archivo[:-4])
        elif re.match(patronxls, archivo):
            xls.append(archivo[:-4])
        elif re.match(patronxlsx, archivo):
            xlsx.append(archivo[:-5])

    #Cuadro para pedir al usuario el tipo del archivo de datos
    call_dat1=Toplevel()
    call_dat1.title('Datos')
    call_dat1.configure(background='midnight blue')
    call_dat1.tipo=StringVar()
    call_dat1.nomm=Label(call_dat1, text='Tipo de archivo: ', bg="midnight blue", fg="snow", width=25, height=2)
    call_dat1.nom=Spinbox(call_dat1, textvariable=call_dat1.tipo, values=('xlsx','xls','csv','Salir'), wrap=True, state='readonly',fg="midnight blue", width=20)
    call_dat1.aceptar=Button(call_dat1, text='Aceptar', command=call_dat1.destroy, width=12, bg="midnight blue", fg="lime green",activebackground="navy", activeforeground="snow")

    call_dat1.nomm.pack();call_dat1.nom.pack()
    call_dat1.aceptar.pack()

    call_dat1.nom.focus_set()
    menu.wait_window(call_dat1)

    tipo=call_dat1.tipo.get()

    if tipo!='Salir' and tipo!='':
        #Escogemos el archivo de este tipo de datos
        call_dat=Toplevel()
        call_dat.title('Datos')
        call_dat.arch=StringVar()
        call_dat.configure(background='midnight blue')
        call_dat.nomm=Label(call_dat, text='Nombre del archivo: ', bg="midnight blue", fg="snow", width=30, height=2)

        if tipo=='csv':
            call_dat.vistas=csv
        elif tipo=='xls':
            call_dat.vistas=xls
        elif tipo=='xlsx':
            call_dat.vistas=xlsx
        call_dat.nom=Spinbox(call_dat, textvariable=call_dat.arch, values=call_dat.vistas, wrap=True, state='readonly',fg="midnight blue", width=25)
        call_dat.nomm.pack()
        call_dat.aceptar=Button(call_dat, text='Aceptar', command=call_dat.destroy, width=15, height=2, bg="midnight blue", fg="lime green",activebackground="navy", activeforeground="snow")
        call_dat.nom.pack()
        call_dat.aceptar.pack()
        
        call_dat.nom.focus_set()
        menu.wait_window(call_dat)

        nombre=call_dat.arch.get()

        #Escogemos la función a usar en función del tipo de archivo que tengamos
        if tipo=='csv':
            nombre='Datos/'+nombre+'.'+tipo
            datos=documento_csv(nombre)
        elif tipo=='xls':
            nombre='Datos/'+nombre+'.'+tipo
            datos=documento_excel(nombre)
        elif tipo=='xlsx':
            nombre='Datos/'+nombre+'.'+tipo
            datos=documento_excel(nombre)

        #Ahora, preguntaremos al usuario qué variables quiere usar para el ajuste
        nombre_variables=list(datos)

        call_var=Toplevel()
        call_var.title('Datos')
        call_var.configure(background='midnight blue')
        call_var.vari=StringVar();call_var.x_name=StringVar();call_var.y_name=StringVar();call_var.graf_name=StringVar()

        call_var.nomm=Label(call_var, text='Nombre de las variables: ', bg="midnight blue", fg="snow", width=40, height=2)
        call_var.nommx=Label(call_var, text='Nombre de la variable independiente (x): ', bg="midnight blue", fg="snow", width=40, height=2)
        call_var.x_nom=Spinbox(call_var, textvariable=call_var.x_name, values=nombre_variables, wrap=True, state='readonly', width=30)
        call_var.nommy=Label(call_var, text='Nombre de la variable dependiente (y): ', bg="midnight blue", fg="snow", width=40, height=2)
        call_var.y_nom=Spinbox(call_var, textvariable=call_var.y_name, values=nombre_variables, wrap=True, state='readonly', width=30,fg="midnight blue")
        call_var.aceptar=Button(call_var, text='Aceptar', command=call_var.destroy, width=15, height=2, bg="midnight blue", fg="lime green",activebackground="navy", activeforeground="snow")
        call_var.nommgra=Label(call_var, text='Nombre de la gráfica: ', bg="midnight blue", fg="snow", height=2)
        call_var.graf_nom=Entry(call_var, textvariable=call_var.graf_name,  bg="midnight blue", fg="snow", width=30)

        call_var.nommgra.pack();call_var.graf_nom.pack()
        call_var.nomm.pack()
        call_var.nommx.pack();call_var.x_nom.pack()
        call_var.nommy.pack();call_var.y_nom.pack()
        call_var.aceptar.pack()

        call_var.x_nom.focus_set()
        menu.wait_window(call_var)

        xname=call_var.x_name.get();yname=call_var.y_name.get();grafname=call_var.graf_name.get()

    else:
        nombre=''; xname=''; yname=''; datos=''; grafname=''
    return datos, xname, yname, grafname, nombre, tipo

def mirar_datos():
    global menu
    #Lista de archivos en la carpeta
    ruta = getcwd(); archivos=[arch.name for arch in scandir(ruta+'/Datos') if arch.is_file()]

    #Diferenciamos los diferentes tipos de archivos en listas separadas.
    patroncsv=r'.*\.csv$'; patronxls=r'.*\.xls$'; patronxlsx=r'.*\.xlsx$'
    csv=[];xls=[];xlsx=[]
    for archivo in archivos:
        if re.match(patroncsv, archivo):
            csv.append(archivo[:-4])
        elif re.match(patronxls, archivo):
            xls.append(archivo[:-4])
        elif re.match(patronxlsx, archivo):
            xlsx.append(archivo[:-5])
    #Cuadro para pedir al usuario el tipo del archivo de datos
    call_dat1=Toplevel()
    call_dat1.title('Datos')
    call_dat1.configure(background='midnight blue')
    call_dat1.tipo=StringVar()
    call_dat1.nomm=Label(call_dat1, text='Tipo de archivo: ', bg="midnight blue", fg="snow")
    call_dat1.nom=Spinbox(call_dat1, textvariable=call_dat1.tipo, values=('xlsx','xls','csv','Salir'), wrap=True, state='readonly', width=6,fg="midnight blue")
    call_dat1.aceptar=Button(call_dat1, text='Aceptar', command=call_dat1.destroy, width=7, bg="midnight blue", fg="lime green",activebackground="navy", activeforeground="snow")

    call_dat1.nomm.pack();call_dat1.nom.pack()
    call_dat1.aceptar.pack()

    call_dat1.nom.focus_set()
    menu.wait_window(call_dat1)

    tipo=call_dat1.tipo.get()

    if tipo!='Salir' and tipo!='':
        #Escogemos el archivo de este tipo de datos
        call_dat=Toplevel()
        call_dat.title('Datos')
        call_dat.configure(background='midnight blue')
        call_dat.arch=StringVar()

        call_dat.nomm=Label(call_dat, text='Nombre del archivo: ', bg="midnight blue", fg="snow")

        if tipo=='csv':
            call_dat.vistas=csv
        elif tipo=='xls':
            call_dat.vistas=xls
        elif tipo=='xlsx':
            call_dat.vistas=xlsx
        call_dat.nom=Spinbox(call_dat, textvariable=call_dat.arch, values=call_dat.vistas, wrap=True, state='readonly', width=20,fg="midnight blue")
        call_dat.nom.pack()
        call_dat.aceptar=Button(call_dat, text='Aceptar', command=call_dat.destroy, width=7, bg="midnight blue", fg="lime green",activebackground="navy", activeforeground="snow")
        call_dat.nomm.pack()
        call_dat.aceptar.pack()
        call_dat.nom.focus_set()
        menu.wait_window(call_dat)

        nombre=call_dat.arch.get()

        #Escogemos la función a usar en función del tipo de archivo que tengamos
        if tipo=='csv':
            nombre='Datos/'+nombre+'.'+tipo
            datos=documento_csv(nombre)
        elif tipo=='xls':
            nombre='Datos/'+nombre+'.'+tipo
            datos=documento_excel(nombre)
        elif tipo=='xlsx':
            nombre='Datos/'+nombre+'.'+tipo
            datos=documento_excel(nombre)
        ensenar_datos(datos)

def ensenar_datos(datos):
    global menu
    mirardatos=Toplevel()
    mirardatos.title('Datos')
    mirardatos.configure(background='midnight blue')
    mirardatos.info=Label(mirardatos, text=datos, bg="midnight blue", fg="SeaGreen1")
    mirardatos.aceptar=Button(mirardatos, text='Aceptar', command=mirardatos.destroy, width=10, bg="midnight blue", fg="lime green",activebackground="navy", activeforeground="snow")
    mirardatos.info.pack();mirardatos.aceptar.pack()

    mirardatos.aceptar.focus_set()
    menu.wait_window(mirardatos)

def llamada_ecuacion():
    global menu
    global ecuacion
    global ecuacioner

    #Eliminamos la posible información anterior sobre la ecuación
    ecuacion=''
    #Preguntamos al usuario qué tipo de ecuación quiere
    ecuacioner=Toplevel()
    ecuacioner.title('Ecuación de ajuste')
    ecuacioner.configure(background='midnight blue')

    ecuacioner.mensaje=Label(ecuacioner, text='Seleccione la ecuación que desea: ', bg="midnight blue", fg="snow", width=35, height=2)
    ecuacioner.linealn=Button(ecuacioner,text='y=mx+n', command=transitor_1, width=35, bg="midnight blue", fg="gold2",activebackground="navy", activeforeground="snow", height=2)
    ecuacioner.lineal=Button(ecuacioner,text='y=mx', command=transitor_2, width=35, bg="midnight blue", fg="gold2",activebackground="navy", activeforeground="snow", height=2)
    ecuacioner.cuadrat=Button(ecuacioner,text='y=cx^2+bx+a', command=transitor_3, width=35, bg="midnight blue", fg="gold2",activebackground="navy", activeforeground="snow", height=2)
    ecuacioner.cuad=Button(ecuacioner,text='y=ax^2', command=transitor_4, width=35, bg="midnight blue", fg="gold2",activebackground="navy", activeforeground="snow", height=2)
    ecuacioner.cuarta=Button(ecuacioner,text='y=ax^4', command=transitor_5, width=35, bg="midnight blue", fg="gold2",activebackground="navy", activeforeground="snow")
    ecuacioner.sin=Button(ecuacioner,text='y=a sin(bx)', command=transitor_6, width=35, bg="midnight blue", fg="gold2",activebackground="navy", activeforeground="snow")
    ecuacioner.sinc=Button(ecuacioner,text='y=a sin(bx+c)', command=transitor_7, width=35, bg="midnight blue", fg="gold2",activebackground="navy", activeforeground="snow")
    ecuacioner.cos=Button(ecuacioner,text='y=a cos(bx)', command=transitor_8, width=35, bg="midnight blue", fg="gold2",activebackground="navy", activeforeground="snow")
    ecuacioner.cosc=Button(ecuacioner,text='y=a cos(bx+c)', command=transitor_9, width=35, bg="midnight blue", fg="gold2",activebackground="navy", activeforeground="snow")
    ecuacioner.sinh=Button(ecuacioner,text='y=a sinh(bx)', command=transitor_10, width=35, bg="midnight blue", fg="gold2",activebackground="navy", activeforeground="snow")
    ecuacioner.cosh=Button(ecuacioner,text='y=a cosh(bx)', command=transitor_11, width=35, bg="midnight blue", fg="gold2",activebackground="navy", activeforeground="snow")
    ecuacioner.ln=Button(ecuacioner,text='y=a ln(x)', command=transitor_12, width=35, bg="midnight blue", fg="gold2",activebackground="navy", activeforeground="snow")
    ecuacioner.inv=Button(ecuacioner,text='y=a/x', command=transitor_13, width=35, bg="midnight blue", fg="gold2",activebackground="navy", activeforeground="snow")
    ecuacioner.invcuad=Button(ecuacioner,text='y=a/x^2', command=transitor_14, width=35, bg="midnight blue", fg="gold2",activebackground="navy", activeforeground="snow")
    ecuacioner.custom=Button(ecuacioner,text='Personalizada', command=equation_custom, width=35, bg="midnight blue", fg="gold2",activebackground="navy", activeforeground="snow", height=2)
    ecuacioner.aceptar=Button(ecuacioner, text='Salir', command=transitor_0, width=25, bg="midnight blue", fg="red2",activebackground="navy", activeforeground="snow")

    ecuacioner.mensaje.pack()
    ecuacioner.linealn.pack();ecuacioner.lineal.pack();ecuacioner.ln.pack()
    ecuacioner.cuadrat.pack();ecuacioner.cuad.pack();ecuacioner.cuarta.pack()
    ecuacioner.sin.pack();ecuacioner.sinc.pack();ecuacioner.sinh.pack()
    ecuacioner.cos.pack();ecuacioner.cosc.pack();ecuacioner.cosh.pack()
    ecuacioner.inv.pack();ecuacioner.invcuad.pack()
    ecuacioner.custom.pack()
    ecuacioner.aceptar.pack()

    ecuacioner.linealn.focus_set()
    menu.wait_window(ecuacioner)

def transitor_0():
    equation('Salir')

def transitor_1():
    global menu
    equation('linealn')

def transitor_2():
    equation('lineal')

def transitor_3():
    equation('cuadrat')

def transitor_4():
    equation('cuad')

def transitor_5():
    equation('cuarta')

def transitor_6():
    equation('sin')

def transitor_7():
    equation('sinc')

def transitor_8():
    equation('cos')

def transitor_9():
    equation('cosc')

def transitor_10():
    equation('sinh')

def transitor_11():
    equation('cosh')

def transitor_12():
    equation('ln')

def transitor_13():
    equation('inv')

def transitor_14():
    equation('invcuad')

def equation(nombre):
    global ecuacioner
    global ecuacion
    global ajustador
    ecuacioner.destroy()
    ecuacion=nombre
    if nombre!='Salir':
        #Extraemos la información de los ajustadores
        if nombre=='linealn':
            #Importamos la función
            from ajustadores import ajlinealn
            ajustador=ajlinealn
        elif nombre=='lineal':
            from ajustadores import ajlineal
            ajustador=ajlineal
        elif nombre=='ln':
            from ajustadores import ajln
            ajustador=ajln
        elif nombre=='cuadrat':
            from ajustadores import ajcuadrat
            ajustador=ajcuadrat
        elif nombre=='cuad':
            from ajustadores import ajcuad
            ajustador=ajcuad
        elif nombre=='cuarta':
            from ajustadores import ajcuarta
            ajustador=ajcuarta
        elif nombre=='sin':
            from ajustadores import ajsin
            ajustador=ajsin
        elif nombre=='sinc':
            from ajustadores import ajsinc
            ajustador=ajsinc
        elif nombre=='cos':
            from ajustadores import ajcos
            ajustador=ajcos
        elif nombre=='cosc':
            from ajustadores import ajcosc
            ajustador=ajcosc
        elif nombre=='sinh':
            from ajustadores import ajsinh
            ajustador=ajsinh
        elif nombre=='cosh':
            from ajustadores import ajcosh
            ajustador=ajcosh
        elif nombre=='inv':
            from ajustadores import ajinv
            ajustador=ajinv
        elif nombre=='invcuad':
            from ajustadores import ajinvcuad
            ajustador=ajinvcuad

def equation_custom():
    global menu
    global ecuacioner
    global customizador
    ecuacioner.destroy()
    pedidor_numpar=Toplevel()
    pedidor_numpar.title('Función personalizada')
    pedidor_numpar.configure(background='midnight blue')
    pedidor_numpar.numparam=IntVar()
    pedidor_numpar.mensaje=Label(pedidor_numpar, text='Número de parámetros: ', bg="midnight blue", fg="snow", width=30)
    pedidor_numpar.num=Spinbox(pedidor_numpar, textvariable=pedidor_numpar.numparam, from_=1, to=12, wrap=True, state='readonly', width=15,fg="midnight blue")
    pedidor_numpar.aceptar=Button(pedidor_numpar, text='Aceptar', command=pedidor_numpar.destroy, width=8, height=2, bg="midnight blue", fg="lime green",activebackground="navy", activeforeground="snow")

    pedidor_numpar.mensaje.pack();pedidor_numpar.num.pack()
    pedidor_numpar.aceptar.pack()

    pedidor_numpar.num.focus_set()
    menu.wait_window(pedidor_numpar)

    num_param=pedidor_numpar.numparam.get()

    #Códigos Unicode
    cod1='\\u03B1=\u03B1, \\u03B2=\u03B2, \\u03B3=\u03B3\n\\u03B4=\u03B4, \\u03B5=\u03B5, \\u03B6=\u03B6\n\\u03B7=\u03B7'
    cod2=', \\u03B8=\u03B8, \\u03BB=\u03BB\n\\u03BC=\u03BC, \\u03BE=\u03BE, \\u03C0=\u03C0\n\\u03C1=\u03C1, \\u03C3=\u03C3'
    cod3=', \\u03C6=\u03C6\n\\u03C9=\u03C9, \\u0394=\u0394, \\u03A3=\u03A3\n\\u03A6=\u03A6, \\u03A9=\u03A9, \\u03B1=\u03B1'
    cod=cod1+cod2+cod3

    nombre_parametros=[]
    for i in range(num_param):
        pedidor_nompar=Toplevel()
        pedidor_nompar.title('Función personalizada')
        pedidor_nompar.configure(background='midnight blue')
        pedidor_nompar.nomparame=StringVar()
        pedidor_nompar.mensaje=Label(pedidor_nompar, text='Nombre del parámetro {0}: '.format(i+1), bg="midnight blue", fg="snow")
        pedidor_nompar.codigos=Label(pedidor_nompar, text=cod+'\n"Salir" para salir', bg="midnight blue", fg="snow")
        pedidor_nompar.nom=Entry(pedidor_nompar, textvariable=pedidor_nompar.nomparame,  bg="midnight blue", fg="snow", width=30)
        pedidor_nompar.aceptar=Button(pedidor_nompar, text='Aceptar', command=pedidor_nompar.destroy, width=15, bg="midnight blue", fg="lime green",activebackground="navy", activeforeground="snow")

        #pedidor_nompar.marco.pack()
        pedidor_nompar.codigos.pack()
        pedidor_nompar.mensaje.pack();pedidor_nompar.nom.pack()
        pedidor_nompar.aceptar.pack()

        pedidor_nompar.nom.focus_set()
        menu.wait_window(pedidor_nompar)

        parametro=pedidor_nompar.nomparame.get()

        nombre_parametros.append(parametro)


    if 'Salir' not in nombre_parametros and 'salir' not in nombre_parametros:
        formulador=Toplevel()
        formulador.title('Función personalizada')
        formulador.configure(background='midnight blue')
        formulador.formule=StringVar()
        formulador.mensaje=Label(formulador, text='y(x)= '.format(i+1), width=30, bg="midnight blue", fg="snow")
        formulador.codigos=Label(formulador, text=cod+'\n"Salir" para salir', bg="midnight blue", fg="snow")
        formulador.parametros=Label(formulador, text=nombre_parametros, bg="midnight blue", fg="snow")
        formulador.nom=Entry(formulador, textvariable=formulador.formule,  bg="midnight blue", fg="snow", width=30)
        formulador.aceptar=Button(formulador, text='Aceptar', command=formulador.destroy, width=15, bg="midnight blue", fg="lime green",activebackground="navy", activeforeground="snow")

        formulador.codigos.pack()
        formulador.mensaje.pack();formulador.nom.pack()
        formulador.aceptar.pack()

        formulador.nom.focus_set()
        menu.wait_window(formulador)

        formula=formulador.formule.get()

        if formula!='Salir' and formula!='salir' and formula!='s':
            patronln=r'ln'; patronsin=r'sin'; patroncos=r'cos';patronsinh=r'sinh';patroncosh=r'cosh';patrontan=r'tan';patrontanh=r'tanh'
            patronpi=r'pi'; patrone=r'e'

            formula=re.sub(patronln,'np.log', formula);formula=re.sub(patronsin,'np.sin', formula);
            formula=re.sub(patroncos,'np.cos', formula);formula=re.sub(patronsinh,'np.sinh', formula)
            formula=re.sub(patroncosh,'np.cosh', formula);formula=re.sub(patrontan,'np.tan', formula)
            formula=re.sub(patrontanh,'np.tanh', formula);formula=re.sub(patronpi,'np.pi', formula)
            formula=re.sub(patrone,'np.e', formula)

            #Creamos la definición
            definicion='#Funcion custom\ndef func_custom(t,'

            for i in range(num_param-1):
                definicion=definicion+nombre_parametros[i]+','
            definicion=definicion+nombre_parametros[-1]+'):\n'
            definicion=definicion+'    y='+formula+'\n    return y\n'
            definicion=re.sub(r'x', 't', definicion)

            ajustillo='\ndef ajcustom(datos, nombre_ajuste, x_name, y_name):\n'
            ajustillo+="    x = datos['%s'% x_name];ux=datos['u%s'% x_name];y=datos['%s'% y_name]; uy=datos['u%s'% y_name]\n"
            ajustillo+='    ajuste=curve_fit(func_custom,x,y,sigma=uy,absolute_sigma=True)\n    '

            for i in range(num_param-1):
                ajustillo+=nombre_parametros[i]+','
            if num_param!=1:
                ajustillo+=nombre_parametros[-1]+'=ajuste[0]\n    '
            else:
                ajustillo+=nombre_parametros[0]+'=ajuste[0][0]\n    '
            for i in range(num_param-1):
                ajustillo+='s'+nombre_parametros[i]+','
            if num_param!=1:
                ajustillo+='s'+nombre_parametros[-1]+'=np.sqrt(np.diag(ajuste[1]))'
            else:
                ajustillo+='s'+nombre_parametros[0]+'=np.sqrt(np.diag(ajuste[1]))[0]'

            for i in range(num_param):
                ajustillo+='\n    s'+nombre_parametros[i]+"='%.1E'% Decimal(s"+nombre_parametros[i]+")"
                ajustillo+='\n    usus'+nombre_parametros[i]+'=s'+nombre_parametros[i]+'[4:];usus'+nombre_parametros[i]+'=int(usus'+nombre_parametros[i]+')'
                ajustillo+='\n    '+nombre_parametros[i]+'=round('+nombre_parametros[i]+',1-usus'+nombre_parametros[i]+')\n'

            for i in range(num_param):
                ajustillo+="    v_{0}='".format(i+1)+nombre_parametros[i]+"={var} ,"+"\\\\u03C3("+nombre_parametros[i]
                ajustillo+=")={inc}'.format(var="+nombre_parametros[i]+', inc=s'+nombre_parametros[i]+')\n'

            ajustillo+='    texto='
            for i in range(num_param-1):
                ajustillo+="v_{0}+'\\\\n'+".format(i+1)
            ajustillo+="v_{0}\n".format(num_param)
            ajustillo+='    y_Ajus=func_custom(x,'
            for i in range(num_param-1):
                ajustillo+=nombre_parametros[i]+','
            ajustillo+=nombre_parametros[-1]+')\n'

            plotillo='    from matplotlib.font_manager import FontProperties\n    font0 = FontProperties();fontt = font0.copy()\n'
            plotillo+="    fontt.set_family('serif');fontt.set_size('xx-large');fontt.set_weight('semibold')\n"
            plotillo+="    fonta = font0.copy();fonta.set_family('serif');fonta.set_size('xx-large');fonta.set_style('italic')\n"
            plotillo+="    fig, ax =plt.subplots(figsize=(12,6))\n"
            plotillo+="    ax.plot(x, y_Ajus, color='black', lw=1.00, ls='-')\n"
            plotillo+="    ax.errorbar(x, y, fmt='o',markersize=5, yerr=uy, xerr=ux, ecolor='crimson', markerfacecolor='crimson', markeredgecolor='crimson')\n"
            plotillo+="    ax.set_title('%s'% nombre_ajuste,fontproperties=fontt)\n"
            plotillo+="    ax.set_xlabel('%s'% x_name, fontproperties=fonta);ax.set_ylabel('%s'% y_name, fontproperties=fonta)\n"
            plotillo+="    plt.savefig('Graficas/Ajuste %s.png' % nombre_ajuste, bbox_inches='tight')\n"
            plotillo+="    global menu\n    grafica=Toplevel()\n    grafica.title('%s'%nombre_ajuste)\n    grafica.configure(background='midnight blue')\n    "
            plotillo+="grafica.imagen=PhotoImage(file='Graficas/Ajuste %s.png'% nombre_ajuste)\n    from tkinter import font\n    "
            plotillo+="grafica.parametros=Label(grafica, text=texto, relief='ridge',borderwidth=3, bg='midnight blue', fg='snow')\n    "
            plotillo+="grafica.parametros.configure(font=('Courier', 5))\n    "
            plotillo+="grafica.image=Label(grafica, image=grafica.imagen, relief='ridge',borderwidth=3, bg='midnight blue', fg='snow')\n    "
            plotillo+="grafica.aceptar=Button(grafica, text='Aceptar', command=grafica.destroy, width=15, bg='midnight blue', fg='lime green',activebackground='navy', activeforeground='snow')\n    "
            plotillo+='grafica.ecuacion=Label(grafica, text="y='+formula+'",relief="ridge",borderwidth=3, bg="midnight blue", fg="snow")\n    '
            plotillo+="grafica.ecuacion.pack()\n    grafica.parametros.pack(side=LEFT);grafica.image.pack();grafica.aceptar.pack()\n"
            plotillo+="    grafica.aceptar.focus_set()\n#Fin custom"


            customizo=definicion+ajustillo+plotillo

            file=open('customizador.py', 'r')
            arch=file.read()
            file.close()

            patronsus=r'#Funcion custom\n(.*(\n)*)*\n#Fin custom'
            arch=re.sub(patronsus,customizo, arch)

            file=open('customizador.py', 'w')
            file.write(arch)
            file.close()

            global ajustador
            if 'customizador' not in sys.modules:
                import customizador as customizador
                ajustador=customizador.ajcustom
            else:
                from importlib import reload
                reload(customizador)
                ajustador=customizador.ajcustom

def ajustenormal():
    global menu
    llamada_ecuacion()
    global ecuacion; global ajustador
    if ecuacion!='Salir':
        question=messagebox.askyesno(message="¿Quiere ajuste en bucle?", title="Ajuste Normal")
        datos, xname, yname, grafname, nombre, tipo =llamada_datos()
        if type(datos)!=str:
            if question==True:
                ajustador(datos, grafname, xname, yname)
                evaluador=messagebox.askyesno(message="¿Continuar?", title="Ajuste %s"% grafname)
                while evaluador==True:
                    if tipo=='csv':
                        datos=documento_csv(nombre)
                    elif tipo=='xls':
                        datos=documento_excel(nombre)
                    elif tipo=='xlsx':
                        datos=documento_excel(nombre)
                    evaluador=messagebox.askyesno(message="¿Continuar?", title="Ajuste %s"% grafname)
            elif question==False:
                ajustador(datos,grafname, xname, yname)

def ajustemultiple():
    global menu
    llamada_ecuacion()
    global ecuacion; global ajustador
    if ecuacion!='Salir':
        numero=Toplevel()
        numero.title('Ajuste múltiple')
        numero.configure(background='midnight blue')
        numero.num=IntVar()
        numero.numm=Label(numero, text='Número de ajustes: ', bg="midnight blue", fg="snow", width=30, height=2)
        numero.numx=Spinbox(numero, textvariable=numero.num, from_=2, to=10, wrap=True, state='readonly',fg="midnight blue", width=18)
        numero.aceptar=Button(numero, text='Aceptar', command=numero.destroy, width=10, height=2, bg="midnight blue", fg="lime green",activebackground="navy", activeforeground="snow")

        numero.numm.pack();numero.numx.pack()
        numero.aceptar.pack()

        numero.numx.focus_set()
        menu.wait_window(numero)

        nume=numero.num.get()
        question=messagebox.askyesno(message="¿Quiere ajuste en bucle?", title="Ajuste Normal")
        datos=[]; xname=[]; yname=[]; grafname=[]; nombre=[]; tipo=[]
        for i in range(nume):
            if not 'Salir' in tipo:
                datosf, xnamef, ynamef, grafnamef, nombref, tipof=llamada_datos()
                datos.append(datosf);xname.append(xnamef);yname.append(ynamef);grafname.append(grafnamef);nombre.append(nombref);tipo.append(tipof)

        if not 'Salir' in tipo:
            if question==True:
                evaluador=[]
                for i in range(nume):
                    ajustador(datos[i], grafname[i], xname[i], yname[i])
                    evaluador.append(messagebox.askyesno(message="¿Continuar?", title="Ajuste {graf} ({var})".format(graf=grafname, var=i+1)))
                while True in evaluador:
                    for i in range(nume):
                        if evaluador[i]==True:
                            if tipo[i]=='csv':
                                datos[i]=documento_csv(nombre[i])
                            elif tipo[i]=='xls':
                                datos[i]=documento_excel(nombre[i])
                            elif tipo[i]=='xlsx':
                                datos[i]=documento_excel(nombre[i])
                            ajustador(datos[i], grafname[i], xname[i], yname[i])
                    for i in range(nume):
                        if evaluador[i]==True:
                            evaluador[i]=messagebox.askyesno(message="¿Continuar?", title="Ajuste {graf} ({var})".format(graf=grafname, var=i+1))
            elif question==False:
                for i in range(nume):
                    ajustador(datos[i],grafname[i], xname[i], yname[i])

def ajuste_comprobador():
    global menu
    global ajustador
    datos, xname, yname, grafname, nombre, tipo =llamada_datos()
    if tipo!='Salir':
        evaluador=True
        while evaluador==True:
            llamada_ecuacion()
            ajustador(datos, grafname, xname, yname)
            evaluador=messagebox.askyesno(message="¿Continuar?", title="Ajuste %s"% grafname)

def ajustador_total():
    datos, xname, yname, grafname, nombre, tipo =llamada_datos()
    if tipo!='Salir':
        global ecuacioner
        ecuacioner=Toplevel()
        transitor_1();ajustador(datos, grafname, xname, yname)
        transitor_2();ajustador(datos, grafname, xname, yname)
        transitor_3();ajustador(datos, grafname, xname, yname)
        transitor_4();ajustador(datos, grafname, xname, yname)
        transitor_5();ajustador(datos, grafname, xname, yname)
        transitor_6();ajustador(datos, grafname, xname, yname)
        transitor_7();ajustador(datos, grafname, xname, yname)
        transitor_8();ajustador(datos, grafname, xname, yname)
        transitor_9();ajustador(datos, grafname, xname, yname)
        transitor_10();ajustador(datos, grafname, xname, yname)
        transitor_11();ajustador(datos, grafname, xname, yname)
        transitor_12();ajustador(datos, grafname, xname, yname)
        transitor_13();ajustador(datos, grafname, xname, yname)
        transitor_14();ajustador(datos, grafname, xname, yname)
    

def menu_inicial():
    global menu
    menu=Tk()
    menu.title('Regresiones')
    menu.attributes('-fullscreen', False)
    menu.configure(background='midnight blue')
    menu.resizable(width=True,height=True)
    menu.mensaje =Label(menu, text="Bienvenido, científico. ¿Qué deseas hacer?", bg="midnight blue", fg="snow", width=39, height=3)
    menu.ajus_norm=Button(menu, text="Ajuste normal",command=ajustenormal, bg="midnight blue", fg="snow",activebackground="navy", activeforeground="snow", width=28, height=3)
    menu.ajus_multi=Button(menu, text="Ajuste multiple", command=ajustemultiple, bg="midnight blue", fg="snow",activebackground="navy", activeforeground="snow", width=28, height=3)
    menu.ajus_comprobador=Button(menu, text="Ajuste comprobador",command=ajuste_comprobador, bg="midnight blue", fg="snow",activebackground="navy", activeforeground="snow", width=28, height=3)
    menu.show_datos=Button(menu, text="Mirar datos",command=mirar_datos, bg="midnight blue", fg="snow",activebackground="navy", activeforeground="snow", width=28, height=3)
    menu.ajust_tot=Button(menu, text="Ajuste total", command=ajustador_total, bg="midnight blue", fg="snow",activebackground="navy", activeforeground="snow", width=28, height=3)
    menu.salir=Button(menu, text="Salir", width=7, command=salida, bg="midnight blue", fg="red2",activebackground="navy", activeforeground="snow", height=3)

    menu.mensaje.pack()
    menu.ajus_norm.pack();menu.ajus_multi.pack()
    menu.ajus_comprobador.pack();menu.ajust_tot.pack()
    menu.show_datos.pack()
    menu.salir.pack()
    menu.ajus_norm.focus_set()
    menu.wait_window(menu)
    menu.mainloop()

def salida():
    global menu
    salida=Toplevel()
    salida.title("Saliendo...")
    salida.resizable(width=False,height=False)
    salida.configure(background='midnight blue')
    salida.mensaje=Label(salida, text="¿Quiere salir?", bg="midnight blue", fg="snow", width=30, height=3)

    salida.cerrar=Button(salida, text='Sí', command=closer, width=15, bg="midnight blue", fg="red2",activebackground="navy", activeforeground="snow", height=3)   
    salida.abort=Button(salida, text='No', command=salida.destroy, width=15, bg="midnight blue", fg="cyan2",activebackground="navy", activeforeground="snow", height=3)

    salida.mensaje.pack(side=TOP, padx=5, pady=3)
    salida.cerrar.pack(side=LEFT, padx=3, pady=3);salida.abort.pack(side=RIGHT, padx=3, pady=3)

    salida.cerrar.focus_set()
    salida.transient(master=menu)
    menu.wait_window(salida)

def closer():
    global menu
    menu.destroy()
    from sys import exit
    sys.exit()

menu_inicial()
