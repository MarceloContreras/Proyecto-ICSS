def leer(nombre):
    try:
        with open(nombre) as f:
            text = f.read()
    except FileNotFoundError:
        text = none

    print(text)

def escribir(nombre):
    with open(nombre, "w") as f:
        for i in range(44):
            print(*matriz[i], sep=" ", file=f)