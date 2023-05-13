import numpy as np

def spline(x, y, val):
    n= len(x)
    #Inicializa los coeficientes a,b,c y d como matrices de cero
    a, b, c, d= np.zeros(n), np.zeros(n), np.zeros(n),  np.zeros(n)
    
    #Inicializa la matriz h como una matriz de ceros
    h= np.zeros(n-1)
    
    #Inicializa la matriz alpha como una matriz de ceros
    alpha= np.zeros(n-1)
    
    #Incializar la matriz l como maatriz de unos
    l= np.ones(n)

    #Iniciañizar la matriz mu como una matriz de ceros
    mu= np.zeros(n-1)

    #Inicializar la matriz z como matriz de ceros
    z= np.zeros(n)

    #Calcular el valor de b[0]
    b[0]= (y[1]-y[0]) / (x[1]-x[0])

    #Calcular el valor de b[n-1]
    b[n-1]= (y[n-1] - y[n-2]) / (x[n-1] - x[n-2])

    for i in range (n-1):
        #Calcular valores de h[i]
        h[i]= x[i+1] - x[i]

    for i in range (1, n-1):
        #calcular valores de alpha[i]
        alpha[i]= 3.0/ h[i]* (y[i+1]- y[i])- 3.0/ h[i-1]* (y[i]- y[i-1])

    for i in range (1, n-1):
        #calcular los valores de l[i]
        l[i]= 2.0* (x[i+1]- x[i+1])- h[i-1]* mu[i-1]
        #calcular los valores de mu[i]
        mu[i]= h[i]/ l[i]
        #calcular los valeros de z[i]
        z[i]= (alpha[i]- h[i-1]* z[i-1]/ l[i])
    
    for i in range (n-2, -1, -1):
        #calcular los valores de c[i]
        c[i]= z[i]- mu[i]* c[i+1]
        #calcular los valores de b[i]
        b[i]= (y[i+1]-y[i])/ h[i]- h[i]* (c[i+1]+ 2.0* c[i])/ 3.0
        #calcular los valores de d[i]
        d[i]= (c[i+1]-c[i])/ (3.0* h[i])
        #calcular los valores de a[i]
        a[i]= y[i]

    for i in range (n-1):
        if val >= x[i] and val<= x[i+1]:
            #calcular el valor de dx
            dx= val- x[i]
            #Calcula el valor de la interpolacion
            result= a[i]+ b[i]* dx+ c[i]* dx* dx+ d[i]* dx* dx* dx
            #Devuelve el valor interpolado de y para x=val
            return result
    #devuelve  0 si el valor de x no esta en el rango de los puntos
    return 0.0

#Solicita al usuario a que infrese los datos de los punto
n= int(input("Ingrese el numero de puntos: "))
x= np.zeros(n)
y= np. zeros(n)
for i in range (n):
    x[i], y[i]= map(float, input("Ingrese el valor de x paara el punto {}: " .format(i+1)))

#Solicita al usuario que ingrese el valor de x para el cual quiere calcular la interpolacion
val= float(input("Ingrese el valor de x para el cual quiere obtener la interpolacion: "))

#Calcular la interpolacion y mostrar el resultado
result= spline(x, y, val)

#Muestra eñ resultado
print ("El valor interpoladdo de y para x = {} es {}" .format(val, result))