import numpy as np # Importa la biblioteca numpy con el alias np
import sympy as sym # Importa la biblioteca sympy con el alias sym
import matplotlib.pyplot as plt # Importa la biblioteca matplotlib.pyplot con el alias plt

def traza3natural(xi,yi): # Define una función llamada traza3natural que toma dos argumentos: xi y yi
    n = len(xi) # Calcula la longitud de la lista xi y la almacena en la variable n
    
    # Valores h
    h = np.zeros(n-1, dtype = float) # Crea un arreglo de ceros llamado h con una longitud de n-1
    for j in range(0,n-1,1): # Recorre desde 0 hasta n-1
        h[j] = xi[j+1] - xi[j] # Calcula los valores de h[j] como la diferencia entre los valores consecutivos de xi 

    # Sistema de ecuaciones
    A = np.zeros(shape=(n-2,n-2), dtype = float) # Crea un arreglo de ceros llamado A con una forma de (n-2,n-2)
    B = np.zeros(n-2, dtype = float) # Crea un arreglo de ceros llamado B con una longitud de n-2
    S = np.zeros(n, dtype = float) # Crea un arreglo de ceros llamado S con una longitud de n
    A[0,0] = 2*(h[0]+h[1]) # Asigna un valor a la posición [0,0] del arreglo A
    A[0,1] = h[1] # Asigna un valor a la posición [0,1] del arreglo A
    B[0] = 6*((yi[2]-yi[1])/h[1] - (yi[1]-yi[0])/h[0]) # Asigna un valor a la posición [0] del arreglo B
        
    for i in range(1,n-3,1): # Recorre desde 1 hasta n-3
        A[i,i-1] = h[i] # Asigna un valor a la posición [i,i-1] del arreglo A
        A[i,i] = 2*(h[i]+h[i+1]) # Asigna un valor a la posición [i,i] del arreglo A
        A[i,i+1] = h[i+1] # Asigna un valor a la posición [i,i+1] del arreglo A
        factor21 = (yi[i+2]-yi[i+1])/h[i+1]
        factor10 = (yi[i+1]-yi[i])/h[i]
        B[i] = 6*(factor21 - factor10) # Asigna un valor a la posición [i] del arreglo B
        A[n-3,n-4] = h[n-3] # Asigna un valor a la posición [n-3,n-4] del arreglo A
        A[n-3,n-3] = 2*(h[n-3]+h[n-2]) # Asigna un valor a la posición [n-3,n-3] del arreglo A
    factor12 = (yi[n-1]-yi[n-2])/h[n-2]
    factor23 = (yi[n-2]-yi[n-3])/h[n-3]
    B[n-3] = 6*(factor12 - factor23) # Asigna un valor a la posición [n-3] del arreglo B

    # Resolver sistema de ecuaciones S
    r = np.linalg.solve(A,B) # Resuelve el sistema de ecuaciones lineales Ax=B y almacena el resultado en r
    for j in range(1,n-1,1):
        S[j] = r[j-1]
        S[0] = 0
        S[n-1] = 0

    # Coeficientes
    a = np.zeros(n-1, dtype = float) # Crea un arreglo de ceros llamado a con una longitud de n-1
    b = np.zeros(n-1, dtype = float) # Crea un arreglo de ceros llamado b con una longitud de n-1
    c = np.zeros(n-1, dtype = float) # Crea un arreglo de ceros llamado c con una longitud de n-1
    d = np.zeros(n-1, dtype = float) # Crea un arreglo de ceros llamado d con una longitud de n-1
        
    for j in range(0,n-1,1):
        a[j] = (S[j+1]-S[j])/(6*h[j]) # Asigna un valor a la posición [j] del arreglo a
        b[j] = S[j]/2 # Asigna un valor a la posición [j] del arreglo b
        factor10 = (yi[j+1]-yi[j])/h[j]
        c[j] = factor10 - (2*h[j]*S[j]+h[j]*S[j+1])/6 # Asigna un valor a la posición [j] del arreglo c
        d[j] = yi[j] # Asigna un valor a la posición [j] del arreglo d

   
    # Polinomio trazador
    x = sym.Symbol('x') # Crea un símbolo llamado x
    px_tabla = [] # Crea una lista vacía llamada px_tabla
    for j in range(0,n-1,1): # Recorre desde 0 hasta n-1
        pxtramo = a[j]*(x-xi[j])**3 + b[j]*(x-xi[j])**2 # Calcula el valor de pxtramo
        pxtramo = pxtramo + c[j]*(x-xi[j])+ d[j] # Agrega el valor de c[j]*(x-xi[j])+ d[j] a pxtramo
        pxtramo = pxtramo.expand() # Expande la expresión de pxtramo
        px_tabla.append(pxtramo) # Agrega el valor de pxtramo a la lista px_tabla
    return(px_tabla) # Retorna el valor de px_tabla

