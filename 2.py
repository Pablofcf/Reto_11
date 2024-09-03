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
