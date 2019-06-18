# CADpy

# Requisitos

 Contar un programa IDLE que lea archivos .py
 No se necesita descargar ninguna libreria externa

# Instrucciones de uso:
  
  CADpy inicializa con un menú de 8 opciones que son:
       
       1. Agregar una línea 
        2. Agregar una elipse o circulo 
        3. Agregar un rectángulo o cuadrado 
        4. Agregar un triangulo 
        5. Mostrar un dibujo 
        6. Leer un dibujo 
        7. Grabar un dibujo 
       
       0. Salir del programa 
   El puntero del input estara listo para recibir un número correspondiente a la opción que quiera elegir.
   Las 4 primeras opciones son de trazo de dibujo y necesitan obtener parámetros que varian según el tipo de trazo.
       
       Linea: Coordenada inicial en x e y, Coordenada final en x e y 
        Elipse o circulo: Distancia del eje horizontal, Distancia del eje vertical, Coordenada del centro en x e y 
        Rectángulo o cuadrado: Coordenada que corresponde a la esquina inferior izquierda en x e y, base, altura
       Triángulo: Coordenada que corresponde a la esquina inferior izquierda en x e y, base, altura
   
   Las opciones 5 imprimira el plano cartesiano actual mientras que la opción 6 y 7 se encargan de abrir o guardar archivos que 
   se encuentren en la misma carpeta del proyecto, ambos pediran el nombre de los archivos.
   La última opción lo retirara del programa. 
# Descripción del programa:
 
 # Construcción
 
 matriz = []
 for i in range(44):
    matriz.append([])
    for j in range(84):
        matriz[i].append("  ") 
        
 El programa se construye con una matriz de 84 por 44, donde primero se crea una lista maestra donde se almacenaran sublistas(representando el eje y) y dentro de las sublistas iran espacios vacios. Representado gráficamente sera así:
 
 [" "," "," "," "," "," "," "," "]
 [" "," "," "," "," "," "," "," "]
 [" "," "," "," "," "," "," "," "]
 [" "," "," "," "," "," "," "," "]
 [" "," "," "," "," "," "," "," "]
 [" "," "," "," "," "," "," "," "]

Uno se puede desplazar con total libertad en la matriz usando los indices de la lista, primero el indice del eje y y luego el del eje x.
Ejemplo: Matriz[3][2]: Buscara en la cuarta fila de arriba a abajo y en la tercera columna de izquierda a derecha.

# Menú

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
        modulos.recta(x1,y1,x2,y2)
     
   El menú consta de 8 opciones que se acceden a ellas mediante un input y luego una condicional utilizando el número ordinal de la opción, internamente se busca que opción corresponde a ese número, se piden los inputs de la operación y se ejecuta la función. Cabe 
   resaltar que se debe importar las funciones de las librerias modulo y memoria antes.
 
# Memoria

def escribir(nombre):
    with open(nombre, "w") as f:
        for i in range(44):
            print(*matriz[i], sep=" ", file=f)

Inicialmente, Python almacena automaticamente los prints que ejecutemos dentro del programa hasta que lo cerremos, debido a que la matriz inicia vacia y se puede ir llenando con las funciones. Sin embargo, si se desea almacenar un archivo se necesita utilizar las librerias de la memoria. Dentro de ellas, se vuelve a imprimir la matriz en su totalidad pero la impresión es almacenada en un archivo donde el nombre es escogido por el usuario, luego de ello, el usuario puede abrirlo e imprimirlo en la pantalla.

def leer(nombre):
    try:
        with open(nombre) as f:
            text = f.read()
    except FileNotFoundError:
        text = none

    print(text)

# Modulos

Recta

Para la impresión de la recta hay que darse cuenta que existen dos casos, uno donde no existe la pendiente y no se debe utilizar 
la ecuación de la recta y uno donde si existe pendiente e inclusive puede ser cero, así sí se puede utilizar la ecuación. La primera parte de la función se dedica al reconocimiento de si la pendiente existe y en caso no como debe graficarla, para ello solo itera un rango de valores colocados por la diferencia de las coordenadas y donde solo el punto y aumenta formando una linea vertical.

def recta(x1,y1,x2,y2):
    if (x2-x1) ==0:
        if (y2-y1)>0:
            for i in range(y2-y1+1):
                matriz[-y2-2+i][x1+1]="x"
        elif (y2-y1)<0:
            for i in range(abs(y2-y1)+1):
                matriz[-y2-2-i][x1+1]="x"
        else:
            matriz[-y1-2][x1+1]="x"
    
