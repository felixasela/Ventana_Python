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
    

    def abrirCombinacion():
    ventanaComb = Toplevel()
    ventanaComb.title("Combinaciones")
    ventanaComb.geometry("500x300")
    ventanaComb.resizable(False,False)

    miLabel = Label(ventanaComb, text="Realice la combinación a partir de los datos dados", font= (18))
    miLabel.place(x = "65", y = "10")

    cTotal = Entry(ventanaComb)
    cTotal.place(x= "250", y = "80")
    cTotal.config(justify="right")

    cCom = Entry(ventanaComb)
    cCom.place(x= "300", y = "150")
    cCom.config(justify="right")

    labelNInicial = Label(ventanaComb, text= "Ingrese el numero total de elementos: ")
    labelNInicial.place(x= "50", y = "80")


    labelNFinal = Label(ventanaComb, text= "Ingrese el numero de elementos que desea combinar: ")
    labelNFinal.place(x= "50", y = "150")

    
    def factorial(num): 
        if num < 0: 
            messagebox.showinfo(message= "ERROR, un numero es negativo")

        elif num == 0: 
            return 1
        else: 
            fact = 1
            while(num > 1): 
                fact *= num 
                num -= 1
            return fact 

    def combinacion():
        proceso = (factorial(int(cTotal.get())))/(factorial(int(cCom.get()))*factorial(int(cTotal.get())-int(cCom.get())))
        messagebox.showinfo(message= "La combinacion de " + str(cCom.get()) + " en " + str(cTotal.get()) + " es " + str(proceso))



    botonHallar = Button(ventanaComb, text = "Hallar", command=combinacion) 
    botonHallar.place(x = 180, y = 220)

def abrirCombinacionR():
    ventanaCombR = Toplevel()
    ventanaCombR.title("Combinaciones con repeticion")
    ventanaCombR.geometry("500x300")
    ventanaCombR.resizable(False,False)

    miLabel = Label(ventanaCombR, text="Realice la combinación con repeticion a partir de los datos dados", font= (18))
    miLabel.place(x = "25", y = "10")

    cTotal = Entry(ventanaCombR)
    cTotal.place(x= "250", y = "80")
    cTotal.config(justify="right")

    cCom = Entry(ventanaCombR)
    cCom.place(x= "300", y = "150")
    cCom.config(justify="right")

    labelNInicial = Label(ventanaCombR, text= "Ingrese el numero total de elementos: ")
    labelNInicial.place(x= "50", y = "80")


    labelNFinal = Label(ventanaCombR, text= "Ingrese el numero de elementos que desea combinar: ")
    labelNFinal.place(x= "50", y = "150")

    
    def factorial(num): 
        if num < 0: 
            messagebox.showinfo(message= "ERROR, un numero es negativo")

        elif num == 0: 
            return 1
        else: 
            fact = 1
            while(num > 1): 
                fact *= num 
                num -= 1
            return fact 

    def combinacionR():
        proceso = (factorial((int(cTotal.get())+int(cCom.get())-1)))/(factorial(int(cCom.get()))*factorial(int(cTotal.get())-1))
        messagebox.showinfo(message= "La combinacion con repeticion de " + str(cCom.get()) + " en " + str(cTotal.get()) + " es " + str(proceso))



    botonHallar = Button(ventanaCombR, text = "Hallar", command=combinacionR) 
    botonHallar.place(x = 180, y = 220)

def abrirPermutacion():
    ventanaP = Toplevel()
    ventanaP.title("Permutacion sin repeticion")
    ventanaP.geometry("500x300")
    ventanaP.resizable(False,False)

    miLabel = Label(ventanaP, text="Realice la permutacion sin repeticion a partir de los datos dados", font= (18))
    miLabel.place(x = "25", y = "10")

    cTotal = Entry(ventanaP)
    cTotal.place(x= "250", y = "80")
    cTotal.config(justify="right")

    cCom = Entry(ventanaP)
    cCom.place(x= "300", y = "150")
    cCom.config(justify="right")

    labelNInicial = Label(ventanaP, text= "Ingrese el numero total de elementos: ")
    labelNInicial.place(x= "50", y = "80")


    labelNFinal = Label(ventanaP, text= "Ingrese el numero de elementos que desea combinar: ")
    labelNFinal.place(x= "50", y = "150")

    
    def factorial(num): 
        if num < 0: 
            messagebox.showinfo(message= "ERROR, un numero es negativo")

        elif num == 0: 
            return 1
        else: 
            fact = 1
            while(num > 1): 
                fact *= num 
                num -= 1
            return fact 

    def permutacionR():
        if cTotal == cCom:
            proceso = factorial(int(cTotal.get()))
            messagebox.showinfo(message= "La permutacion de " + str(cCom.get()) + " en " + str(cTotal.get()) + " es " + str(proceso))
        else:
            proceso = (factorial((int(cTotal.get()))))/(factorial(int(cTotal.get())-int(cCom.get())))
            messagebox.showinfo(message= "La permutacion de " + str(cCom.get()) + " en " + str(cTotal.get()) + " es " + str(proceso))



    botonHallar = Button(ventanaP, text = "Hallar", command=permutacionR) 
    botonHallar.place(x = 180, y = 220)

