import modulos
import memoria
import sys

def menuprincipal():
    print("Menu")
    print("1. Agregar una línea.")
    print("2. Agregar una elipse o un círculo.")
    print("3. Agregar un rectángulo o un cuadrado.")
    print("4. Agregar un triangulo.")
    print("5. Mostrar un dibujo")
    print("6. Leer un dibujo.")
    print("7. Grabar un dibujo.")
    print("0. Salir del programa.")
    seleccion = int(input("Ingrese una opción: "))
    if seleccion == 1:
        x1 = int(input("x1 = "))
        y1 = int(input("y1 = "))
        x2 = int(input("x2 = "))
        y2 = int(input("y2 = "))
        modulos.recta(x1, y1, x2, y2)
        menuprincipal()


    elif seleccion == 2:
        curvas = int(input("Elija una variante: "))
        print("1. Círculo")
        print("2. Elipse")

        if curvas == 1:
            h = int(input("H:"))
            k = int(input("K:"))
            r = int(input("R:"))
            modulos.circulo(h, k, r)
            menuprincipal()

        elif curvas == 2:
            a = int(input("A:"))
            b = int(input("B:"))
            h = int(input("H:"))
            k = int(input("K:"))
            modulos.elipse(a, b, h, k)
            menuprincipal()

    elif seleccion == 3:
        x = int(input("X: "))
        y = int(input("Y: "))
        base = int(input("Base: "))
        altura = int(input("Altura: "))
        modulos.rectangulo_cuadrado(x, y, base, altura)
        menuprincipal()

    elif seleccion == 4:
        x = int(input("X: "))
        y = int(input("Y: "))
        base = int(input("Base: "))
        altura = int(input("Altura: "))
        modulos.triangulo(x, y, base, altura)
        menuprincipal()

    elif seleccion == 5:
        modulos.impresion()
        menuprincipal()

    elif seleccion == 6:
        nombre = input("Nombre del archivo")
        memoria.leer(nombre)
        menuprincipal()

    elif seleccion == 7:
        nombre = input("Nombre del archivo")
        modulos.escribir1(nombre)
        menuprincipal()
    elif seleccion == 0:
        sys.exit()
    else:
        print("Caracter no valido. Ingrese [0 - 7]")
        menuprincipal()


menuprincipal()

