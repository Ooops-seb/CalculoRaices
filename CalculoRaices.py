#METODOS NUMERICOS
#   Nombre: Erik Villarreal
#   24 de noviembre 2022

from os import system
import sympy as sp
import numpy as np
import math
from matplotlib import pyplot

##DECLARACION FUNCIONES
def main():
    tolerancia = float(0.001)
    while True:
        system("cls")
        menu()
        op=int(input("Ingrese una opción: "))
        if op==1:
            system("cls")
            OPbiseccion()
            aux=input("\nPresione Enter para continuar...")
            system("cls")
        elif op==2:
            system("cls")
            OPsecante()
            aux=input("\nPresione Enter para continuar...")
            system("cls")
        elif op==3:
            system("cls")
            OPnewton()
            aux=input("\nPresione Enter para continuar...")
            system("cls")
        elif op==4:
            system("cls")
            tolerancia=error(tolerancia)
            aux=input("\nPresione Enter para continuar...")
            system("cls")
        elif op==5:
            print("Saliendo del programa...")
            break
        else:
            print("\n\t***OPCIÓN INVÁLIDA - INGRESE DE NUEVO***")

def menu():
    print("\n***MÉTODOS NUMÉRICOS***")
    print("\t1. Método de Bisección")
    print("\t2. Método de Secante")
    print("\t3. Método de Newton")
    print("\t4. Ver índice de tolerancia")
    print("\t5. SALIR")

def OPbiseccion():
    print("***MÉTODO DE BISECCIÓN***")
    ecuacion=input("Ingrese ecuación: ")
    print("\n***INTERVALO***")
    x0=float(input("Ingrese x0: "))
    x1=float(input("Ingrese x1: "))
    iteracciones_biseccion = 0
    respuesta_biseccion = biseccion(ecuacion, x0, x1)

def OPsecante():
    print("***MÉTODO DE SECANTE***")
    ecuacion=input("Ingrese ecuación: ")
    print("***INTERVALO***")
    x0=float(input("Ingrese x0: "))
    x1=float(input("Ingrese x1: "))
    iteracciones_secante = 0
    respuesta_secante = secante(ecuacion, x0, x1)

def OPnewton():
    print("***MÉTODO DE NEWTON***")
    ecuacion=input("Ingrese ecuación: ")
    x=float(input("Ingrese x0: "))
    iteracciones_newton = 0
    respuesta_newton = newton(ecuacion, x)

def newton(f, xn_1, iteracciones_newton=20):
    xn = float(0)
    auxTol = float(0.1)
    x = sp.symbols('x')
    print("\t***ITERACCIONES***")
    for n in range (iteracciones_newton):
        fun = sp.sympify(f).subs(x,xn_1)
        Fx = sp.sympify(sp.diff(f)).subs(x,xn_1)
        if(auxTol>tolerancia):
            iteracciones_newton+=1
            xn = xn_1 - (fun/Fx)
            if n == 0:
                print("\nValor incial: ", xn_1)
            else:
                print("\n",n , ": ", xn_1)
            auxTol=abs((xn-xn_1)/xn)
            aux = xn
            xn = xn_1
            xn_1 = aux
        elif(auxTol<tolerancia):
            break
        if(Fx == 0):
            print("Derivada es 0")
            break

    print("\nEl punto es: ", xn)
    print("Con un número de iteracciones: ", iteracciones_newton-21)
    print("\t¿Desea Graficar el punto?")
    print("1. SI\t2. NO")
    while True:
        op=int(input("Ingrese valor: "))
        if op == 1:
            graficar(f, xn) 
            return xn
        if op == 2:
            break
        else:
            print("\n\t***OPCIÓN INVÁLIDA - INGRESE DE NUEVO***")

def secante(f, x0, x1, iteracciones_secante=20):
    xn = float(0.0)
    x = sp.symbols('x')
    auxTol = float(0.1)
    funA = sp.sympify(f).subs(x, x0)
    funB = sp.sympify(f).subs(x, x1)
    print("\t***ITERACCIONES***")
    for n in range (iteracciones_secante):
        if (funA*funB) >= 0:
            print("No se puede aplicar el método.")
            return None
        elif auxTol > tolerancia:
            iteracciones_secante+=1
            num = funB * (x0 - x1)
            den = funA - funB
            xn = x1 -(num/den)
            funAux = sp.sympify(f).subs(x, xn)
            print("\n",n+1 , ": ", xn)
            if funAux == 0:
                return xn
            elif funA * funAux <0:
                x1 = xn
            else:
                x0 = xn
            auxTol=abs((xn-x1)/xn)
        else:
            break
    print("\nEl punto es: ", xn)
    print("Con un número de iteracciones: ", iteracciones_secante-20)
    print("\t¿Desea Graficar el punto?")
    print("1. SI\t2. NO")
    while True:
        op=int(input("Ingrese valor: "))
        if op == 1:
            graficar(f, xn) 
            return xn
        if op == 2:
            break
        else:
            print("\n\t***OPCIÓN INVÁLIDA - INGRESE DE NUEVO***")

def biseccion(f, a, b):
    x = sp.symbols('x')
    funA = sp.sympify(f).subs(x, a)
    funB = sp.sympify(f).subs(x, b)
    aux=b-a
    iteracciones_biseccion=round(math.log((aux/tolerancia),2))
    if funA * funB > 0:
        print("No existe raiz")
    else:
        print("\t***ITERACCIONES***")
        for n in range(iteracciones_biseccion):
            xn = (a + b) / 2
            print("\n",n+1 , ": ", xn)
            funX = sp.sympify(f).subs(x, xn)
            if funX == 0:
                return xn
            if funA * funX < 0:
                b = xn
            else:
                a = xn

    print("\nEl punto es: ", xn)
    print("Con un número de iteracciones: ", iteracciones_biseccion)
    print("\t¿Desea Graficar el punto?")
    print("1. SI\t2. NO")
    while True:
        op=int(input("Ingrese valor: "))
        if op == 1:
            graficar(f, xn) 
            return xn
        if op == 2:
            break
        else:
            print("\n\t***OPCIÓN INVÁLIDA - INGRESE DE NUEVO***")


def error(tolerancia):
    print("\n\t***TOLERANCIA***")
    print("La índice de tolerancia actual es: ", tolerancia)
    print("\t¿Desea editarlo?")
    print("1. SI\t2. NO")
    op=int(input("Ingrese valor: "))
    if op == 1:
        while True:
            print("\n\tLa tolerancia debe ser menor a 1")
            tolerancia=float(input("Ingrese valor: "))
            if(tolerancia<=1):
                print("\tCambio realizado...")
                break
            else:
                print("***VALOR INVÁLIDO - INGRESE DE NUEVO***")
        return tolerancia
    if op == 2:
        return tolerancia
    else:
        print("\n\t***OPCIÓN INVÁLIDA - INGRESE DE NUEVO***")

def graficar(f, xn):
    def f1(x):
        return  eval(f)
    x = np.linspace(-10, 10, 500)
    pyplot.plot(x, [f1(i) for i in x], color="g")
    pyplot.plot(xn, 0, "o", color = "y")

    pyplot.axhline(0, color="Blue", linestyle = ":")
    pyplot.axvline(0, color="Blue", linestyle = ":")

    pyplot.xlim(-10, 10)
    pyplot.ylim(-10, 10)
    pyplot.show()
    

##DECLARACION VARIABLES
tolerancia = float(0.001)

##INICIO
main()