def abrirPermutacionR():
    ventanaPR = Toplevel()
    ventanaPR.title("Permutacion con repeticion")
    ventanaPR.geometry("500x400")
    ventanaPR.resizable(False,False)

    miLabel = Label(ventanaPR, text="Realice la permutacion con repeticion a partir de los datos dados", font= (18))
    miLabel.place(x = "25", y = "10")

    cTotal = Entry(ventanaPR)
    cTotal.place(x= "250", y = "80")
    cTotal.config(justify="right")

    elementos = Entry(ventanaPR)
    elementos.place(x= "300", y = "150")
    elementos.config(justify="right")

    elementos2 = Entry(ventanaPR)
    elementos2.place(x= "300", y = "200")
    elementos2.config(justify="right")

    elementos3 = Entry(ventanaPR)
    elementos3.place(x= "300", y = "250")
    elementos3.config(justify="right")

    labelNInicial = Label(ventanaPR, text= "Ingrese el numero total de elementos: ")
    labelNInicial.place(x= "50", y = "80")

    labelNFinal = Label(ventanaPR, text= "Ingrese las veces que se repite el primer elemento: ")
    labelNFinal.place(x= "50", y = "150")

    labelNFinal = Label(ventanaPR, text= "Ingrese las veces que se repite el segundo elemento: ")
    labelNFinal.place(x= "50", y = "200")

    labelNFinal = Label(ventanaPR, text= "Ingrese las veces que se repite el tercer elemento: ")
    labelNFinal.place(x= "50", y = "250")

    
    def factorial(num): 
        if num < 0: 
            messagebox.showinfo(message= "ERROR, un numero es negativo")

        elif num == 0: 
            return 1
        else: 
            fact = 1
            while(num > 1): 
                fact *= num 
                num -= 1
            return fact 

    def permutacionR():
        proceso = (factorial((int(cTotal.get()))))/(factorial(int(elementos.get()))*factorial(int(elementos2.get()))*factorial(int(elementos3.get())))
        messagebox.showinfo(message= "La permutacion de " + str(cTotal.get()) + " repitiendo los elementos dados es " + str(proceso))



    botonHallar = Button(ventanaPR, text = "Hallar", command=permutacionR) 
    botonHallar.place(x = 180, y = 300)
    
labelQueDesea = Label(raiz, text= "¿Que operacion deseas realizar?", font= ("Courier", 10, "italic"))
labelQueDesea.place(x = 15, y = 20)

botonFibonacci = Button(raiz, text = "Encontrar numeros primos", command= abrirPrim, font= ("Courier", 10, "italic"))
botonFibonacci.place(x = 35, y = 60)

botonBases = Button(raiz, text = "Encontrar la secuencia de Fibonacci", command=abrFibo, font= ("Courier", 10, "italic"))
botonBases.place(x = 35, y = 110)

botonPrimos = Button(raiz, text = "Conversion de bases", command=abrBases, font= ("Courier", 10, "italic"))
botonPrimos.place(x = 35, y = 160)

botonComb = Button(raiz, text = "Combinacion sin repeticion", command=abrirCombinacion)
botonComb.place(x = 165, y = 270)

botonCombR = Button(raiz, text = "Combinacion con repeticion", command=abrirCombinacionR)
botonCombR.place(x = 165, y = 320)

botonPer = Button(raiz, text = "Permutacion sin repeticion", command=abrirPermutacion)
botonPer.place(x = 165, y = 370)

botonPerR = Button(raiz, text = "Permutacion con repeticion", command=abrirPermutacionR)
botonPerR.place(x = 165, y = 420)


raiz.mainloop()