# INGRESO , Datos de prueba
xi = list(map(float, input('Ingresa los valores de x separados por espacios: ').split())) # Pide al usuario que ingrese los valores de x separados por espacios y los almacena en la lista xi
fi = list(map(float, input('Ingresa los valores de y separados por espacios: ').split())) # Pide al usuario que ingrese los valores de y separados por espacios y los almacena en la lista fi
muestras = 10 # Asigna el valor 10 a la variable, esta mostrara los puntos por cada tramo de polinomio


# PROCEDIMIENTO
# Tabla de polinomios por tramos
n = len(xi) # Calcula la longitud de la lista xi y la almacena en la variable n
px_tabla = traza3natural(xi,fi) # Llama a la función traza3natural con los argumentos xi y fi y almacena el resultado en la variable px_tabla

# SALIDA
print('Polinomios por tramos: ') # Imprime el mensaje "Polinomios por tramos: "
for tramo in range(1,n,1): # Recorre desde 1 hasta n
    print(' x = ['+str(xi[tramo-1]) +','+str(xi[tramo])+']') # Imprime el intervalo de x para el tramo actual
    print(str(px_tabla[tramo-1])) # Imprime el polinomio trazador para el tramo actual


# GRAFICA
# Puntos para graficar cada tramo
xtraza = np.array([]) # Crea un arreglo vacío llamado xtraza
ytraza = np.array([]) # Crea un arreglo vacío llamado ytraza
tramo = 1 # Asigna el valor 1 a la variable tramo

while not(tramo>=n): # Mientras tramo sea menor que n
    a = xi[tramo-1] # Asigna el valor de xi[tramo-1] a la variable a
    b = xi[tramo] # Asigna el valor de xi[tramo] a la variable b
    xtramo = np.linspace(a,b,muestras) # Crea un arreglo de muestras puntos igualmente espaciados entre a y b y lo almacena en xtramo
    
    # evalua polinomio del tramo
    pxtramo = px_tabla[tramo-1] # Asigna el valor de px_tabla[tramo-1] a la variable pxtramo
    pxt = sym.lambdify('x',pxtramo) # Crea una función lambda a partir de la expresión pxtramo y la almacena en pxt
    ytramo = pxt(xtramo) # Evalúa la función pxt en los puntos xtramo y almacena el resultado en ytramo
    
    # vectores de trazador en x,y
    xtraza = np.concatenate((xtraza,xtramo)) # Concatena los valores de xtraza y xtramo y almacena el resultado en xtraza
    ytraza = np.concatenate((ytraza,ytramo)) # Concatena los valores de ytraza y ytramo y almacena el resultado en ytraza
    tramo = tramo + 1 # Incrementa el valor de tramo en 1


# Gráfica
plt.plot(xi,fi,'ro', label='puntos') # Grafica los puntos (xi,fi) con marcadores rojos en forma de círculo
plt.plot(xtraza,ytraza, label='trazador' , color='blue') # Grafica la curva (xtraza,ytraza) con color azul y etiqueta 'trazador'
plt.title('Trazadores Cúbicos Naturales') # Agrega el título 'Trazadores Cúbicos Naturales' a la gráfica
plt.xlabel('xi') # Agrega la etiqueta 'xi' al eje x
plt.ylabel('px(xi)') # Agrega la etiqueta 'px(xi)' al eje y
plt.legend() # Muestra la leyenda de la gráfica
plt.show() # Muestra la gráfica en pantalla
