def matriz_transpuesta (P=list, x=int, y=int)->list:


    Pa = []


    for fcf in range (y):
        Pa1 = []
        for ff in range (x):
            pa = (P[ff][fcf])
            Pa1.append (pa)
        Pa.append (Pa1)


    return Pa


if __name__ == "__main__":
    x=int(input("Digite el número de filas que tendrá la Matriz P: "))
    y=int(input("Digite el número de columnas que tendrá la Matriz P: "))
   
    P = []


    for fcf in range (x):
        P1 = []
        for ff in range (y):
            p=float(input(f"¿Qué valor irá en ({fcf+1} , {ff+1})?: "))
            P1.append (p)
        P.append (P1)


print ("Matriz original: ")
for fila in P:
    print (fila)


print ("Matriz transpuesta: ")
for fila in (matriz_transpuesta(P,x,y)):
    print (fila)
