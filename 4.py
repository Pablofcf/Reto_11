def sumar_columnas_de_una_matriz (P=list, x=int, y=int)->float:

    suma_columna = 0
    for fcf in range (x):
        suma_columna += (P[fcf][y-1])

    return suma_columna

if __name__ == "__main__":
    x=int(input("Digite el número de filas que tendrá la Matriz P: "))
    e=int(input("Digite el número de columnas que tendrá la Matriz P: "))
    
    P = []

    for fcf in range (x):
        P1 = []
        for ff in range (e):
            p=float(input(f"¿Qué valor irá en ({fcf+1} , {ff+1})?: "))
            P1.append (p)
        P.append (P1)

    y=int(input("¿Qué columna desea sumar?: "))

sumar_columna = sumar_columnas_de_una_matriz(P,x,y)

print (f"La suma de los elementos de la {y} columna de la matriz {P} es igual a {sumar_columna}")