from math import sqrt
matriz = []
for i in range(44):
    matriz.append([])
    for j in range(84):
        matriz[i].append("  ")


for i in range(43):
    for j in range(83):
        matriz[-i-2][0]=str(i)
        matriz[43][j+1]=str(j)
        matriz[-i-2][1]="."
        matriz[0][j+1]=" ."
        matriz[42][j+1]=" ."
        matriz[-i-2][83]= "."

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
        elif m==0:
            if (x2-x1 )> 0:
                for i in range(x2-x1+1):
                    matriz[-y1-2][x1+1+i]="x"
            elif (x2-x1) <0:
                for i in range(abs(x2-x1)+1):
                    matriz[-y1-2][x1+1-i]="x"
        else:
            print("Ingrese un valor correcto")


def rectangulo_cuadrado(x,y,base,altura):
    recta(x,y,x,y+altura)
    recta(x,y,x+base,y)
    recta(x,y+altura,x+base,y+altura)
    recta(x+base,y,x+base,y+altura)

def triangulo(x,y,base,altura):
    recta(x,y,x+base,y)
    recta(x,y,x+int((base/2)),y+altura)
    recta(x+base,y,x+int(base/2),y+altura)

def circulo(h,k,r):
    for i in range(h-r, h+r + 1):
        y = round(sqrt(r**2-((i-h)**2))+k)
        matriz[-int(y)-2][i+1] = "x"
        y = round(-sqrt(r**2-((i-h)**2))+k)
        matriz[-int(y)-2][i+1] = "x"

def elipse(a,b,h,k):
   if a>b:
     for i in range (h-a,h+a+1):
       ecuacion = round(((b**2-(b**(2)*(i-h)**2)/a**2)**1/2)+k)
       matriz[-int(ecuacion)-2][i+1]="x"
       ecuacion = round(-((b ** 2 - (b ** (2) * (i - h) ** 2) / a ** 2) ** 1 / 2) + k)
       matriz[-int(ecuacion)-2][i+1]="x"
   elif b>a:
     for i in range (h-a,h+a+1):
       ecuacion = round(((a**2-(a**(2)*(i-h)**2)/b**2)**1/2)+k)
       matriz[-int(ecuacion)-2][i+1]="x"
       ecuacion = round(-((a ** 2 - (a ** (2) * (i - h) ** 2) / b ** 2) ** 1 / 2) + k)
       matriz[-int(ecuacion)-2][i+1]="x"

def impresion():
    for i in range(44):
        print(*matriz[i], sep=" ")

def escribir1(nombre):
    with open(nombre, "w") as f:
        for i in range(44):
            print(*matriz[i], sep=" ", file=f)