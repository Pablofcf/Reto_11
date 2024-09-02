# Reto_11

1. Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
#Creamos 2 matrices
matriz1=[[1,2,3],[4,5,6],[7,8,9]]
matriz2=[[9,8,7],[6,5,4],[3,2,1]]
#Creamos una función
def sumaMatrices(a, b):
    #Condicion de que las 2 listas sean de igual longitud
    if len(a) == len(b) and len(a[0])==len(b[0]):


        d=[]
        for i in range(len(a[0])):
            d.append([])
            for j in range(len(b[0])):
                d[i].append(a[i][j] + b[i][j])
        return d
    else:
        return None
if __name__=="__main__":
 c= sumaMatrices(matriz1,matriz2)
 if c == None:
    print("No se puede sumar")
 else:
    for fila in c:
        print("[", end=" ")
        for elemento in fila:
            print(elemento, end=" ")
        print("]")
```
2. Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
'''Producto de matrices'''
#Reciclamos las 2 matrices
matriz1=[[1,2,3],[4,5,6],[7,8,9]]
matriz2=[[9,8,7],[6,5,4],[3,2,1]]
#Creamos una función para el producto
def productoMatriz(a, b):
    #Condicion de que las 2 listas sean de igual longitud
    if len(a) == len(b) and len(a[0])==len(b[0]):


        d=[]
        for i in range(len(a[0])):
            d.append([])
            for j in range(len(b[0])):
                #Aqui multiplicamos los indices de la 1ra matriz con los de la 2da
                d[i].append(a[i][j] * b[i][j])
        return d
    else:
        return None
if __name__=="__main__":
 c= productoMatriz(matriz1,matriz2)
 if c == None:
    print("No se puede multiplicar")
 else:
    for fila in c:
        print("[", end=" ")
        for elemento in fila:
            print(elemento, end=" ")
        print("]")
```
3. Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
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
```
4. Desarrollar un programa que sume los elementos de una columna dada de una matriz.

```python

```
5. Desarrollar un programa que sume los elementos de una fila dada de una matriz.

```python

```
