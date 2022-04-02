from cgitb import text
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from math import sqrt
import tkinter as tk
from tkinter import ttk

raiz = Tk()
raiz.title("Ventana principal")
raiz.geometry("400x200")
raiz.resizable(False,False)


def abrirPrim():
    def calPrim():
        ini = cuadroTexto.get()
        fin = cuadroTexto2.get()
        listaResul = []
        cont = 0
        for num in range(int(ini), int(fin) + 1):
                contNoPrimos = 0
                i = 2
                while i < num and contNoPrimos == 0:
                    modulo = num % i
                    if modulo == 0:
                            contNoPrimos += 1
                    else:
                        i += 1

                if contNoPrimos == 0:
                    cont += 1
                    listaResul.append(num)    
                    if 1 in listaResul:
                        listaResul.remove(1)
                    else: 
                        continue
        messagebox.showinfo(message= "se encuentran" + " " + str(len(listaResul)) + " " + "numeros primos en el rango dado, los cuales son: "+
        str(listaResul))
    ventanaPrimos = Toplevel()
    ventanaPrimos.title("Encontrar numeros primos")
    ventanaPrimos.geometry("400x250")
    raiz.resizable(False,False)
    miLabel = Label(ventanaPrimos, text="Encuentre los números primos", font= ("Courier", 14, "italic"))
    miLabel.place(x = "20", y = "10")

    cuadroTexto = Entry(ventanaPrimos)
    cuadroTexto.place(x= "210", y = "80")
    cuadroTexto.config(justify="left")

    cuadroTexto2 = Entry(ventanaPrimos)
    cuadroTexto2.place(x= "210", y = "150")
    cuadroTexto2.config(justify="left")

    labelNInicial = Label(ventanaPrimos, text= "Ingrese el numero de inicio: ", font= ("Courier", 7, "italic"))
    labelNInicial.place(x= "50", y = "80")


    labelNFin = Label(ventanaPrimos, text= "Ingrese el numero del final: ", font= ("Courier", 7, "italic"))
    labelNFin.place(x= "50", y = "150")

    botonHallar = Button(ventanaPrimos, text = "Calcular", command= calPrim, font= ("Courier", 10, "italic"))
    botonHallar.place(x = 180, y = 200)
    
def abrFibo():
    ventanaFibo = Toplevel()
    ventanaFibo.title("Encontrar la secuencia Fibonacci")
    ventanaFibo.geometry("500x300")
    ventanaFibo.resizable(False,False)

    miLabel = Label(ventanaFibo, text="Encuentre la secuencia de Fibonacci en un rango ingresado", font= (18))
    miLabel.place(x = "15", y = "10")

    cuadroTexto = Entry(ventanaFibo)
    cuadroTexto.place(x= "210", y = "80")
    cuadroTexto.config(justify="left")

    cuadroTexto2 = Entry(ventanaFibo)
    cuadroTexto2.place(x= "210", y = "150")
    cuadroTexto2.config(justify="left")

    labelNInicial = Label(ventanaFibo, text= "Ingrese el numero de inicio: ")
    labelNInicial.place(x= "50", y = "80")


    labelNFin = Label(ventanaFibo, text= "Ingrese el numero de finalizacion: ")
    labelNFin.place(x= "20", y = "150")

    def verifi(n):
        return ((1+sqrt(5))*n-(1-sqrt(5))*n)/(2*n*sqrt(5))

    def fibonacci():
        listaResul = []
        ini = float(cuadroTexto.get())
        fin = float(cuadroTexto2.get())
        n = 0
        num = verifi(n)
        while num <= fin:
            if ini <= num:
                listaResul.append(num)
            n += 1
            num = verifi(n)

        messagebox.showinfo(message= "Los numeros de Fibonacci en el rango ingresado son: " + str(listaResul))


    botonHallar = Button(ventanaFibo, text = "Encontrar", command= fibonacci)
    botonHallar.place(x = 180, y = 220)

def abrBases():
    ventanaBases = Toplevel()
    ventanaBases.title("Conversion de bases")
    ventanaBases.geometry("450x180")
    ventanaBases.resizable(False,False)

    labelTop = tk.Label(ventanaBases,
                    text = "Ingrese el numero y la base a la que desea convertir:", font= ("Courier", 8, "italic"))
    labelTop.place(x = "40", y = "30")

    cuadroTexto = Entry(ventanaBases)
    cuadroTexto.place(x= "160", y = "70")
    cuadroTexto.config(justify="center")

    comboBases = ttk.Combobox(ventanaBases, state= 'readonly')
    comboBases.place(x = "150", y = "100")

    opciones = ["Base 6", "Base 7", "Base 8", "Base 9"] 

    comboBases['values'] = opciones

    def base6(n):
        fin = []
        resultado = []
        while n != 0:
            fin.append(n % 6)
            n = n // 6
        for i in reversed(fin):
            resultado.append(i)
        messagebox.showinfo(message= "El numero en base 6 es: "+ ''.join(map(str, resultado)))

    def base7(n):
        fin = []
        resultado = []
        while n != 0:
            fin.append(n % 7)
            n = n // 7
        for i in reversed(fin):
            resultado.append(i)
        messagebox.showinfo(message= "El numero en base 7 es: "+ ''.join(map(str, resultado)))

    def base8(n):
        fin = []
        resultado = []
        while n != 0:
            fin.append(n % 8)
            n = n // 8
        for i in reversed(fin):
            resultado.append(i)
        messagebox.showinfo(message= "El numero en base 8 es: "+ ''.join(map(str, resultado)))

    def base9(n):
        fin = []
        resultado = []
        while n != 0:
            fin.append(n % 9)
            n = n // 9
        for i in reversed(fin):
            resultado.append(i)
        messagebox.showinfo(message= "El numero en base 9 es: "+ ''.join(map(str, resultado)))
        resultado.clear()

    def cambioBase():
        if comboBases.get() == "Base 6":
            base6(int(cuadroTexto.get()))
        elif comboBases.get() == "Base 7":
            base7(int(cuadroTexto.get()))
        elif comboBases.get() == "Base 8":
            base8(int(cuadroTexto.get()))
        elif comboBases.get() == "Base 9":
            base9(int(cuadroTexto.get()))

    botonConvertir = Button(ventanaBases, text = "Convertir", command= cambioBase, font= ("Courier", 8, "italic"))
    botonConvertir.place(x = 180, y = 140)
    

labelQueDesea = Label(raiz, text= "¿Que operacion deseas realizar?", font= ("Courier", 10, "italic"))
labelQueDesea.place(x = 15, y = 20)

botonFibonacci = Button(raiz, text = "Encontrar numeros primos", command= abrirPrim, font= ("Courier", 10, "italic"))
botonFibonacci.place(x = 35, y = 60)

botonBases = Button(raiz, text = "Encontrar la secuencia de Fibonacci", command=abrFibo, font= ("Courier", 10, "italic"))
botonBases.place(x = 35, y = 110)

botonPrimos = Button(raiz, text = "Conversion de bases", command=abrBases, font= ("Courier", 10, "italic"))
botonPrimos.place(x = 35, y = 160)

raiz.mainloop()