En los casos donde si existe, se subdividen en pendiente negativa- positiva o cero. Las pendientes positivas y negativas se pueden tratar con la ecuación y evaluando la variable x en un for que itera desde el x1 al x2. Para la impresión, debe primero colocarse la coordenada en y (debe ser entero al ser un indice) y luego la coordenada en x . Los aumentos en los indices se deben a que parte de la matriz es ocupada por en un encuandre de puntos y la recta numérica en ambos ejes.     
    
    
    
    else:
        m = (y2 - y1) / (x2 - x1)
        if m > 0 or m < 0:
            x3 = 0
            x4 = 0
            if (x2 < x1 and y1 > y2) or (x1 > x2 and y2 > y1):
                x3 = x2
                x4 = x1
                for i in range(x3, x4 + 1):
                    ecuacion = m * i + m * (-x1) + y1
                    matriz[-int(ecuacion)-2][i+1] = "x"
            else:
                for i in range(x1, x2 + 1):
                    ecuacion = m * i + m * (-x1) + y1
                    matriz[-int(ecuacion)-2][i+1] = "x"
        
 En los casos de pendiente cero no hay la necesidad de utilizar la ecuación de la recta y sigue el mismo principio de impresión.
        
        
        elif m==0:
            if (x2-x1 )> 0:
                for i in range(x2-x1+1):
                    matriz[-y1-2][x1+1+i]="x"
            elif (x2-x1) <0:
                for i in range(abs(x2-x1)+1):
                    matriz[-y1-2][x1+1-i]="x"
        else:
            print("Ingrese un valor correcto")


Rectángulo

Para la construcción del rectángulo, se utiliza la función recta donde se evalua en cada uno de las esquinas hacia la otra esquina sea. 
Es arbitrario que orden de esquinas se toma con que no se tracen rectas en diagonal.


def rectangulo_cuadrado(x,y,base,altura):
    recta(x,y,x,y+altura)
    recta(x,y,x+base,y)
    recta(x,y+altura,x+base,y+altura)
    recta(x+base,y,x+base,y+altura)

Triangulo:

Un caso similar al rectángulo donde tambien se usan las rectas aunque hay que tomar precauciones. Lo recomendables es que la primera linea empiece de la esquina inferior izquierda y tenga como punto final la coordenada donde se encuentra la mitad de la base y la altura máxima(la punta del triángulo), de la misma manera de ese punto se parte hacia la esquina inferior derecha y finalmente se traza una linea de pendiente 0 para formar la base.

def triangulo(x,y,base,altura):
    recta(x,y,x+base,y)
    recta(x,y,x+int((base/2)),y+altura)
    recta(x+base,y,x+int(base/2),y+altura)

Elipse y triangulo:

Los casos del elipse y triangulo son particulares ya que no son funciones como tal. Si se despeja la variable dependiente(y) y independiente(x) se puede gráficar un cemicirculo o semielipse que se asemeja a una parabola. Sin embargo, la misma ecuación nos proporciona una herramienta eficaz

        y = round(sqrt(r**2-((i-h)**2))+k)
        matriz[-int(y)-2][i+1] = "x"
        y = round(-sqrt(r**2-((i-h)**2))+k)
        matriz[-int(y)-2][i+1] = "x"

    y = round(sqrt(r**2-((i-h)**2))+k)
    y = round(-sqrt(r**2-((i-h)**2))+k)
    
Por último, se esta la opción de imprimir que tan solo debe imprimir cada lista de manera vertical con un formato donde no haya corchetes y comillas por los strings

def impresion():
    for i in range(44):
        print(*matriz[i], sep=" ")
        
# Memoria

Python tiene la capacidad de manejar archivos .txt, el modo w es para write o escribir, a para append o escribir al final y r para read o leer. El acceso se da mediane el comando with con el nombre del archivo, el modo de uso y un nombre para el archivo como variable.

El primer comando utiliza tambien la posibilidad de un try, except para que si ocurre errores el programa continue en corriendo. 
IMPORTANTE: Los archivos van a almacenarse en la misma carpeta.

Para leer el archivo tan solo hay que utilizar el comando .read() donde antes del punto hay el nombre del archivo como variable.

def leer(nombre):
    try:
        with open(nombre) as f:
            text = f.read()
    except FileNotFoundError:
        text = none

    print(text)
    
Para escribir en el archivo se trabaja de la siguiente manera, python escribira en el archivo todo lo que se solia imprimir en la pantalla, por lo que, para este caso, tan solo se debe repetir el comando de impresión pero dentro del comando with con el modo "w".

def escribir(nombre):
    with open(nombre, "w") as f:
        for i in range(44):
            print(*matriz[i], sep=" ", file=f)
        
        
# Participantes
  Oscar De la Cruz Velasquez
  Marcelo Contreras Cabrera
  Ivan Del Carpio Cheme
