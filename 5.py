def sumar_filas_de_una_matriz (P=list, x=int, y=int)->float:

    suma_fila = 0
    for fcf in range (x):
        suma_fila += (P[fcf][y-1])

    return suma_fila

if __name__ == "__main__":
    e=int(input("Digite el número de filas que tendrá la Matriz P: "))
    x=int(input("Digite el número de columnas que tendrá la Matriz P: "))
    
    P = []

    for fcf in range (e):
        P1 = []
        for ff in range (e):
            p=float(input(f"¿Qué valor irá en ({fcf+1} , {ff+1})?: "))
            P1.append (p)
        P.append (P1)

    y=int(input("¿Qué fila desea sumar?: "))

sumar_fila = sumar_filas_de_una_matriz(P,x,y)

print (f"La suma de los elementos de la {y} columna de la matriz {P} es igual a {sumar_fila}")